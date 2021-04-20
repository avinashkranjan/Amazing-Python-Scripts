# importing required libraries
import pandas as pd
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
import re
warnings.filterwarnings("ignore")

# reading the dataset
msg = pd.read_csv(
    "./Message_Spam_Detection/Cleaned_Dataset.csv", encoding='latin-1')
msg.drop(['Unnamed: 0'], axis=1, inplace=True)

# seperating target and features
y = pd.DataFrame(msg.label)
x = msg.drop(['label'], axis=1)

# countvectorization
cv = CountVectorizer(max_features=5000)
temp1 = cv.fit_transform(x['final_text'].values.astype('U')).toarray()
tf = TfidfTransformer()
temp1 = tf.fit_transform(temp1)
temp1 = pd.DataFrame(temp1.toarray(), index=x.index)
x = pd.concat([x, temp1], axis=1, sort=False)

# drop final_text col
x.drop(['final_text'], axis=1, inplace=True)

# converting to int datatype
y = y.astype(int)

# randomforstclassifier model
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(x, y)

# User input
text = input("Enter text: ")

# data cleaning/preprocessing - removing punctuation and digits
updated_text = ''
for i in range(len(text)):
    if text[i] not in string.punctuation:
        if text[i].isdigit() == False:
            updated_text = updated_text+text[i]
text = updated_text

# data clearning/preprocessing - tokenization and convert to lower case
text = re.split("\W+", text.lower())

# data cleaning/preprocessing - stopwords
updated_list = []
stopwords = nltk.corpus.stopwords.words('english')
for i in range(len(text)):
    if text[i] not in stopwords:
        updated_list.append(text[i])
text = updated_list

# data cleaning/preprocessing - lemmentizing
updated_list = []
wordlem = nltk.WordNetLemmatizer()
for i in range(len(text)):
    updated_list.append(wordlem.lemmatize(text[i]))
text = updated_list

# data cleaning/preprocessing - mergining token
text = " ".join(text)

text = cv.transform([text])
text = tf.transform(text)
pred = model.predict(text)
if pred == 0:
    print("Not Spam")
else:
    print("Spam")
