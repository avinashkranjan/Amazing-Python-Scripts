import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import joblib

dataframe = pd.read_csv("spam.csv")
print(dataframe.describe())

x = dataframe["EmailText"]
y = dataframe["Label"]

x_train, y_train = x[0:4457], y[0:4457]
x_test, y_test = x[4457:], y[4457:]

cv = CountVectorizer()
features = cv.fit_transform(x_train)

tuned_parameters = {
    'kernel': ['rbf', 'linear'],
    'gamma': [1e-3, 1e-4],
    'C': [1, 10, 100, 1000]
}

model = GridSearchCV(svm.SVC(), tuned_parameters)

model.fit(features, y_train)

print(model.best_params_)

print(model.score(cv.transform(x_test), y_test))

joblib.dump(model.best_estimator_, 'filename.pkl', compress=1)

print(x)

print(y)

y.count()

y.unique()

dataframe['Label'].value_counts()

dataframe['Label'].value_counts().plot(kind='bar')

loaded_model = joblib.load('filename.pkl')
a = input('Enter the text:- ')
result = model.predict(cv.transform([a]))
print(result[0])
