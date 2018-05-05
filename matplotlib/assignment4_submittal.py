"""Coursera: python for datascience, matplotlib - Assignment 4 solution
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, YearLocator

def gdp_inflation_data(file_name, sheet):
    """Read gdp and inflation data"""
    data = pd.read_excel('assignment_data/{}.xlsx'.format(file_name), sheetname=sheet)
    data.set_index('year', inplace=True)
    if 'inflation_rate' in list(data):
        data.inflation_rate = data.inflation_rate*100
    data = data.iloc[::-1] # place dates in ascending order
    data.index = pd.to_datetime(data.index, format='%Y')
    return data

def plot_data():
    """Plot the figure"""

    ng_gdp = gdp_inflation_data('data_gdp', 'NG')
    ng_inflation = gdp_inflation_data('data_inflation', 'NG')
    uae_gdp = gdp_inflation_data('data_gdp', 'UAE')
    uae_inflation = gdp_inflation_data('data_inflation', 'UAE')

    fig = plt.figure(facecolor='lightblue', figsize=(12, 8))
    ax_gdp = plt.subplot(2, 1, 1)
    ax_inf = plt.subplot(2, 1, 2, sharex=ax_gdp)
    years = YearLocator()
    yrfmt = DateFormatter("%Y")

    ax_inf.plot_date(ng_inflation.index, ng_inflation.inflation_rate, 'g-o', label='Nigeria')
    ax_inf.plot_date(uae_inflation.index, uae_inflation.inflation_rate, 'r-o', label='UAE')
    ax_gdp.plot_date(ng_gdp.index, ng_gdp.GDP_bn_dol, 'g-o', label='Nigeria')
    ax_gdp.plot_date(uae_gdp.index, uae_gdp.GDP_bn_dol, 'r-o', label='UAE')

    ax_gdp.xaxis.set_major_locator(years)
    ax_gdp.xaxis.set_major_formatter(yrfmt)
    ax_gdp.set(ylabel="GDP (billions of $)")
    ax_gdp.autoscale_view()
    ax_gdp.legend(loc="upper left")

    ax_inf.xaxis.set_major_locator(years)
    ax_inf.xaxis.set_major_formatter(yrfmt)
    ax_inf.set(ylabel="Inflation rate (in %)")
    ax_inf.autoscale_view()
    ax_inf.legend(loc="lower left")
    title = "Variation of GDP and inflation rate of Nigeria and UAE between 2005 and 2016"
    fig.suptitle(title, fontsize=16)

    fig.autofmt_xdate()

    plt.savefig("comparing_gdp_inflation.png", facecolor=fig.get_facecolor(), dpi=100)
    plt.savefig("comparing_gdp_inflation.pdf", facecolor=fig.get_facecolor(), dpi=100)
    plt.show()

if __name__ == "__main__":
    plot_data()
