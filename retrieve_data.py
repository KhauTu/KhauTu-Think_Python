import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import yfinance as yf
import matplotlib.pyplot as plt

goog = yf.download('GOOG', data_source='google', start='2009-3-14', end='2014-4-14')
# print(goog.head())
# f = pd.DataFrame(goog)
# print(f.Open)

goog['Log_Ret'] = np.log(goog['Close']/goog['Close'].shift(1))
goog['Volatility'] = goog['Log_Ret'].rolling(252).std() * np.sqrt(252)
f = pd.DataFrame(goog)
# print(f.Volatility.tail())

# %matplotlib inline
# goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8, 6))

# plt.show()
print(goog['Close'].head())
print(goog['Close'].shift(1).head())