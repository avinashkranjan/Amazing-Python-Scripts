# import the  libraries
import pandas as pd
import pickle

# Function to let user choose from various options


def let_user_pick(options, str):
    print(f"Enter the {str}")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1, element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return options[int(i)-1]
    except:
        pass
    return None

# Function to convert yes or no to boolean


def know_language(yes_no):
    if yes_no.lower() == 'y' or yes_no.lower() == 'yes' or yes_no == '1':
        return 1
    else:
        return 0


# Make an empty dataframe df
data = [['0', '0', '0', '0', '0', '0', '0', '0']]
df = pd.DataFrame(data, columns=[
                  'Sector', 'python_yn', 'job_sim', 'R_yn', 'tableau', 'power bi', 'ml', 'dl'])

# Take Sector as an input from user
sectors = ['Information Technology', 'Business Services', 'Education',
           'Business Services', 'Finance', 'Government', 'Travel & Tourism']
sect = let_user_pick(sectors, 'Sector')
df['Sector'][0] = sect

# Take job role as an input from user
job_role = ['Software Enginner', 'data scientist', 'data engineer',
            'analyst', 'Machine Learnig Engineer', 'director', 'manager']
job_simp = let_user_pick(job_role, 'Job Role')
if job_simp == 'Software Engineer':
    job_simp = 'na'
elif job_simp == 'Machine Learnig Engineer':
    job_simp = 'mle'
df['job_sim'][0] = job_simp

# Asking  for skills from user
python = know_language(input('Do you know python?(Y/N)'))
df['python_yn'][0] = python

r = know_language(input('Do you know R?(Y/N)'))
df['R_yn'][0] = r

tableau = know_language(input('Do you know Tableau?(Y/N)'))
df['tableau'][0] = tableau

Power_Bi = know_language(input('Do you know Power Bi?(Y/N)'))
df['power bi'][0] = Power_Bi

Machine_Learning = know_language(input('Do you know Machine Learning?(Y/N)'))
df['ml'][0] = Machine_Learning

Deep_Learning = know_language(input('Do you know Deep Learning?(Y/N)'))
df['dl'][0] = Deep_Learning

# Load the model
with open('./Salary Predictor/models/random_forest2_model.sav', 'rb') as f:
    random_forest_model = pickle.load(f)

# load the columns file
with open('./Salary Predictor/models/model_columns1.pkl', 'rb') as f:
    model_columns = pickle.load(f)

# Query into the model to fet results
query_ = pd.get_dummies(pd.DataFrame(df, index=[0]), prefix=[
                        'Sector', 'job_sim'], columns=['Sector', 'job_sim'])
query = query_.reindex(columns=model_columns, fill_value=0)
prediction = list(random_forest_model.predict(query))
final_val = round(prediction[0], 2)

print(f'Your Estimated Annual Salary will be {final_val}K Dollars')
