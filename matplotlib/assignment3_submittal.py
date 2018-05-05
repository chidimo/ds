"""Coursera python for datascience, matplotlib
Assignment 3 solution
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from assignment3_data import dff, cm_scheme, normalize_y

#pylint: disable=C0103
#pylint: disable=E1101
#pylint: disable=R0913
#pylint: disable=W0621
#pylint: disable=W0614

def interactive_chameleon(ax, ax2, dff, y_value, color_map):
    """Change bar colors according to clicked y value

    Parameters
    ----------
    ax : Axes
        The axes with which to plot the data
    ax2 : Axes
        Axes on which to put colormap
    dff : DataFrame
        Dataframe of distribution
    means : Series
        Mean of each column in the dataframe
    std_dev : Series
        Standard deviation of each column in the dataframe
    min_value : float
        Minimum value contained in the population
    color_map :
        Matplotlib colormap

    Notes
    -------
    100% dark purple shade indicate that the chosen y value is above the bar.
    The other shades show how close we are to the mean WITHIN the bar
    """
    means = dff.mean()
    conf_95 = dff.sem()*1.96
    max_value = dff.values.max()
    min_value = dff.values.min()

    bins = len(dff.columns)
    normalize = mpl.colors.Normalize(vmin=0, vmax=1)
    # colors = [color_map(x) for x in np.linspace(0, 1, bins)]

    for key, col_name in enumerate(dff.columns):
        bar_mean = means[col_name]
        bar_err = conf_95[col_name]
        normed_y = normalize_y(y_value, bar_mean)
        bar_color = color_map(normed_y)

        ax.bar(key,
               bar_mean,
               align='center',
               width=1.0,
               yerr=bar_err,
               alpha=1,
               color=bar_color,
               edgecolor='k',
               capsize=10,
               label='%s: p = %2.2f'%(col_name, bar_mean))

    ax.set_ylabel('Mean values (95% confidence intervals on top)')
#     ax.legend(loc='best')
    ax.axhline(y=y_value, color='#3D3C3A', zorder=20)
    ax.set_xticks((range(len(dff.columns))))
    ax.set_xticklabels(dff.columns, position=(-700, 0))
    ax.set_title('Bar colors at y = %.0f'%(y_value))

    ax2.set_yticks([])
    color_bar = mpl.colorbar.ColorbarBase(ax2, cmap=color_map,
                                          norm=normalize,
                                          orientation='horizontal')
    color_bar.set_ticks(np.linspace(0, 1, bins+1))
    color_bar.set_ticklabels(['0%', '25%', '50%', '75%', '100%'])
    plt.show()

def chameleon(event):
    """Change color of chameleon"""
    ax.cla()
    ax2.cla()
    interactive_chameleon(ax, ax2, dff, event.ydata, cm_scheme[5])

def interactive_draw_line():
    """Place y value line"""
    min_value = dff.values.min()
    y_value = int(input('Enter a value of y between {} and {} '
                        .format(np.abs(min_value), np.abs(min_value))))
    ax.axhline(y=y_value, color='#3D3C3A', zorder=20)

def color_dance(event):
    """Switch colormaps"""
    ax.cla()
    ax2.cla()
    key = int(event.ydata)%4
    interactive_chameleon(ax, ax2, dff, event.ydata, cm_scheme[key])

if __name__ == "__main__":
    """Switch colors with a single colormap"""
    cm_viridis = plt.cm.viridis

    fig = plt.figure(figsize=(8, 6), facecolor='lightblue')
    ax = fig.add_axes([0.15, 0.15, 0.6, 0.80], frame_on=True)
    ax2 = fig.add_axes([0.4, 0.05, 0.4, 0.025], frame_on=True)
    interactive_chameleon(ax, ax2, dff, 40000, cm_scheme[5])
    plt.gcf().canvas.mpl_connect('button_press_event', chameleon)
    