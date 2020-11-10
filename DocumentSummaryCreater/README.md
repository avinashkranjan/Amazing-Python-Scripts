# Document-Summary-Creater
A python script to create a sentence summary

## Prerequisites
##### This script needs Python 3.*

pip install these libraries from requirements.txt
* sumy
* spacy
* neologdn

and run the command to download some libraries

```bash
$ python -m spacy download en_core_web_sm
$ python -c "import nltk; nltk.download('punkt')"
```

## Usage:
* Run main.py and enter the path of the text file
* After that, a text file that summarizes the read text file into two tenths is created
