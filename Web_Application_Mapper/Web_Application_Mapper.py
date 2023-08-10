import os
import threading
import requests

threads = 10
target = "http://www.test.com"
directory = "/Users/justin/Downloads/joomla-3.1.1"
filters = [".jpg", ".gif", ".png", ".css"]

os.chdir(directory)
web_paths = []

for r, d, f in os.walk("."):
    for files in f:
        remote_path = os.path.join(r, files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.append(remote_path)


def test_remote():
    while True:
        try:
            path = web_paths.pop()
        except IndexError:
            break

        url = f"{target}{path}"
        try:
            response = requests.get(url)
            print(f"[{response.status_code}] => {path}")
        except requests.HTTPError as error:
            print(f"Failed {error}")
            pass


threads_list = []

for i in range(threads):
    print(f"Spawning thread: {i}")
    t = threading.Thread(target=test_remote)
    t.start()
    threads_list.append(t)

for t in threads_list:
    t.join()
