from sklearn.feature_extraction.text import CountVectorizer
import nltk
import pandas as pd  # pandas is a library where your data can be stored, analyzed and processed in row and column representation
from openpyxl import Workbook
sentences = input("Enter your sentences: ")
# eg. My name is sanya. I am caring and loving. I am generous.
# converting to lower case (normalization)
sentences = sentences.lower()
# sentence tokenized
tokenized_sentences = nltk.tokenize.sent_tokenize(sentences)
print(tokenized_sentences)
tokenized_sentences1 = []
for x in tokenized_sentences:
    x = x.replace(".", "")  # removed .
    tokenized_sentences1.append(x)
# list of word can be converted to set to get unique words
print(tokenized_sentences1)
# instantiating CountVectorizer()
countVectorizer = CountVectorizer()  # BOW
# transforming text from to vectors where each word and its count is a feature
# pass list of sentences as arguments
tmpbow = countVectorizer.fit_transform(tokenized_sentences1)
print("tmpbow \n", tmpbow)  # bag of word model is ready

bow = tmpbow.toarray()
print("Vocabulary = ", countVectorizer.vocabulary_)
print("Features = ", countVectorizer.get_feature_names())
# Features in machine learning are nothing but names of the columns
print("BOW ", bow)

# create dataframe  #DataFrame is an analogy to excel-spreadsheet
cv_dataframe = pd.DataFrame(bow, columns=countVectorizer.get_feature_names())

print("cv_dataframe is below\n", cv_dataframe)
cv_dataframe.to_excel('./Bag of words model/bowp.xlsx', sheet_name='data')
