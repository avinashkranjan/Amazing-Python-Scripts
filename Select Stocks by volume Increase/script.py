import yfinance as yf
import pandas as pd

print("1) Dataset comparison of stocks")
print("2) Real time comparison of stocks")
ch = input("Enter choice: ")
if(ch==1):
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


else:
  import pandas as pd
  from alpha_vantage.timeseries import TimeSeries
  import time

  api_key = 'IJP88YSA0WASY3X0'
  stocks=input("Name of the stock: ")
  period=input("Interval for comparison with units: ")
  
  ts = TimeSeries(key=api_key, output_format='pandas')
  data, meta_data = ts.get_intraday(symbol=stocks, interval = period, outputsize = "full")
  print(data)

  i = 1


  close_data = data['4. close']
  percentage_change = close_data.pct_change()

  print(percentage_change)

  last_change = percentage_change[-1]

  if abs(last_change) > 0.0004:
     print("Stock Alert:" + str(last_change))

