
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor as executor
from optparse import OptionParser


def printer(word):
    sys.stdout.write(word + "                                        \r")
    sys.stdout.flush()
    return True


yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"


def check_status(domain, url):
    if not url or url.startswith("#") or len(url) > 30:
        return False

    printer("Testing: " + domain + url)
    try:
        link = domain + url
        req = requests.head(link)
        st = str(req.status_code)
        if st.startswith(("2", "1")):
            print(green + "[+] " + st + " | Found: " + end + "[ " + url +
                  " ]" + "                                                   \r")
        elif st.startswith("3"):
            link = req.headers['Location']
            print(yellow + "[*] " + st + " | Redirection From: " + end + "[ " + url + " ]" + yellow +
                  " -> " + end + "[ " + link + " ]" + "                                         \r")
        elif st.startswith("4"):
            if st != '404':
                print(blue + "[!] " + st + " | Found: " + end + "[ " + url +
                      " ]" + "                                                   \r")
        return True
    except Exception:
        return False


def presearch(domain, ext, url):
    if ext == 'Null' or ext == 'None':
        check_status(domain, url)
    elif url and not url.isspace():
        ext_list = [ext] if ext != "None" else [""]
        for i in ext_list:
            link = url if not i else url + "." + str(i)
            check_status(domain, link)


def main():
    parser = OptionParser(green + """
#Usage:""" + yellow + """
    -t target host
    -w wordlist
    -d thread number (Optional, Default: 10)
    -e extensions (Optional, ex: html,php)
""" + green + """
#Example:""" + yellow + """
    python3 dirbrute.py -t domain.com -w dirlist.txt -d 20 -e php,html
""" + end)

    try:
        parser.add_option("-t", dest="target", type="string",
                          help="the target domain")
        parser.add_option("-w", dest="wordlist",
                          type="string", help="wordlist file")
        parser.add_option("-d", dest="thread", type="int",
                          help="the thread number")
        parser.add_option("-e", dest="extension",
                          type="string", help="the extensions")
        (options, _) = parser.parse_args()

        if not options.target or not options.wordlist:
            print(parser.usage)
            exit(1)

        target = options.target
        wordlist = options.wordlist
        thread = options.thread if options.thread else 10
        ext = options.extension if options.extension else "Null"

        target = target if target.startswith("http") else "http://" + target
        target = target if target.endswith("/") else target + "/"

        print("[" + yellow + bold + "Info" + end + "]:\n")
        print(blue + "[" + red + "+" + blue + "] Target: " + end + target)
        print(blue + "[" + red + "+" + blue + "] File: " + end + wordlist)
        print(blue + "[" + red + "+" + blue + "] Thread: " + end + str(thread))
        print(blue + "[" + red + "+" + blue + "] Extension: " + end + str(ext))
        print("\n[" + yellow + bold + "Start Searching" + end + "]:\n")

        ext_list = ext.split(",") if ext != "Null" else ["Null"]
        with open(wordlist, 'r') as urls:
            with executor(max_workers=int(thread)) as exe:
                jobs = [exe.submit(presearch, target, ext,
                                   url.strip('\n')) for url in urls]

        took = (time.time() - start) / 60
        print(red + "Took: " + end +
              f"{round(took, 2)} m" + "                          \r")

        print("\n\t* Happy Hacking *")

    except Exception as e:
        print(red + "#Error: " + end + str(e))
        exit(1)


if __name__ == '__main__':
    start = time.time()
    main()
