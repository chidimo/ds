"""Docstring"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pylint: disable=C0103
#pylint: disable=E1101

def distribution_data():
    """Return distribution dataframe"""
    np.random.seed(12345)

    df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                       np.random.normal(43000, 100000, 3650),
                       np.random.normal(43500, 140000, 3650),
                       np.random.normal(48000, 70000, 3650)],
                      index=[1992, 1993, 1994, 1995])
    df2 = df.transpose()
    df2.columns = [1992, 1993, 1994, 1995]
    df2 = df2
    return df2

def normalize_y(y_value, mean):
    """Normalize the chosen y value"""
    if y_value > mean:
        return 0
    # this if block makes sure we don't go lower than midpoint
    # in our colorations. Removing it means we could potentially
    # return to 100% dark purple within the bar.
    if y_value/mean < 0.5:
        return 0.5
    return y_value/mean

greys = ['grey']*4
darks = ['#25383C', '#2B547E', '#3B9C9C', '#800517']
brights = ['#00FFFF', '#FFFF00', '#FFD801', '#F433FF']
violets = ['#A74AC7', '#6C2DC7', '#B93B8F', '#7D1B7E']
greens = ['', '', '', '']

cm_bone = plt.cm.bone
cm_cool = plt.cm.cool
cm_accent = plt.cm.Accent
cm_jet = plt.cm.jet
cm_inferno = plt.cm.inferno
cm_yor = plt.cm.YlOrRd
cm_bupu = plt.cm.BuPu
cm_viridis = plt.cm.viridis

cm_scheme = [cm_bone, cm_cool, cm_accent, cm_jet, cm_yor, cm_bupu, cm_viridis]
color_scheme = [greys, darks, brights, violets]

dff = distribution_data()

if __name__ == "__main__":
    distribution_data()
