import string
import nltk
import sys
import os

user_input = input(' Enter file location of your Tagged Hindi Text: ')
# C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\\Tagged_Hindi_Corpus.txt
assert os.path.exists(
    user_input), "I did not find the file at, "+str(user_input)
# opens the hindi_tagged_corpus.txt file
fp = open(user_input, mode="r", encoding="utf-8")
print("Hooray we found your file!")

user_answer = input(
    ' Enter file location where you wish to get your Only Hindi Text file: ')
# C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\Only_Hindi.txt
fd = open(user_answer, mode="a", encoding="utf-8")
data = fp.read()
data_token = nltk.tokenize.word_tokenize(data)  # data tokenization
words = []
categories = []
for i in data_token:
    charc = i.split('|')
    if(len(charc) > 2):
        ch = charc[2].split(".")
        categories.append(ch[0])  # This gives all the categories of POS tags
        if i not in string.punctuation and len(charc[0]) > 1:
            words.append(charc[0])  # This gives the list of hindi words
str = ""
for word in words:
    str += word+" "  # it concatenates the words
fd.write(str)  # writes to only_hindi.txt file
print("Hooray your Only Hindi Text file is ready...Please Check!")
fp.close()
fd.close()
