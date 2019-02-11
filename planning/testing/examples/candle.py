"""
Show how to make date plots in matplotlib using date tick locators and
formatters.  See major_minor_demo1.py for more information on
controlling major and minor ticks

All matplotlib date plotting is done by converting date instances into
days since the 0001-01-01 UTC.  The conversion, tick locating and
formatting is done behind the scenes so this is most transparent to
you.  The dates module provides several converter functions date2num
and num2date

This example requires an active internet connection since it uses
yahoo finance to get the data for plotting
"""

import matplotlib.pyplot as plt
import pandas as pd
import quandl
from matplotlib.dates import DateFormatter, MonthLocator, YearLocator

years = YearLocator()  # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

quotes = data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")

dates = quotes.index
Value = quotes['Value']

fig, ax = plt.subplots()
ax.plot_date(dates, Value, '-')

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()


# format the coords message box
def price(x):
    return '$%1.2f' % x


ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.show()
