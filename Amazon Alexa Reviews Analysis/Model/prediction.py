import pandas as pd
import Amazon_Alexa_Reviews_Analysis as A

# loading our model

import joblib
classifier = joblib.load(r'C:\Users\DELL\Desktop\Kaggle+HE\Github GSSoC21\Amazing Python Scripts\Amazon Alexa Reviews Analysis\Model\AmazonAlexaReviewsAnalysis.pkl')

# getting a review as input

a = input('Enter review: ')
df1 = pd.read_csv(r'C:\Users\DELL\Desktop\Kaggle+HE\Github GSSoC21\Amazing Python Scripts\Amazon Alexa Reviews Analysis\Dataset\amazon_alexa.csv')

l = []
for i in df1['verified_reviews']:
    l.append(i)
    
b = None    
for j in range(0,len(l)):
    if l[j] == a:
        b = classifier.predict(A.X_train[j])

if b == 0:         
    print('\nFeedback is negative :(')
    
else:
    print('\nFeedback is positive :)')    