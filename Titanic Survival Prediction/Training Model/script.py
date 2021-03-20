#import the  libraries
import numpy as np
import pandas as pd
import pickle
import random as rd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA

# Print options
np.set_printoptions(precision=4, threshold=10000, linewidth=160, edgeitems=999, suppress=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 160)
pd.set_option('expand_frame_repr', False)
pd.set_option('precision', 4)


def processCabin():

    # Replace missing values with "U0"
    df['Cabin'][df.Cabin.isnull()] = 'U0'

    # create feature for the alphabetical part of the cabin number
    df['CabinLetter'] = df['Cabin'].map( lambda x : getCabinLetter(x))
    df['CabinLetter'] = pd.factorize(df['CabinLetter'])[0]

    # create binary features for each cabin letters
    if keep_binary:
        cletters = pd.get_dummies(df['CabinLetter']).rename(columns=lambda x: 'CabinLetter_' + str(x))
        df = pd.concat([df, cletters], axis=1)

    # create feature for the numerical part of the cabin number
    df['CabinNumber'] = df['Cabin'].map( lambda x : getCabinNumber(x)).astype(int) + 1
    # scale the number to process as a continuous feature
    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['CabinNumber_scaled'] = scaler.fit_transform(df['CabinNumber'])


def getCabinLetter(cabin):
    """
    Find the letter component of the Cabin variable
    """
    match = re.compile("([a-zA-Z]+)").search(cabin)
    if match:
        return match.group()
    else:
        return 'U'


def getCabinNumber(cabin):
    """
    Find the number component of the Cabin variable
    """
    match = re.compile("([0-9]+)").search(cabin)
    if match:
        return match.group()
    else:
        return 0


def processTicket():
    """
    Generate features from the Ticket variable
    """
    global df

    df['TicketPrefix'] = df['Ticket'].map( lambda x : getTicketPrefix(x.upper()))
    df['TicketPrefix'] = df['TicketPrefix'].map( lambda x: re.sub('[\.?\/?]', '', x) )
    df['TicketPrefix'] = df['TicketPrefix'].map( lambda x: re.sub('STON', 'SOTON', x) )
    #print len(df['TicketPrefix'].unique()), "ticket codes:", np.sort(df['TicketPrefix'].unique())

    df['TicketPrefixId'] = pd.factorize(df['TicketPrefix'])[0]

    # create binary features for each cabin letters
    if keep_binary:
        prefixes = pd.get_dummies(df['TicketPrefix']).rename(columns=lambda x: 'TicketPrefix_' + str(x))
        df = pd.concat([df, prefixes], axis=1)

    df.drop(['TicketPrefix'], axis=1, inplace=True)

    df['TicketNumber'] = df['Ticket'].map( lambda x: getTicketNumber(x) )
    df['TicketNumberDigits'] = df['TicketNumber'].map( lambda x: len(x) ).astype(np.int)
    df['TicketNumberStart'] = df['TicketNumber'].map( lambda x: x[0:1] ).astype(np.int)
    #print np.sort(df.TicketNumberStart.unique())

    df['TicketNumber'] = df.TicketNumber.astype(np.int)
    #print np.sort(df['TicketNumber'])

    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['TicketNumber_scaled'] = scaler.fit_transform(df['TicketNumber'])


def getTicketPrefix(ticket):
    """
    Find the letter component of the ticket variable)
    """
    match = re.compile("([a-zA-Z\.\/]+)").search(ticket)
    if match:
        return match.group()
    else:
        return 'U'

### Find the numerical component of the ticket variable)
def getTicketNumber(ticket):
    match = re.compile("([\d]+$)").search(ticket)
    if match:
        return match.group()
    else:
        return '0'


### Generate features from the ticket price
def processFare():
    global df

    # replace missing values as the median fare. Currently the datasets only contain one missing Fare value
    df['Fare'][ np.isnan(df['Fare']) ] = df['Fare'].median()

    # zero values cause problems with our division interaction variables so set to 1/10th of the lowest fare
    df['Fare'][ np.where(df['Fare']==0)[0] ] = df['Fare'][ df['Fare'].nonzero()[0] ].min() / 10

    # bin into quintiles for binary features
    df['Fare_bin'] = pd.qcut(df['Fare'], 4)
    if keep_binary:
        df = pd.concat([df, pd.get_dummies(df['Fare_bin']).rename(columns=lambda x: 'Fare_' + str(x))], axis=1)

    if keep_bins:
        df['Fare_bin_id'] = pd.factorize(df['Fare_bin'])[0]+1

    # center and scale the fare to use as a continuous variable
    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Fare_scaled'] = scaler.fit_transform(df['Fare'])

    if keep_bins and keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Fare_bin_id_scaled'] = scaler.fit_transform(df['Fare_bin_id'])


    if not keep_strings:
        df.drop('Fare_bin', axis=1, inplace=True)


### Build binary features from 3-valued categorical feature
def processEmbarked():
    global df

    # Replace missing values with most common port, and create binary features
    df.Embarked[ df.Embarked.isnull() ] = df.Embarked.dropna().mode().values

    # Lets turn this into a number so it conforms to decision tree feature requirements
    df['Embarked'] = pd.factorize(df['Embarked'])[0]

    # Create binary features for each port
    if keep_binary:
        df = pd.concat([df, pd.get_dummies(df['Embarked']).rename(columns=lambda x: 'Embarked_' + str(x))], axis=1)


### Generate features based on the passenger class
def processPClass():
    global df

    # Replace missing values with mode
    df.Pclass[ df.Pclass.isnull() ] = df.Pclass.dropna().mode().values

    # create binary features
    if keep_binary:
        df = pd.concat([df, pd.get_dummies(df['Pclass']).rename(columns=lambda x: 'Pclass_' + str(x))], axis=1)

    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Pclass_scaled'] = scaler.fit_transform(df['Pclass'])


### Generate features from the SibSp and Parch variables
def processFamily():
    global df

    # interaction variables require no zeros, so let's just bump everything
    df['SibSp'] = df['SibSp'] + 1
    df['Parch'] = df['Parch'] + 1

    # First process scaling
    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['SibSp_scaled'] = scaler.fit_transform(df['SibSp'])
        df['Parch_scaled'] = scaler.fit_transform(df['Parch'])

    # Then build binary features
    if keep_binary:
        sibsps = pd.get_dummies(df['SibSp']).rename(columns=lambda x: 'SibSp_' + str(x))
        parchs = pd.get_dummies(df['Parch']).rename(columns=lambda x: 'Parch_' + str(x))
        df = pd.concat([df, sibsps, parchs], axis=1)


### Convert the Sex variable from a string to binary
def processSex():
    global df
    df['Gender'] = np.where(df['Sex'] == 'male', 1, 0)


### Generate features from the Name variable
def processName():
    global df
    # how many different names do they have?
    df['Names'] = df['Name'].map(lambda x: len(re.split(' ', x)))

    # what is each person's title?
    df['Title'] = df['Name'].map(lambda x: re.compile(", (.*?)\.").findall(x)[0])

    # group low-occuring, related titles together
    df['Title'][df.Title == 'Jonkheer'] = 'Master'
    df['Title'][df.Title.isin(['Ms','Mlle'])] = 'Miss'
    df['Title'][df.Title == 'Mme'] = 'Mrs'
    df['Title'][df.Title.isin(['Capt', 'Don', 'Major', 'Col', 'Sir'])] = 'Sir'
    df['Title'][df.Title.isin(['Dona', 'Lady', 'the Countess'])] = 'Lady'

    # Build binary features
    if keep_binary:
        df = pd.concat([df, pd.get_dummies(df['Title']).rename(columns=lambda x: 'Title_' + str(x))], axis=1)

    # process scaling
    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Names_scaled'] = scaler.fit_transform(df['Names'])

    if keep_bins:
        df['Title_id'] = pd.factorize(df['Title'])[0]+1

    if keep_bins and keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Title_id_scaled'] = scaler.fit_transform(df['Title_id'])


### Generate features from the Age variable
def processAge():
    global df
    setMissingAges()

    # center the mean and scale to unit variance
    if keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Age_scaled'] = scaler.fit_transform(df['Age'])

    # have a feature for children
    df['isChild'] = np.where(df.Age < 13, 1, 0)

    # bin into quartiles and create binary features
    df['Age_bin'] = pd.qcut(df['Age'], 4)
    if keep_binary:
        df = pd.concat([df, pd.get_dummies(df['Age_bin']).rename(columns=lambda x: 'Age_' + str(x))], axis=1)

    if keep_bins:
        df['Age_bin_id'] = pd.factorize(df['Age_bin'])[0]+1

    if keep_bins and keep_scaled:
        scaler = preprocessing.StandardScaler()
        df['Age_bin_id_scaled'] = scaler.fit_transform(df['Age_bin_id'])

    if not keep_strings:
        df.drop('Age_bin', axis=1, inplace=True)


### Populate missing ages using a RandomForestClassifier
def setMissingAges():
    global df

    age_df = df[['Age','Embarked','Fare', 'Parch', 'SibSp', 'Title_id','Pclass','Names','CabinLetter']]
    X = age_df.loc[ (df.Age.notnull()) ].values[:, 1::]
    y = age_df.loc[ (df.Age.notnull()) ].values[:, 0]

    rtr = RandomForestRegressor(n_estimators=2000, n_jobs=-1)
    rtr.fit(X, y)

    predictedAges = rtr.predict(age_df.loc[ (df.Age.isnull()) ].values[:, 1::])
    df.loc[ (df.Age.isnull()), 'Age' ] = predictedAges


### Keep the raw list until the very end even if raw values are not retained so that interaction
### parameters can be created
def processDrops():
    global df
    rawDropList = ['Name', 'Names', 'Title', 'Sex', 'SibSp', 'Parch', 'Pclass', 'Embarked', \
                   'Cabin', 'CabinLetter', 'CabinNumber', 'Age', 'Fare', 'Ticket', 'TicketNumber']
    stringsDropList = ['Title', 'Name', 'Cabin', 'Ticket', 'Sex', 'Ticket', 'TicketNumber']
    if not keep_raw:
        df.drop(rawDropList, axis=1, inplace=True)
    elif not keep_strings:
        df.drop(stringsDropList, axis=1, inplace=True)


def getDataSets(binary=False, bins=False, scaled=False, strings=False, raw=True, pca=False, balanced=False):
    """
    Performs all feature engineering tasks including populating missing values, generating binary categorical
    features, scaling, and other transformations. The boolean parameters of this function will allow fine-grained
    control of what types of features to return, so that it can be used by multiple ML algorithms

    Parameters
    ==========
    binary - boolean
        whether or not to include binary features in the data set

    bins - boolean
        whether or not to include binned features in the data set

    scaled - boolean
        whether or not to include scaled features in the data set

    strings - boolean
        whether or not to include features that are strings in the data set

    raw - boolean
        whether or not to include raw features in the data set

    pca - boolean
        whether or not to perform PCA on the data set

    balanced - boolean
        whether or not to perform up sampling on the survived examples to balance the class distributions

    Returns
    =======
    input_df - array-like
        The labeled training data

    submit_df - array-like
        The unlabled test data to predict and submit

    """
    global keep_binary, keep_bins, keep_scaled, keep_raw, keep_strings, df
    keep_binary = binary
    keep_bins = bins
    keep_scaled = scaled
    keep_raw = raw
    keep_strings = strings

    # read in the training and testing data into Pandas.DataFrame objects
    input_df = pd.read_csv('data/raw/train.csv', header=0)
    submit_df  = pd.read_csv('data/raw/test.csv',  header=0)

    # merge the two DataFrames into one
    df = pd.concat([input_df, submit_df])

    # re-number the combined data set so there aren't duplicate indexes
    df.reset_index(inplace=True)

    # reset_index() generates a new column that we don't want, so let's get rid of it
    df.drop('index', axis=1, inplace=True)

    # the remaining columns need to be reindexed so we can access the first column at '0' instead of '1'
    df = df.reindex_axis(input_df.columns, axis=1)

    # process the individual variables present in the raw data
    processCabin()
    processTicket()
    processName()
    processFare()
    processEmbarked()
    processFamily()
    processSex()
    processPClass()
    processAge()
    processDrops()

    # Move the survived column back to the first position
    columns_list = list(df.columns.values)
    columns_list.remove('Survived')
    new_col_list = list(['Survived'])
    new_col_list.extend(columns_list)
    df = df.reindex(columns=new_col_list)

    print "Starting with", df.columns.size, "manually generated features...\n", df.columns.values

    #*********************************************************************************************************
    # Automated feature generation based on basic math on scaled features
    numerics = df.loc[:, ['Age_scaled', 'Fare_scaled', 'Pclass_scaled', 'Parch_scaled', 'SibSp_scaled',
                          'Names_scaled', 'CabinNumber_scaled', 'Age_bin_id_scaled', 'Fare_bin_id_scaled']]
    print "\nFeatures used for automated feature generation:\n", numerics.head(10)

    new_fields_count = 0
    for i in range(0, numerics.columns.size-1):
        for j in range(0, numerics.columns.size-1):
            if i <= j:
                name = str(numerics.columns.values[i]) + "*" + str(numerics.columns.values[j])
                df = pd.concat([df, pd.Series(numerics.iloc[:,i] * numerics.iloc[:,j], name=name)], axis=1)
                new_fields_count += 1
            if i < j:
                name = str(numerics.columns.values[i]) + "+" + str(numerics.columns.values[j])
                df = pd.concat([df, pd.Series(numerics.iloc[:,i] + numerics.iloc[:,j], name=name)], axis=1)
                new_fields_count += 1
            if not i == j:
                name = str(numerics.columns.values[i]) + "/" + str(numerics.columns.values[j])
                df = pd.concat([df, pd.Series(numerics.iloc[:,i] / numerics.iloc[:,j], name=name)], axis=1)
                name = str(numerics.columns.values[i]) + "-" + str(numerics.columns.values[j])
                df = pd.concat([df, pd.Series(numerics.iloc[:,i] - numerics.iloc[:,j], name=name)], axis=1)
                new_fields_count += 2

    print "\n", new_fields_count, "new features generated"


    #*********************************************************************************************************
    # Use Spearman correlation to remove highly correlated features

    # calculate the correlation matrix
    df_corr = df.drop(['Survived', 'PassengerId'],axis=1).corr(method='spearman')

    # create a mask to ignore self-
    mask = np.ones(df_corr.columns.size) - np.eye(df_corr.columns.size)
    df_corr = mask * df_corr

    drops = []
    # loop through each variable
    for col in df_corr.columns.values:
        # if we've already determined to drop the current variable, continue
        if np.in1d([col],drops):
            continue

        # find all the variables that are highly correlated with the current variable
        # and add them to the drop list
        corr = df_corr[abs(df_corr[col]) > 0.98].index
        #print col, "highly correlated with:", corr
        drops = np.union1d(drops, corr)

    print "\nDropping", drops.shape[0], "highly correlated features...\n" #, drops
    df.drop(drops, axis=1, inplace=True)


    #*********************************************************************************************************
    # Split the data sets apart again, perform PCA/clustering/class balancing if necessary
    #
    input_df = df[:input_df.shape[0]]
    submit_df  = df[input_df.shape[0]:]

    if pca:
        print "reducing and clustering now..."
        input_df, submit_df = reduceAndCluster(input_df, submit_df)
    else:
        # drop the empty 'Survived' column for the test set that was created during set concatentation
        submit_df.drop('Survived', axis=1, inplace=1)

    print "\n", input_df.columns.size, "initial features generated...\n" #, input_df.columns.values

    if balanced:
        # Undersample training examples of passengers who did not survive
        print 'Perished data shape:', input_df[input_df.Survived==0].shape
        print 'Survived data shape:', input_df[input_df.Survived==1].shape
        perished_sample = rd.sample(input_df[input_df.Survived==0].index, input_df[input_df.Survived==1].shape[0])
        input_df = pd.concat([input_df.ix[perished_sample], input_df[input_df.Survived==1]])
        input_df.sort(inplace=True)
        print 'New even class training shape:', input_df.shape

    return input_df, submit_df


def reduceAndCluster(input_df, submit_df, clusters=3):
    """
    Takes the train and test data frames and performs dimensionality reduction with PCA and clustering

    This was part of some experimentation and wasn't used for top scoring submissions. Leaving it in for reference
    """

    # join the full data together
    df = pd.concat([input_df, submit_df])
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    df = df.reindex_axis(input_df.columns, axis=1)

    # Series of labels
    survivedSeries = pd.Series(df['Survived'], name='Survived')

    print df.head()

    # Split into feature and label arrays
    X = df.values[:, 1::]
    y = df.values[:, 0]

    print X[0:5]


    # Minimum percentage of variance we want to be described by the resulting transformed components
    variance_pct = .99

    # Create PCA object
    pca = PCA(n_components=variance_pct)

    # Transform the initial features
    X_transformed = pca.fit_transform(X,y)

    # Create a data frame from the PCA'd data
    pcaDataFrame = pd.DataFrame(X_transformed)

    print pcaDataFrame.shape[1], " components describe ", str(variance_pct)[1:], "% of the variance"



    # use basic clustering to group similar examples and save the cluster ID for each example in train and test
    kmeans = KMeans(n_clusters=clusters, random_state=np.random.RandomState(4), init='random')

    #==============================================================================================================
    # # Perform clustering on labeled AND unlabeled data
    # clusterIds = kmeans.fit_predict(X_pca)
    #==============================================================================================================

    # Perform clustering on labeled data and then predict clusters for unlabeled data
    trainClusterIds = kmeans.fit_predict(X_transformed[:input_df.shape[0]])
    print "clusterIds shape for training data: ", trainClusterIds.shape
    #print "trainClusterIds: ", trainClusterIds

    testClusterIds = kmeans.predict(X_transformed[input_df.shape[0]:])
    print "clusterIds shape for test data: ", testClusterIds.shape
    #print "testClusterIds: ", testClusterIds

    clusterIds = np.concatenate([trainClusterIds, testClusterIds])
    print "all clusterIds shape: ", clusterIds.shape
    #print "clusterIds: ", clusterIds


    # construct the new DataFrame comprised of "Survived", "ClusterID", and the PCA features
    clusterIdSeries = pd.Series(clusterIds, name='ClusterId')
    df = pd.concat([survivedSeries, clusterIdSeries, pcaDataFrame], axis=1)

    # split into separate input and test sets again
    input_df = df[:input_df.shape[0]]
    submit_df = df[input_df.shape[0]:]
    submit_df.reset_index(inplace=True)
    submit_df.drop('index', axis=1, inplace=True)
    submit_df.drop('Survived', axis=1, inplace=1)

    return input_df, submit_df


if __name__ == '__main__':

    train, test = getDataSets(bins=True, scaled=True, binary=True)
    drop_list = ['PassengerId']
    train.drop(drop_list, axis=1, inplace=1)
    test.drop(drop_list, axis=1, inplace=1)

    train, test = reduceAndCluster(train, test)

    print "Labeled survived counts :\n", pd.value_counts(train['Survived'])/train.shape[0]
    print "Labeled cluster counts  :\n", pd.value_counts(train['ClusterId'])/train.shape[0]
    print "Unlabeled cluster counts:\n", pd.value_counts(test['ClusterId'])/test.shape[0]

    print train.columns.values
