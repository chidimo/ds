"""Docstring"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#pylint: disable=C0103
#pylint: disable=E1101
#pylint: disable=R0913
#pylint: disable=W0621
#pylint: disable=W0614

def annotate_bar(ax, dff):
    """Annotate the plot"""

    means = dff.mean()
    conf_95 = dff.sem()*1.96

    bins = len(dff.columns)

    ax.bar(range(len(dff.columns)),
           means,
           yerr=conf_95,
           color='cyan',
           width=0.05,
           alpha=0.5,
           edgecolor='k',
           capsize=10)

    ax.set_xticks((range(bins)))
    ax.set_xticklabels(dff.columns)
    ax.set_title('Annotating the histogram')

    ax.annotate('95% Confidence',
                xy=(0, conf_95),
                xytext=(0, 0.5*conf_95),
                arrowprops=dict(arrowstyle='->'),
                verticalalignment='center',
                annotation_clip=False)
    ax.annotate('Mean',
                xy=(0, means),
                xytext=(0, 0.5*means),
                arrowprops=dict(arrowstyle='->'),
                verticalalignment='center',
                annotation_clip=False)
    ax.scatter(0, conf_95, color='r')
    plt.show()

if __name__ == "__main__":
    np.random.seed(12345)

    dff = pd.DataFrame([np.random.normal(32000, 200000, 3650)], index=[1992])
    dff = dff.transpose()
    dff.columns = [1992]

    fig, ax = plt.subplots()
    annotate_bar(ax, dff)
    