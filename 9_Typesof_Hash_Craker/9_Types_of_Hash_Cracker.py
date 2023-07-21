#!/usr/bin/env python3

import hashlib
import itertools
import multiprocessing
import os
import string
import threading
import time


class Cracker(object):
    ALPHA_LOWER = (string.ascii_lowercase,)
    ALPHA_UPPER = (string.ascii_uppercase,)
    ALPHA_MIXED = (string.ascii_lowercase, string.ascii_uppercase)
    PUNCTUATION = (string.punctuation,)
    NUMERIC = (''.join(map(str, range(0, 10))),)
    ALPHA_LOWER_NUMERIC = (string.ascii_lowercase,
                           ''.join(map(str, range(0, 10))))
    ALPHA_UPPER_NUMERIC = (string.ascii_uppercase,
                           ''.join(map(str, range(0, 10))))
    ALPHA_MIXED_NUMERIC = (
        string.ascii_lowercase, string.ascii_uppercase, ''.join(map(str, range(0, 10))))
    ALPHA_LOWER_PUNCTUATION = (string.ascii_lowercase, string.punctuation)
    ALPHA_UPPER_PUNCTUATION = (string.ascii_uppercase, string.punctuation)
    ALPHA_MIXED_PUNCTUATION = (
        string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
    NUMERIC_PUNCTUATION = (''.join(map(str, range(0, 10))), string.punctuation)
    ALPHA_LOWER_NUMERIC_PUNCTUATION = (string.ascii_lowercase, ''.join(
        map(str, range(0, 10))), string.punctuation)
    ALPHA_UPPER_NUMERIC_PUNCTUATION = (string.ascii_uppercase, ''.join(
        map(str, range(0, 10))), string.punctuation)
    ALPHA_MIXED_NUMERIC_PUNCTUATION = (
        string.ascii_lowercase, string.ascii_uppercase, ''.join(
            map(str, range(0, 10))), string.punctuation
    )

    def __init__(self, hash_type, hash, charset, progress_interval):
        """
        Sets the hash type and actual hash to be used
        :param hash_type: What algorithm we want to use
        :param hash: The hash in base64 format
        :return:
        """
        self.__charset = charset
        self.__curr_iter = 0
        self.__prev_iter = 0
        self.__curr_val = ""
        self.__progress_interval = progress_interval
        self.__hash_type = hash_type
        self.__hash = hash
        self.__hashers = {}

    def __init_hasher(self):
        hashlib_type = self.__hash_type if self.__hash_type != "ntlm" else "md4"
        self.__hashers[self.__hash_type] = hashlib.new(hashlib_type)

    def __encode_utf8(self, data):
        return data.encode("utf-8")

    def __encode_utf16le(self, data):
        return data.encode("utf-16le")

    @staticmethod
    def __search_space(charset, maxlength):
        """
        Generates the search space for us to attack using a generator
        We could never pregenerate this as it would take too much time and require godly amounts of memory
        For example, generating a search space with a rough size of 52^8 would take over 50TB of RAM
        :param charset: The character set to generate a search space for
        :param maxlength: Maximum length the search space should be capped at
        :return:
        """
        return (
            ''.join(candidate) for candidate in
            itertools.chain.from_iterable(
                itertools.product(charset, repeat=i) for i in
                range(1, maxlength + 1)
            )
        )

    def __attack(self, q, max_length):
        """
        Tries all possible combinations in the search space to try and find a match.
        This is an extremely tight loop so we need to inline and reduce work as much as we can in here.
        :param q: Work queue
        :param max_length: Maximum length of the character set to attack
        :return:
        """
        self.__init_hasher()
        self.start_reporting_progress()
        hash_fn = self.__encode_utf8 if self.__hash_type != "ntlm" else self.__encode_utf16le
        for value in self.__search_space(self.__charset, max_length):
            hasher = self.__hashers[self.__hash_type].copy()
            self.__curr_iter += 1
            self.__curr_val = value
            hasher.update(hash_fn(value))
            if self.__hash == hasher.hexdigest():
                q.put("FOUND")
                q.put("{}Match found! Password is {}{}".format(
                    os.linesep, value, os.linesep))
                self.stop_reporting_progress()
                return

        q.put("NOT FOUND")
        self.stop_reporting_progress()

    @staticmethod
    def work(work_q, done_q, max_length):
        """
        Take the data given to us from some process and kick off the work
        :param work_q: This is what will give us work from some other process
        :param done_q: Used to signal the parent from some other process when we are done
        :param max_length: Maximum length of the character set
        :return:
        """
        obj = work_q.get()
        obj.__attack(done_q, max_length)

    def start_reporting_progress(self):
        self.__progress_timer = threading.Timer(
            self.__progress_interval, self.start_reporting_progress)
        self.__progress_timer.start()
        print(
            f"Character set: {self.__charset}, iteration: {self.__curr_iter}, trying: {self.__curr_val}, hashes/sec: {self.__curr_iter - self.__prev_iter}",
            flush=True)
        self.__prev_iter = self.__curr_iter

    def stop_reporting_progress(self):
        self.__progress_timer.cancel()
        print(
            f"Finished character set {self.__charset} after {self.__curr_iter} iterations", flush=True)


if __name__ == "__main__":
    character_sets = {
        "01": Cracker.ALPHA_LOWER,
        "02": Cracker.ALPHA_UPPER,
        "03": Cracker.ALPHA_MIXED,
        "04": Cracker.NUMERIC,
        "05": Cracker.ALPHA_LOWER_NUMERIC,
        "06": Cracker.ALPHA_UPPER_NUMERIC,
        "07": Cracker.ALPHA_MIXED_NUMERIC,
        "08": Cracker.PUNCTUATION,
        "09": Cracker.ALPHA_LOWER_PUNCTUATION,
        "10": Cracker.ALPHA_UPPER_PUNCTUATION,
        "11": Cracker.ALPHA_MIXED_PUNCTUATION,
        "12": Cracker.NUMERIC_PUNCTUATION,
        "13": Cracker.ALPHA_LOWER_NUMERIC_PUNCTUATION,
        "14": Cracker.ALPHA_UPPER_NUMERIC_PUNCTUATION,
        "15": Cracker.ALPHA_MIXED_NUMERIC_PUNCTUATION
    }

    hashes = {
        "01": "MD5",
        "02": "MD4",
        "03": "LM",
        "04": "NTLM",
        "05": "SHA1",
        "06": "SHA224",
        "07": "SHA256",
        "08": "SHA384",
        "09": "SHA512"
    }

    prompt = "Specify the character set to use:{}{}".format(
        os.linesep, os.linesep)
    for key, value in sorted(character_sets.items()):
        prompt += "{}. {}{}".format(key, ''.join(value), os.linesep)

    while True:
        try:
            charset = input(prompt).zfill(2)
            selected_charset = character_sets[charset]
        except KeyError:
            print("{}Please select a valid character set{}".format(
                os.linesep, os.linesep))
            continue
        else:
            break

    prompt = "{}Specify the maximum possible length of the password: ".format(
        os.linesep)

    while True:
        try:
            password_length = int(input(prompt))
        except ValueError:
            print("{}Password length must be an integer".format(os.linesep))
            continue
        else:
            break

    prompt = "{}Specify the hash's type:{}".format(os.linesep, os.linesep)
    for key, value in sorted(hashes.items()):
        prompt += "{}. {}{}".format(key, value, os.linesep)

    while True:
        try:
            hash_type = hashes[input(prompt).zfill(2)]
        except KeyError:
            print("{}Please select a supported hash type".format(os.linesep))
            continue
        else:
            break

    prompt = "{}Specify the hash to be attacked: ".format(os.linesep)

    while True:
        try:
            user_hash = input(prompt)
        except ValueError:
            print("{}Something is wrong with the format of the hash. Please enter a valid hash".format(
                os.linesep))
            continue
        else:
            break

    print(f"Trying to crack hash {user_hash}", flush=True)
    processes = []
    work_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()
    progress_interval = 3
    cracker = Cracker(hash_type.lower(), user_hash.lower(),
                      ''.join(selected_charset), progress_interval)
    start_time = time.time()
    p = multiprocessing.Process(target=Cracker.work,
                                args=(work_queue, done_queue, password_length))
    processes.append(p)
    work_queue.put(cracker)
    p.start()

    if len(selected_charset) > 1:
        for i in range(len(selected_charset)):
            progress_interval += .2
            cracker = Cracker(hash_type.lower(), user_hash.lower(),
                              selected_charset[i], progress_interval)
            p = multiprocessing.Process(target=Cracker.work,
                                        args=(work_queue, done_queue, password_length))
            processes.append(p)
            work_queue.put(cracker)
            p.start()

    failures = 0
    while True:
        data = done_queue.get()
        if data == "NOT FOUND":
            failures += 1
        elif data == "FOUND":
            print(done_queue.get())
            for p in processes:
                p.terminate()

            break

        if failures == len(processes):
            print("{}No matches found{}".format(os.linesep, os.linesep))
            break

    print("Took {} seconds".format(time.time() - start_time))
