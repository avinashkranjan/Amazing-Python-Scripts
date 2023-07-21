# importing necessary libraries
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


def perform_grid_search(X, y):
    # Define the parameter grid for each algorithm
    rf_param_grid = {
        'n_estimators': [100, 200, 500],
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5, 10]
    }

    svm_param_grid = {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf', 'poly']
    }

    logr_param_grid = {
        'C': [0.1, 1, 10],
        'penalty': ['l1', 'l2']
    }

    dt_param_grid = {
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5, 10]
    }

    nb_param_grid = {
        'var_smoothing': [1e-9, 1e-8, 1e-7]
    }

    knn_param_grid = {
        'n_neighbors': [3, 5, 7],
        'weights': ['uniform', 'distance']
    }

    # Create the GridSearchCV objects for each algorithm
    rf_grid_search = GridSearchCV(
        RandomForestClassifier(), rf_param_grid, cv=5)
    svm_grid_search = GridSearchCV(SVC(), svm_param_grid, cv=5)
    dt_grid_search = GridSearchCV(DecisionTreeRegressor(), dt_param_grid, cv=5)
    nb_grid_search = GridSearchCV(GaussianNB(), nb_param_grid, cv=5)
    knn_grid_search = GridSearchCV(
        KNeighborsClassifier(), knn_param_grid, cv=5)
    logr_grid_search = GridSearchCV(
        LogisticRegression(), logr_param_grid, cv=5)

    # Fit the models and perform grid search
    rf_grid_search.fit(X, y)
    svm_grid_search.fit(X, y)
    dt_grid_search.fit(X, y)
    nb_grid_search.fit(X, y)
    knn_grid_search.fit(X, y)
    logr_grid_search.fit(X, y)

    # Store the results in a dictionary
    results = {
        'Random Forest': {'Best Parameters': rf_grid_search.best_params_, 'Best Score': rf_grid_search.best_score_},
        'SVM': {'Best Parameters': svm_grid_search.best_params_, 'Best Score': svm_grid_search.best_score_},
        'Decision Tree': {'Best Parameters': dt_grid_search.best_params_, 'Best Score': dt_grid_search.best_score_},
        'Naive Bayes': {'Best Parameters': nb_grid_search.best_params_, 'Best Score': nb_grid_search.best_score_},
        'K-Nearest Neighbors': {'Best Parameters': knn_grid_search.best_params_, 'Best Score': knn_grid_search.best_score_},
        'Logistic Regression': {'Best Parameters': logr_grid_search.best_params_, 'Best Score': logr_grid_search.best_score_}
    }

    return results


# Define your data and target variables here
X = ...
y = ...

# Perform grid search
grid_search_results = perform_grid_search(X, y)

# Print the results
for algorithm, result in grid_search_results.items():
    print(algorithm)
    print("Best Parameters: ", result['Best Parameters'])
    print("Best Score: ", result['Best Score'])
    print("")
