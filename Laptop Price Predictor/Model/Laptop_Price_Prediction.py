# LAPTOP PRICE PREDICTION

# Importing Libraries

import pandas as pd
from sklearn import preprocessing
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Getting our Data

df = pd.read_csv(r'./Laptop Price Predictor/Dataset/laptoppricing.csv', encoding = 'unicode_escape')

# Data Preprocessing

df.rename(columns={'ï»¿Manufacturer':'Manufacturer'}, inplace=True)

label_encoder = preprocessing.LabelEncoder()
df['Manufacturer'] = df['Manufacturer'].astype('|S')
df['Manufacturer'] = label_encoder.fit_transform(df['Manufacturer'])

# checking vif
variables = df[['Manufacturer', 'IntelCore(i-)', 'IntelCoreGen',
       'processing speed(GHz)', 'Ram(gb)', 'HDD(gb)', 'SSD(gb)',
       'Graphics(gb)', 'ScreenSize(inch)']]
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif['Features'] = variables.columns

print('Variance inflation factor is:\n',vif)

# now, we'll drop columns which have vif>10
df = df.drop(['IntelCore(i-)','IntelCoreGen','processing speed(GHz)','HDD(gb)','ScreenSize(inch)'], axis=1)

# Splitting Data for Training and Testing

data = df.values
X,y = data[:,:-1], data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)  # splitting in the ration 80:20

# Model

regr = RandomForestRegressor(random_state=0)
regr.fit(X, y)

# Making Predictions and Checking Accuracy

y_pred = regr.predict(X_test)

print('\nAccuracy (r2_score):',r2_score(y_test, y_pred))

# Getting the pkl file

import pickle
pickle.dump(regr, open('./Laptop Price Predictor/Model/LaptopPricePrediction.pkl', 'wb'))