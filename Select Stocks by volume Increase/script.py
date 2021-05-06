import yfinance as yf
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import os

print("1) Dataset comparison of stocks")
print("2) Real time comparison of stocks")
ch = int(input("Enter choice: "))
if(ch == 1):
    data = input("Enter file path: ")
    df = pd.read_csv(data)

    stocks = input("Enter column heading of stocks: ")
    days = input("Enter number of days for comparision: ")
    timesincrease = input(
        "Enter number of times increase in volume required: ")

    increased_stocks = []

    for stock in df[stocks]:
        stock = stock.upper()
        if '^' in stock:
            pass
        else:
            try:
                stock_info = yf.Ticker(stock)

                hist = stock_info.history(period=days)
                previous_averaged_volume = hist['Volume'].iloc[1:days-1:1].mean()
                todays_volume = hist['Volume'][-1]

                if todays_volume > previous_averaged_volume * timesincrease:
                    increased_stocks.append(stock)
            except:
                pass

    print(increased_stocks)


elif(ch == 2):

    api_key = os.environ['api_key']
    stocks = input("Name of the stock: ")

    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(
        symbol=stocks, interval='5min', outputsize="full")

    close_data = data['4. close']
    percentage_change = close_data.pct_change()

    print("Percentage Change: " + str(percentage_change))

    last_change = percentage_change[-1]

    if abs(last_change) > 0.0004:
        print("Stock Alert:" + str(last_change))

else:
    print("Invalid choice")
