# importing libraries

import pandas as pd
import plotly.express as px

# storing the dataset
book_relative_path = 'Purchases - Home B.xlsx'
book_prices = 'PriceBook.xlsx'

# reading the data
data_prices = pd.read_excel(book_prices)
data_home_1 = pd.read_excel(book_relative_path)

#print​(df_prices, df_home_1)

data_total = data_home_1.merge(data_prices, on='ID')

data_total['Total Price'] = data_total['PURCHASED AMOUNT'] * data_total['Price']

#print​(df_total)

fig = px.pie(data_total[['MATERIAL', 'Total Price']], values='Total Price', names='MATERIAL')
fig.show()

