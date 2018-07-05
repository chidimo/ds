# %matplotlib notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def assignment_data():
    """Return distribution dataframe"""
    np.random.seed(12345)

    df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                       np.random.normal(43000, 100000, 3650),
                       np.random.normal(43500, 140000, 3650),
                       np.random.normal(48000, 70000, 3650)],
                      index=[1992, 1993, 1994, 1995])
    df = df.transpose()
    df.columns = [1992, 1993, 1994, 1995]
    return df

def normalize_y(y_value, mean):
    """
    Normalize the chosen y value
    
    Notes
    ------
    The last 'if' block makes sure we don't go lower than midpoint in our colorations.
    Removing it means we could potentially return to 100% dark color within the bar.
    """
    if y_value > mean:
        return 0
    if y_value/mean < 0.5:
        return 0.5
    return y_value/mean

greys = ['grey']*4
darks = ['#25383C', '#2B547E', '#3B9C9C', '#800517']
brights = ['#00FFFF', '#FFFF00', '#FFD801', '#F433FF']
violets = ['#A74AC7', '#6C2DC7', '#B93B8F', '#7D1B7E']

color_scheme = [greys, darks, brights, violets]
cm_scheme = [plt.cm.bone, plt.cm.cool, plt.cm.Accent, plt.cm.jet, plt.cm.inferno, plt.cm.YlOrRd, plt.cm.BuPu, plt.cm.viridis]

# %%file week3_solution.py

def interactive_bar(ax, ax2, distribution_data, y_value, color_map):
    """Change bar colors according to clicked y value

    Parameters
    ----------
    ax : Axes
        The axes with which to plot the data
    ax2 : Axes
        Axes on which to put colormap
    distribution_data : DataFrame
        Dataframe of distribution
    y_value : int
        Value of y
    color_map :
        Matplotlib colormap

    Notes
    -------
    100% dark purple shade indicate that the chosen y value is above the bar.
    The other shades show how close we are to the mean WITHIN the bar
        
    means : Series
        Mean of each column in the dataframe
    std_dev : Series
        Standard deviation of each column in the dataframe
    min_value : float
        Minimum value in the population
    """
    means = distribution_data.mean()
    conf_95 = distribution_data.sem()*1.96
    max_value = distribution_data.values.max()
    min_value = distribution_data.values.min()

    bins = len(distribution_data.columns)
    normalize = mpl.colors.Normalize(vmin=0, vmax=1)
    colors = [color_map(x) for x in np.linspace(0, 1, bins)]

    for key, col_name in enumerate(distribution_data.columns):
        bar_mean = means[col_name]
        bar_err = conf_95[col_name]
        normed_y = normalize_y(y_value, bar_mean)
        bar_color = color_map(normed_y)

        ax.bar(key, bar_mean, align='center', width=1.0, yerr=bar_err, alpha=1, color=bar_color,
               edgecolor='k', capsize=10, label='%s: p = %2.2f'%(col_name, bar_mean))

    ax.set_ylabel('Mean values (95% confidence intervals on top)')
    ax.legend(loc='best')
    ax.axhline(y=y_value, color='#3D3C3A', zorder=20)
    ax.set_xticks((range(len(distribution_data.columns))))
    ax.set_xticklabels(distribution_data.columns, position=(-700, 0))
    ax.set_title('Bar colors at y = %.0f'%(y_value))

    ax2.set_yticks([])
    color_bar = mpl.colorbar.ColorbarBase(ax2, cmap=color_map, norm=normalize, orientation='horizontal')
    color_bar.set_ticks(np.linspace(0, 1, bins+1))
    color_bar.set_ticklabels(['0%', '25%', '50%', '75%', '100%'])
    plt.show()

def onclick(event):
    """Change bar colors"""
    ax.cla()
    ax2.cla()
    interactive_bar(ax, ax2, distribution_data, event.ydata, cm_scheme[5])

def color_dance(event):
    """Switch colormaps"""
    ax.cla()
    ax2.cla()
    key = int(event.ydata)%4
    print("KK", key)
    interactive_bar(ax, ax2, distribution_data, event.ydata, cm_scheme[key])
    
def activate():
    """Switch colors with a single colormap"""
    distribution_data = assignment_data()
    cm_viridis = plt.cm.viridis

    fig = plt.figure(figsize=(8, 6), facecolor='lightblue')
    ax = fig.add_axes([0.15, 0.15, 0.6, 0.80], frame_on=True)
    ax2 = fig.add_axes([0.4, 0.05, 0.4, 0.025], frame_on=True)
    interactive_bar(ax, ax2, distribution_data, 40000, cm_scheme[0])
    plt.gcf().canvas.mpl_connect('button_press_event', color_dance)
    
if __name__ == "__main__":
    activate()