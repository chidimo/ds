"""Coursera python for datascience, matplotlib
Assignment 2 solution
"""

# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=W0621

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

def read_and_clean():
    """Read data and set index"""
    dff = pd.read_csv('assignment_data/weather_patterns.csv', index_col='Date')
    dff.Data_Value = dff.Data_Value/10

    # convert index to datetime
    dff.index = pd.to_datetime(dff.index)
    # remove leap days by masking

    to_drop = np.array([((each.day == 29) & (each.month == 2))  for each in dff.index])
    dff = dff[~to_drop]
    dff.sort_index(inplace=True)
    del dff['ID']
    return dff

def min_max(dff):
    """Separate the min and max readings"""
    maxxes = dff.loc[dff.Element == 'TMAX']
    minnies = dff.loc[dff.Element == 'TMIN']
    del maxxes['Element']
    del minnies['Element']
    return maxxes, minnies

def daily_maximums(dff, yrstart, yrend):
    """Single maximum value for each day"""
    dff = dff[(dff.index.year >= yrstart) & (dff.index.year < yrend)]
    new = pd.DataFrame(columns=['Value'])

    for idx, mdf in dff.groupby(by=dff.index.month): # pull common months

        for idxx, days in mdf.groupby(by=mdf.index.day): # pull common days

            maxi = days.Data_Value.max()
            index = days[days.Data_Value == maxi].index[0] # take only one index
            new.loc[index] = maxi
    return new

def daily_minimums(dff, yrstart, yrend):
    """Single maximum value for each day"""
    dff = dff[(dff.index.year >= yrstart) & (dff.index.year < yrend)]
    new = pd.DataFrame(columns=['Value'])

    for idx, mdf in dff.groupby(by=dff.index.month):

        for idxx, days in mdf.groupby(by=mdf.index.day):

            maxi = days.Data_Value.min()
            index = days[days.Data_Value == maxi].index[0]
            new.loc[index] = maxi
    return new

def dataframes_for_plot():
    """All dataframes needed for the plot"""
    dff = read_and_clean()
    min_max_parts = min_max(dff) # split dataframe into MIN and MAX

    highs_0514 = daily_maximums(min_max_parts[0], 2005, 2014)
    lows_0514 = daily_minimums(min_max_parts[1], 2005, 2014)

    highs_15 = daily_maximums(min_max_parts[0], 2015, 2016)
    lows_15 = daily_minimums(min_max_parts[1], 2015, 2016)

    # reindex to match with 2015 index
    highs_0514.set_index(highs_15.index, inplace=True) 
    lows_0514.set_index(highs_15.index, inplace=True)

    # compute record highs and lows
    record_highs = highs_15[highs_15.Value > highs_0514.Value]
    record_lows = lows_15[lows_15.Value < lows_0514.Value]

    return highs_0514, lows_0514, record_highs, record_lows

def plot_temperatures(highs_0514, lows_0514, record_highs, record_lows):
    """Plot the temperature values"""
    fig = plt.figure(facecolor='lightblue', figsize=(10, 8))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
    monthsFmt = DateFormatter("%b")


    ax.plot_date(highs_0514.index, highs_0514.Value,
                 'b-', label="2004-2015 highs")
    ax.plot_date(lows_0514.index, lows_0514.Value,
                 'c-', label="2004-2015 lows")
    ax.fill_between(highs_0514.index, highs_0514.Value,
                    lows_0514.Value, facecolor='lightblue')

    ax.plot_date(record_highs.index, record_highs.Value,
                 mec="#F88017", mfc="k", label="2015 Highs")
    ax.plot_date(record_lows.index, record_lows.Value,
                 mec="#2D6580", mfc="#7F462C", label="2015 Lows")

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)

    ax.set(xlabel="Individual days of the year",
           ylabel=r"Temperature values in $^{o} C$")

    ax.autoscale_view()
    fig.autofmt_xdate()

    ax.grid(True)

    ax.legend(loc="upper left")

    title = r"""Temperature highs and lows for every calendar day of the year
    in Abu Dhabi, UAE, for the ten-year period 2005 to 2014 
    (Record-breaking highs and lows for 2015 overlayed in points)"""

    ax.set_title(title)
    plt.savefig('output/Temperature_Abu_Dhabi.pdf', facecolor=fig.get_facecolor(), dpi=100)
    plt.savefig('output/Temperature_Abu_Dhabi.png', facecolor=fig.get_facecolor(), dpi=100)

    plt.show()

if __name__ == "__main__":
    highs_0514, lows_0514, record_highs, record_lows = dataframes_for_plot()
    plot_temperatures(highs_0514, lows_0514, record_highs, record_lows)
