import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated historical price data (more data points)
data = {
    'Date': pd.date_range(start='2010-01-01', periods=1000),
    'Open': np.random.uniform(100, 200, 1000),
    'High': np.random.uniform(200, 250, 1000),
    'Low': np.random.uniform(80, 150, 1000),
    'Close': np.random.uniform(120, 180, 1000),
    'Volume': np.random.randint(10000, 50000, 1000)
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Example trading strategy


def simple_moving_average_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0.0

    signals['Short_MA'] = data['Close'].rolling(
        window=short_window, min_periods=1, center=False).mean()
    signals['Long_MA'] = data['Close'].rolling(
        window=long_window, min_periods=1, center=False).mean()

    signals['Signal'][short_window:] = np.where(
        signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1.0, 0.0)

    signals['Positions'] = signals['Signal'].diff()

    return signals


# Define strategy parameters
short_window = 10
long_window = 50

# Apply strategy
signals = simple_moving_average_strategy(df, short_window, long_window)

# Risk management parameters
risk_per_trade = 0.02  # 2% risk per trade
initial_portfolio_value = 100000

# Simulate trading
position = 0
portfolio_value = []
for index, row in signals.iterrows():
    if row['Positions'] == 1:
        max_position_size = (
            risk_per_trade * initial_portfolio_value) / (row['Close'] - row['Low'])
        position = min(max_position_size,
                       initial_portfolio_value / row['Close'])
        initial_portfolio_value -= position * row['Close']
    elif row['Positions'] == -1:
        initial_portfolio_value += position * row['Close']
        position = 0
    portfolio_value.append(initial_portfolio_value + position * row['Close'])

signals['PortfolioValue'] = portfolio_value

# Visualization improvements
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(signals.index, signals['Close'], label='Close Price', alpha=0.5)
plt.plot(signals.index, signals['Short_MA'], label=f'Short {short_window} MA')
plt.plot(signals.index, signals['Long_MA'], label=f'Long {long_window} MA')
plt.legend()
plt.title('Price Data and Moving Averages')

plt.subplot(2, 1, 2)
plt.plot(signals.index, signals['PortfolioValue'],
         label='Portfolio Value', linestyle='--', color='green')
plt.legend()
plt.title('Portfolio Value')

plt.tight_layout()
plt.show()
