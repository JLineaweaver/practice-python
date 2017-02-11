import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

df_google = web.DataReader('GOOGL', 'yahoo', start, end)
df_apple = web.DataReader('AAPL', 'yahoo', start, end)
df_amazon = web.DataReader('AMZN', 'yahoo', start, end)
df_microsoft = web.DataReader('MSFT', 'yahoo', start, end)

df_google.plot()
df_apple.plot()
df_amazon.plot()
df_microsoft.plot()
plt.show()
