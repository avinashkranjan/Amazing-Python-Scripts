import os

# Define the JPEG signature header and footer
header = b"\xff\xd8\xff"
footer = b"\xff\xd9"

# Initialize global counters
file_cnt = 0
dir_cnt = 0

# Directory search


def fileSearch(dir_path, cnt):
    global file_cnt
    global dir_cnt
    filelist = []

    for _ in range(cnt):
        print("\t", end=" ")
    print("[>] Directory: %s" % dir_path)
    for files in os.listdir(dir_path):
        full_path = os.path.join(dir_path, files)
        if os.path.isfile(full_path):
            filelist.append(full_path)
            for _ in range(cnt):
                print("\t", end=" ")
            print("[+] File Name: %s" % files)
            file_cnt += 1
        elif os.path.isdir(full_path):
            for i in range(cnt):
                print("\t", end=" ")
            print(
                "[!] SubDirectory: \"%s\" found. Start file search in this directory." % files)
            filelist.extend(fileSearch(full_path, cnt + 1))
            dir_cnt += 1

    return filelist

# File open and store carved file


def Carving(file_list):
    cnt = 0
    carv_list = []
    print("====================Carving Start====================")
    for i in range(len(file_list)):
        with open(file_list[i], 'rb') as file:
            carv_cont = findSignature(file)
            print("[-] ", file_list[i], " File passed")

            if len(carv_cont) != 0:
                carv_name = f'carv{cnt}.jpeg'
                with open(carv_name, 'wb') as carv:
                    for j in range(len(carv_cont)):
                        carv.write(carv_cont[j])
                print(f'[*] {carv_name} is created!')
                carv_list.append(carv_name)
                cnt += 1

    return carv_list

# Find signature


def findSignature(file):
    flag = 0
    contents = []

    while True:
        buf = file.read(0x200)
        if len(buf) == 0:
            break
        if flag != 1:
            is_head = buf[:3]
            if header == is_head and flag == 0:
                contents.append(buf)
                flag = 1
        else:
            if footer in buf[-2:]:
                contents.append(buf)
                return contents
            else:
                contents.append(buf)
    return contents


# Main
if __name__ == "__main__":
    print("==================File Search Start==================")
    fl = fileSearch("./", 0)
    print(f'\nSEARCH RESULT: {file_cnt} Files. {dir_cnt} Directory.')
    print(f"Filelist: {fl}\n")
    c1 = Carving(fl)
    print(f"Carvlist: {c1}\n")

    print("Exit...")
