#importing required libraries
import pandas as pd
import string 
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
import warnings
warnings.filterwarnings("ignore")
nltk.download('stopwords')
nltk.download('wordnet')

#reading the dataset 
#dataset: https://www.kaggle.com/uciml/sms-spam-collection-dataset
msg=pd.read_csv("spam.csv",encoding='latin-1')
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

#adding length column to dataset 
msg['length']=msg['text'].apply(len)

#on basis of data examination,found that spam contains numbers,emails,websites,symbols.
#using regex to check for numbers,emails,websites,symbols. 
#added a new column called 'contain', if any of the above thing are present, contain=1 else contain=0
msg['contain']=msg['text'].str.contains('£').map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains('%').map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains('€').map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains('\$').map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("T&C").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("www|WWW").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("http|HTTP").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("https|HTTPS").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("@").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("email|Email|EMAIL").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("SMS|sms|FREEPHONE").map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("\d{11}",regex=True).map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("\d{10}",regex=True).map({False:0,True:1})
msg['contain']=msg['contain']|msg['text'].str.contains("\d{5}",regex=True).map({False:0,True:1})

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

#splitting the data 
x_train,x_val,y_train,y_val=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=0)

#countvectorization 
cv=CountVectorizer(max_features=5000)
temp1=cv.fit_transform(x_train['final_text']).toarray()
temp2=cv.transform(x_val['final_text']).toarray()
tf=TfidfTransformer()
temp1=tf.fit_transform(temp1)
temp2=tf.transform(temp2)
temp1=pd.DataFrame(temp1.toarray(),index=x_train.index)
temp2=pd.DataFrame(temp2.toarray(),index=x_val.index)
x_train=pd.concat([x_train,temp1],axis=1,sort=False)
x_val=pd.concat([x_val,temp2],axis=1,sort=False)

#drop final_text col
x_train.drop(['final_text'],axis=1,inplace=True)
x_val.drop(['final_text'],axis=1,inplace=True)

#converting to int datatype
y_train=y_train.astype(int)
y_val=y_val.astype(int)

#multinomial model
model=MultinomialNB()
model.fit(x_train,y_train)
y_preds=model.predict(x_val)
print("Multinomial Model: ",accuracy_score(y_val,y_preds))

#decisiontree model
model=DecisionTreeClassifier(random_state=0)
model.fit(x_train,y_train)
y_preds=model.predict(x_val)
print("Decision Tree: ",accuracy_score(y_val,y_preds))

#randomforstclassifier model
model=RandomForestClassifier(n_estimators=100,random_state=0)
model.fit(x_train,y_train)
y_preds=model.predict(x_val)
print("Random Forest: ",accuracy_score(y_val,y_preds))