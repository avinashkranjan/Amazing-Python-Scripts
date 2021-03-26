import string
import nltk

fp=open(r"C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\\Tagged_Hindi_Corpus.txt",mode="r",encoding="utf-8") #opens the hindi_tagged_corpus.txt file
fd=open(r"C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\\Only_Hindi.txt",mode="a",encoding="utf-8")
data=fp.read()
data_token=nltk.tokenize.word_tokenize(data) #data tokenization
words=[]
categories=[]
for i in data_token:
    charc=i.split('|')
    if(len(charc)>2):
        ch=charc[2].split(".")
        categories.append(ch[0])  #This gives all the categories of POS tags
        if i not in string.punctuation and len(charc[0])>1:
               words.append(charc[0]) #This gives the list of hindi words
str=""
for word in words:
    str+=word+" " #it concatenates the words
fd.write(str) #writes to only_hindi.txt file
fp.close()
fd.close()
