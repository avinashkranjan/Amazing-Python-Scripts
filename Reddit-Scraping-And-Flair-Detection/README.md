# Reddit Flair Detector
## Steps followed:

Described each step along with code in the notebooks. 

### Step 1: Extraction of r/india data 
Used praw library of python for extraction.

### Step 2: Exploratory Data Analysis
Analysed the data using graphs and scattered points as well as correlation. Used matplotlib library for the same.

### Step 3: Made Reddit Flair Detector. Performed the following the steps:
- Preprocessed the data: Removed stopwords and performed stemming on the data
- Diving into training and test: Divided the dataset into training and   test set. Used standard, 0.7:0.3 metric
- Testing accross classifiers: Tested along 3 classifiers: Naive Bayees, SVM   and Logisitic Regression. Checked accuracy of each of the classifiers.
- Saving the model: Saved the model with highest accuracy in a .sav file to   use it for prediction. 
- Model testing: Take input URL from the user and return the predicted and    actual flairs. Call the saved model for predicted flairs

### How it works:
The model reads all the urls in the file line by line and predict the flair
- The same is stored in json file.

### Output:

It will be a key and predicted flair as value.

    
