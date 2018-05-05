"""Sine and Cosine curves"""


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6), dpi=100)
plt.subplot(111)

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
sin, cos = np.sin(x), np.cos(x)

plt.plot(x, sin, color="green", linewidth=1.0, linestyle="-", label="sine")
plt.plot(x, cos, color="blue", linewidth=1.0, linestyle="-", label="cosine")

# plt.xlabel("Sine and Cosine functions")
# plt.ylabel("Values of x")

# plt.xlim(-4.0, 4.0)
# plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

plt.xlim(1.1*x.min(), 1.1*x.max())
plt.xticks([-np.pi, -np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$-\pi/4$', r'$0$', r'$+\pi/4$', r'$+\pi/2$', r'$+\pi$'])

# plt.ylim(-1.0, 1.0)
# plt.yticks(np.linspace(-1, 1, 10, endpoint=True))

plt.ylim(1.1*cos.min(), 1.1*cos.max())
plt.yticks([-1, 1], [r'$-1$', r'$+1$'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

point = 2*np.pi/3
plt.plot([point, point], [0, np.cos(point)], color="red", linewidth=1.5, linestyle="--")
plt.scatter([point, ], [np.cos(point), ], 50, color="black")
plt.annotate(r"$\sin(\frac{2\pi}{3}) = \frac{\sqrt{3}}{2}$",
             xy=(point, np.sin(point)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))


plt.plot([point, point], [0, np.sin(point)], color="red", linewidth=1.5, linestyle="--")
plt.scatter([point, ], [np.sin(point), ], 50, color="black")
plt.annotate(r'$\cos(\frac{2\pi}{3}) = \frac{1}{2}$',
             xy=(point, np.cos(point)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    print(label)
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

plt.legend(loc='upper left', frameon=False)
plt.savefig("sin_cosine.pdf", dpi=100)

plt.show()
