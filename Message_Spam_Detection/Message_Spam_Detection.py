#importing required libraries
import pandas as pd
import string 
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")

#reading the dataset 
msg=pd.read_csv("Cleaned_Dataset.csv",encoding='latin-1')
msg.drop(['Unnamed: 0'],axis=1,inplace=True)

#seperating target and features
y=pd.DataFrame(msg.label)
x=msg.drop(['label'],axis=1)

#countvectorization 
cv=CountVectorizer(max_features=5000)
temp1=cv.fit_transform(x['final_text'].values.astype('U')).toarray()
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
