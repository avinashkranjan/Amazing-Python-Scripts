# Package/Script Name

Short description of package/script

-->Package installed- NLKT
- NLTK stands for 'Natural Language Tool Kit'. It consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, sentiment analysis, topic segmentation, and named entity recognition. NLTK helps the computer to analysis, preprocess, and understand the written text.


## Setup instructions

--> Explanation on how to setup and run your package/script locally
- simply import the NLKT package by writing 'import nlkt' in first line of your script.
- To run the script locally save the 'Tagged_Hindi_Corpus.txt' file at your favourable location.
- In code, in fp=open(r"..."), give the location of your saved file as mentioned in previous step.
- In code, in fd=open(r"..."), give the location where you want the file with only Hindi text after removal of POS.
- Note that for this script, I have run the script therefore only_hindi.txt file already exists. Before executing your script make sure you delete 'only_hindi.txt' file and see   it after running the script.
- Run the script with "python hindi_POS_tag_removal.py OR python <name of your py file.py>"
- You will be able to see the file with only Hindi text.


## Detailed explanation of script, if needed

Script is written as follows:

- Open the hindi_tagged_corpus file.
- Data tokenization.
- Create 2 empty lists.
- To get all categories from POS.
- To get all the hindi words.
- To concatenate the words.
- To write the words in only_hindi file.

## Input

![Image](C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\Input.png)

## Output
![Image](C:\Users\ZAVERI SANYA\Desktop\Amazing-Python-Scripts\Remove_POS_hindi_text\Output.png)


## Author(s)

- This code is written by Sanya Devansh Zaveri. [https://github.com/zaverisanya]

## Disclaimers, if any

There are no disclaimers for this script.
