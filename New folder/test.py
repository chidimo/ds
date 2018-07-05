import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from weather_patterns import read_and_sort, remove_leaps, min_max, daily_maximum, daily_minimum
# %matplotlib notebook

df = read_and_sort()

df = remove_leaps(df)

split_min_max = min_max(df)
highs_df = split_min_max[0]
lows_df = split_min_max[1]

high_0514 = daily_maximum(highs_df, 2005, 2015)
low_0514 = daily_minimum(lows_df, 2005, 2015)

max_15 = daily_maximum(highs_df, 2015, 2016)
min_15 = daily_minimum(lows_df, 2015, 2016)
