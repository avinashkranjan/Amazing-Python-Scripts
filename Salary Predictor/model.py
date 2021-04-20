# import libraries
import pickle
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('./Salary Predictor/dataset/cleaned_dataset.csv')

df_model = df[['avg_salary', 'Sector', 'python_yn',
               'job_sim', 'R_yn', 'tableau', 'power bi', 'ml', 'dl']]

# Categorical encoding
df_dum = pd.get_dummies(df_model)

# division into training and test set
X = df_dum.drop('avg_salary', axis=1)
y = df_dum.avg_salary.values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Model Generation
regressor = RandomForestRegressor()


np.mean(cross_val_score(regressor, X_train, y_train,
        scoring='neg_mean_absolute_error', cv=5))

# Hyperparameter tuning
parameters = {
    "n_estimators": range(10, 400, 10),
    "criterion": ['mse', 'mae'],
    "max_features": ['auto', 'sqrt', 'log2']
}

gs = GridSearchCV(regressor, param_grid=parameters,
                  scoring='neg_mean_absolute_error', cv=5)
gs.fit(X_train, y_train)

gs.best_score_
y_pred = gs.best_estimator_.predict(X_test)

# Accuracy measurement
mean_absolute_error(y_test, y_pred)

# Save the model
filename = './Salary Predictor/models/random_forest2_model.sav'
pickle.dump(gs.best_estimator_, open(filename, 'wb'))

# saving the columns
model_columns = list(X.columns)
with open('./Salary Predictor/models/model_columns1.pkl', 'wb') as file:
    pickle.dump(model_columns, file)
