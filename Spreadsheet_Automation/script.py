# importing libraries

import pandas as pd
import plotly.express as px

# storing the dataset
data1 = input("Enter first dataset")
data2 = input("Enter second dataset")

# reading the data
data_read_1 = pd.read_excel(data1)
data_read_2 = pd.read_excel(data2)

# print​(df_prices, df_home_1)

reference = input("What is the basis of merging? ")
data_total = data_read_2.merge(data_read_1, on=reference)


# print​(df_total)
criteria_1 = input("Enter criteria 1")
criteria_2 = input("Enter criteria 2")
fig = px.pie(data_total[[criteria_1, criteria_2]],
             values=criteria_2, names=criteria_1)
fig.show()
