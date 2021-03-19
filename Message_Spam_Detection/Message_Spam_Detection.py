#importing required libraries
import pandas as pd
import string 
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")
nltk.download('stopwords')
nltk.download('wordnet')

#reading the dataset 
#dataset: https://www.kaggle.com/uciml/sms-spam-collection-dataset
msg=pd.read_csv("dataset.csv",encoding='latin-1')
msg.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1,inplace=True)
msg.rename(columns={"v1":"label","v2":"text"},inplace=True)

#mapping ham=0 and spam=1
for i in msg.index:
  if msg['label'][i]=='ham':
    msg['label'][i]=0
  else:
    msg['label'][i]=1

#dropping duplicate columns 
msg=msg.drop_duplicates()

#data cleaning/preprocessing - removing punctuation and digits 
msg['cleaned_text']=""
for i in msg.index:
  updated_list=[]
  for j in range(len(msg['text'][i])):
    if msg['text'][i][j] not in string.punctuation:
      if msg['text'][i][j].isdigit()==False:
        updated_list.append(msg['text'][i][j])
  updated_string="".join(updated_list)
  msg['cleaned_text'][i]=updated_string
msg.drop(['text'],axis=1,inplace=True)

#data clearning/preprocessing - tokenization and convert to lower case 
msg['token']=""
for i in msg.index:
  msg['token'][i]=re.split("\W+",msg['cleaned_text'][i].lower())

#data cleaning/preprocessing - stopwords
msg['updated_token']=""
stopwords=nltk.corpus.stopwords.words('english')
for i in msg.index:
  updated_list=[]
  for j in range(len(msg['token'][i])):
    if msg['token'][i][j] not in stopwords:
      updated_list.append(msg['token'][i][j])
  msg['updated_token'][i]=updated_list
msg.drop(['token'],axis=1,inplace=True)

#data cleaning/preprocessing - lemmentizing
msg['lem_text']=""
wordlem=nltk.WordNetLemmatizer()
for i in msg.index:
  updated_list=[]
  for j in range(len(msg['updated_token'][i])):
    updated_list.append(wordlem.lemmatize(msg['updated_token'][i][j]))
  msg['lem_text'][i]=updated_list 
msg.drop(['updated_token'],axis=1,inplace=True)

#data cleaning/preprocessing - mergining token
msg['final_text']=""
for i in msg.index:
  updated_string=" ".join(msg['lem_text'][i])
  msg['final_text'][i]=updated_string
msg.drop(['cleaned_text','lem_text'],axis=1,inplace=True)

#seperating target and features
y=pd.DataFrame(msg.label)
x=msg.drop(['label'],axis=1)

#countvectorization 
cv=CountVectorizer(max_features=5000)
temp1=cv.fit_transform(x['final_text']).toarray()
tf=TfidfTransformer()
temp1=tf.fit_transform(temp1)
temp1=pd.DataFrame(temp1.toarray(),index=x.index)
x=pd.concat([x,temp1],axis=1,sort=False)

#drop final_text col
x.drop(['final_text'],axis=1,inplace=True)

#converting to int datatype
y=y.astype(int)

#randomforstclassifier model
model=RandomForestClassifier(n_estimators=100,random_state=0)
model.fit(x,y)
filename="randomforest.sav"
pickle.dump(model,open(filename,"wb"))

#User input
text=input("Enter text: ")
text=cv.transform([text])
text=tf.transform(text)
model=pickle.load(open("randomforest.sav","rb"))
pred=model.predict(text)
if pred==0:
  print("Not Spam")
else:
  print("Spam")