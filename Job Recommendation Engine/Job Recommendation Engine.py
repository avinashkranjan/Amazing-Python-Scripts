#!/usr/bin/env python
# coding: utf-8

# **Import Libraries**

# In[1]:


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize


# ## Data preprocessing

# In[2]:


data = pd.read_csv('naukri_com-jobs__20190701_20190830__30k_data.csv')


# In[3]:


data.head()


# In[4]:


user_profiles = data[['Uniq Id', 'Role Category',
                      'Location', 'Job Experience Required', 'Key Skills']]
job_postings = data[['Uniq Id', 'Role Category',
                     'Location', 'Job Experience Required', 'Key Skills']]


# ### User Profile

# In[5]:


user_profiles = user_profiles.groupby('Uniq Id').agg(lambda x: ' '.join(x))
user_profiles.reset_index(inplace=True)


# ### Similarity measurement (Cosine)

# In[6]:


user_profiles_matrix = pd.get_dummies(user_profiles.drop('Uniq Id', axis=1))
user_profiles_matrix = normalize(user_profiles_matrix)  # Normalize the matrix
similarity_matrix = cosine_similarity(
    user_profiles_matrix, user_profiles_matrix)


# ### Job recommendation

# In[7]:


# Define the number of nearest neighbors to consider
k = 5


def get_job_recommendations(user_id):
    user_index = user_profiles[user_profiles['Uniq Id'] == user_id].index[0]
    similar_users = similarity_matrix[user_index].argsort(
    )[::-1][1:k+1]  # Exclude the user itself

    # Get job postings from similar users
    recommended_roles = []
    for user in similar_users:
        similar_user_id = user_profiles.iloc[user]['Uniq Id']
        similar_user_roles = data[data['Uniq Id'] ==
                                  similar_user_id]['Role Category'].values
        recommended_roles.extend(similar_user_roles)

    # Filter out already interacted job roles
    user_interacted_roles = data[data['Uniq Id']
                                 == user_id]['Role Category'].values
    recommended_roles = list(set(recommended_roles) -
                             set(user_interacted_roles))

    # Rank recommended roles based on frequency
    recommended_roles = pd.Series(
        recommended_roles).value_counts().sort_values(ascending=False)

    return recommended_roles.index.tolist()


# Example usage
user_id = '9be62c49a0b7ebe982a4af1edaa7bc5f'
recommended_roles = get_job_recommendations(user_id)
print(f"Recommended job roles for user {user_id}:")
for role in recommended_roles:
    print(role)


# In[ ]:


# In[ ]:
