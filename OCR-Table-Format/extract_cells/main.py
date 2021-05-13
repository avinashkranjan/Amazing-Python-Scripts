import sys

from table_ocr.extract_cells import main

paths = main(sys.argv[1])
print("\n".join(paths))