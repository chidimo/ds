
# coding: utf-8

# get_ipython().magic('matplotlib notebook')
import numpy as np
import matplotlib.pyplot as plt
# use gridspec to partition the figure into subplots
import matplotlib.gridspec as gridspec

# pyplot.figure().add_axes()

fig = plt.figure(figsize=(4, 4), facecolor='grey')
# fig = plt.figure(figsize=plt.figaspect(2.0)) # height = 2 * width

ax1 = fig.add_axes([0, 0.5, 1, 0.5])
ax2 = fig.add_axes([0, 0, 1, 0.5])

ax1.plot([2, 4, 8, 16, 32])
ax1.plot([1, 2, 3, 4, 5, 6, 7])
ax2.plot([1, 3, 9, 27, 81])

ax1.set_title('green')
ax2.set_title('blue')


for each in ax1.get_children() + ax2.get_children():
    print(each)

fig, axes = plt.subplots(3, 3)

axes[1,2].plot([1, 2, 3, 4])

fig.tight_layout()


# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(False)

plt.figure()
gspec = gridspec.GridSpec(3, 3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

plt.figure()
ax = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

x = np.linspace(0, 2, 1000)
y = np.sin(2 * np.pi * (x - 0.01 * 2))
line.set_data(x, y)

np.random.uniform(0,1,(50,2))

