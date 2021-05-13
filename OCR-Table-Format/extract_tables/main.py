import argparse

from table_ocr.extract_tables import main

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")
args = parser.parse_args()
files = args.files
results = main(files)
for image, tables in results:
    print("\n".join(tables))
