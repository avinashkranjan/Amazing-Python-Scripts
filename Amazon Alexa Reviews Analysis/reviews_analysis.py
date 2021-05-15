# Amazon Alexa Reviews Analysis

# The aim is to analyse Alexa's reviews by NLP. If the feedback is positive, the result is 1, else it is 0. Using logistic regression, I have tried to classify the feedback as positive or negative.

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

def process_rev(rev):
    """
        Process review function.
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

# applying process_rev function to all reviews 

processed_reviews = []
all_reviews = df['verified_reviews']
for i in all_reviews:
  i = process_rev(i)
  processed_reviews.append(i)
df['verified_reviews'] = processed_reviews

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

# getting a review as input

user_review = input('Enter review: ')

# processing the review

processed_user_review = process_rev(user_review)

cleaned_review = ''
for i in processed_user_review:
     cleaned_review = cleaned_review + ' ' + i

# vectorizing

X_final = cv.transform([cleaned_review])  # predictor variable 'X_final'

# making predictions

feedback = classifier.predict(X_final)
if feedback == 0:
    print('\nFeedback is negative :(')
else:
    print('\nFeedback is positive :)')