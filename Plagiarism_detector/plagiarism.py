from difflib import SequenceMatcher


def similarity_per(f1, f2):
    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
        file1_data = file1.read()
        file2_data = file2.read()
        similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
        print(f"these 2 files are {similarity*100} % similar")


if __name__ == '__main__':
    f1 = input("file 1 path :")
    f2 = input("file 2 path :")
    similarity_per(f1, f2)
