import os
import wave
import simpleaudio as sa
import numpy as np
from scipy.io import wavfile


"""
  [NOTE] In this algorithm we make use of LSB Steganographic method of encoding. In this algorithm we have converted each charecter
  of the secret text into 8-bit binary string and then we have stored it to a numpy array of size x*8 where x = no. of charecters.
  After that we have copied the same into the LSB of the binary form of the audio file we have read.
"""


class Encrypt:

    def __init__(self, message_audio_file_path: str, secret_message: str):
        self.message_audio_file_path = message_audio_file_path
        self.secret_message = secret_message

        # For getting name of the file
        self.message_filename = message_audio_file_path.split(os.sep)[-1]

        # Reading the .wav audio file as a Wave obj - to be used later
        self.message_audio = wave.open(message_audio_file_path)

        # Getting the numpy array from the secret string.
        self.secret_as_nparr = self.get_bin_npapp_from_path(
            secret_message)

        self.mess_as_nparr = None

    """
      This function is used as a helper function
    """

    def get_bin_npapp_from_path(self, secret: str) -> np.ndarray:

        strings = ' '.join('{0:08b}'.format(ord(word), 'b')
                           for word in secret)
        lst = []
        for word in strings.split(" "):
            # arr = np.fromstring(word, dtype="u1")-ord('0')
            temp_lst = [int(i) for i in word]
            lst.append(np.array(temp_lst))

        return np.array(lst)

    """
      This function is there for playing audio.
    """

    def play_audio(self) -> None:

        playing = sa.WaveObject.from_wave_read(self.message_audio)
        obj = playing.play()

        if obj.is_playing():
            print(f"Playing audio : {self.message_filename}")

        obj.wait_done()

    """
      This function is for encryption
    """

    def encrypt_using_lsb(self, output_dir: str, file_name: str) -> (np.ndarray, bool):

        # Getting the ouput path
        curr_dir_path = os.getcwd()
        output_dir_path = os.path.join(curr_dir_path, output_dir)

        try:
            os.mkdir(output_dir_path)
        except:
            pass

        print(f"This might take some while if either your audio file or your secret message is big")

        # Reading shape of secret message and reshaping
        m1, n1 = self.secret_as_nparr.shape
        secret_reshape = self.secret_as_nparr.reshape(m1*n1, 1)

        # Reading the .wav file
        samplerate, self.mess_as_nparr = wavfile.read(
            self.message_audio_file_path)

        # Reading the shape of .wav file and reshaping
        m2, n2 = self.mess_as_nparr.shape
        message_reshape = self.mess_as_nparr.reshape(m2*n2, 1)

        # Edge case
        if m1*n1 > m2*n2:
            print("Coudn't be done")
            quit()

        # Encryption part
        k = 0
        for i in range(m2*n2):
            if k < m1*n1:
                # This line is for copying the bit off the secret message to the LSB of the audio
                message_reshape[i][0] = message_reshape[i][0] & 0xFE | secret_reshape[k][0]
                k += 1
            else:
                message_reshape[i][0] = 0
                break

        # Reshaping back again
        message_reshape = message_reshape.reshape(m2, n2)

        try:
            # Writing into ouput file
            p = wavfile.write(os.path.join(output_dir_path, file_name),
                              samplerate, message_reshape.astype(message_reshape.dtype))
            print("Success !!!")
            return message_reshape, True
        except:
            print("Error !!!")
            pass
            return None, False
