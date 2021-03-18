import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor


url = "https://gist.githubusercontent.com/jerry-shad/36912907ba8660e11cd27be0d3e30639/raw/424f0891dc46d96cd5f867f3d2697777ac984f68/pollution.csv"
df = pd.read_csv(url,parse_dates=['date'])
df.drop(columns=['Unnamed: 0'],axis=1,inplace=True)

# sort the dataframe by date and reset the index 
df = df.sort_values(by='date').reset_index(drop=True)
# after sorting the dataframe, split the dataframe
split_date ='2017-12-01'
df_training = df.loc[(df.date <= split_date).values]
df_test = df.loc[(df.date > split_date).values]
# drop the date column 
df_training.drop(columns=['date'],axis=1,inplace=True)
df_test.drop(columns=['date'],axis=1,inplace=True)

y_train = df_training['pollution_index']
y_test = df_test['pollution_index']
df_training.drop(['pollution_index'],axis=1)
df_test.drop(['pollution_index'],axis=1)

scaler = StandardScaler() 
scaler.fit(df_training)
X_train = scaler.transform(df_training)  
X_test = scaler.transform(df_test)

X_train_df = pd.DataFrame(X_train,columns=df_training.columns)
X_test_df = pd.DataFrame(X_test,columns=df_test.columns)