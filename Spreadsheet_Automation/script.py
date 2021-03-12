# importing libraries

import pandas as pd
import plotly.express as px

# storing the dataset
book_relative_path = input("Enter first dataset")
book_prices = input("Enter second dataset")

# reading the data
data_prices = pd.read_excel(book_prices)
data_home_1 = pd.read_excel(book_relative_path)

#print​(df_prices, df_home_1)

item = input("What is the basis of merging? ")
data_total = data_home_1.merge(data_prices, on=item)

data_total['Total Price'] = data_total['PURCHASED AMOUNT'] * data_total['Price']

#print​(df_total)
material=input("Enter criteria 1")
price=input("Enter criteria 2")
fig = px.pie(data_total[[material, price]], values=price, names=material)
fig.show()

