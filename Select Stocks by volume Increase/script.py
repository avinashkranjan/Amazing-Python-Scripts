import yfinance as yf
import pandas as pd

data = input("Enter file path: ")
df = pd.read_csv(data)

stocks = input("Enter column heading of stocks: ")
days = input("Enter number of days for comparision: ")
timesincrease = input("Enter number of times increase in volume required: ")
print(df[stocks])
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

