# shellocr.py
# Extract OCR using Tesseract
# Created by Subhangi Choudhary

import subprocess
import shlex
# shlex is used for passing parameters

# subprocess.call(['./extract_text.sh'])
# Run above if no parameters are required

subprocess.call(shlex.split('./extract_text.sh ./pdf/ ./txt/'))