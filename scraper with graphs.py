import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

ticker = 'BTC-USD'
period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 0, 1).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 8, 1, 0, 1).timetuple()))
interval = '1d'

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df)

# x-values, the dates
dates = df[['Date']]
dates = dates.values.tolist()
dates = ['January 1st', 'February 1st', 'March 1st', 'April 1st', 'May 1st', 'June 1st', 'July 1st']

# y-values, the prices
close = df[['Close']]
close = close.values.tolist()

# both values in one frame
data = df[['Date', 'Close']]

# the plot
ticks = list(range(0,213))

ax = data.plot()
# ax.set_xticklabels(dates)
ax.xaxis.set_major_locator(plt.MaxNLocator(7))
ax.yaxis.set_major_locator(plt.MaxNLocator(7))

plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.xlabel('2021 in Days')
plt.ylabel(f'Daily Closing Prices of {ticker}')

plt.show()

#### candlestick chart graph  ######

ohlc = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

# Creating Subplots
fig, ax = plt.subplots()

candle = candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Daily Candlestick Chart of BTC')

# Formatting Date
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)

plt.show()
