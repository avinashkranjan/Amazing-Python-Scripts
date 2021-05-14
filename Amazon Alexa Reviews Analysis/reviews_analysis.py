# Amazon Alexa Reviews Analysis

# The aim is to analyse Alexa's reviews by NLP. If the feedback is positive, the result is 1, else it is 0. Using logistic regression, I have tried to classify the feedback as positive or negative.

## MODELLING

# Importing Libraries

import pandas as pd
import nltk 
nltk.download('stopwords')                 # download the stopwords from NLTK

import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

from sklearn.linear_model import LogisticRegression  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import roc_auc_score

# Getting our Data

df = pd.read_csv('../Amazon Alexa Reviews Analysis/Dataset/amazon_alexa.csv')

# Data Preprocessing

df = df.drop(['rating', 'date', 'variation'], axis = 1)

df.isnull().any()  # checking for null values

# no null values were found

def process_rev(rev):
    """Process review function.
    Input:
        rev: a string containing a review
    Output:
        rev_clean: a list of words containing the processed review

    """
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
    # tokenize reviews
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    rev_tokens = tokenizer.tokenize(rev)

    rev_clean = []
    for word in rev_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # rev_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            rev_clean.append(stem_word)

    return rev_clean

# using the process_rev function for:
# 1. Removing stop words
# 2. Tokenization
# 3. Stemming
A = []
a = df['verified_reviews']
for i in a:
  i = process_rev(i)
  A.append(i)
df['verified_reviews'] = A

# Vectorizing

cv = CountVectorizer(max_features=1500, analyzer='word', lowercase=False) 

df['verified_reviews'] = df['verified_reviews'].apply(lambda x: " ".join(x) )  # to join all words in the lists
X = cv.fit_transform(df['verified_reviews'])  # predictor variable 'X'

y = pd.DataFrame(df['feedback'])  # respose variable 'y'

# Splitting for Training and Testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)  # splitting in the ratio 80:20

# Model

classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Making Predictions

y_pred = classifier.predict(X_test)

# Checking Accuracy

print('\nAccuracy:',roc_auc_score(y_test, y_pred))
print('\n')

# Predictions are 68.25% accurate.

# Getting the pkl File
import pickle
pickle.dump(classifier, open('../Amazon Alexa Reviews Analysis/Model/AmazonAlexaReviewsAnalysis.pkl', 'wb'))

## MAKING PREDICTIONS

# getting a review as input

a = input('Enter review: ')

# processing the review

b = process_rev(a)

b_new = ''
for i in b:
     b_new = b_new + ' ' + i

# vectorizing

X_final = cv.transform([b_new])  # predictor variable 'X_final'

# making predictions

feedback = classifier.predict(X_final)
if feedback == 0:
    print('\nFeedback is negative :(')
else:
    print('\nFeedback is positive :)')