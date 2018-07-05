# Datascience

## Custom ipython kernel

<https://ipython.readthedocs.io/en/stable/install/kernel_install.html>

1. `pipenv install jupyter`
1. `pipenv install tornado`
1. `pipenv install ipykernel`
1. `python -m ipykernel install --user --name [env name] --display-name [optional]`

## Resources

### Numpy

1. <https://docs.scipy.org/doc/numpy-dev/user/quickstart.html>
1. <https://docs.scipy.org/doc/numpy-dev/reference/index.html#reference>
1. <http://www.scipy-lectures.org/>
1. <http://www.python-course.eu/numpy.php/>
1. <https://github.com/scipy-lectures/scipy-lecture-notes>
1. <http://mathesaurus.sourceforge.net/>
1. <https://docs.scipy.org/doc/scipy/reference/tutorial/index.html>
1. <http://matplotlib.org/api/animation_api.html>

### Pandas

1. http://pandas.pydata.org/
1. https://www.youtube.com/watch?v=9d5-Ti6onew>
1. <https://www.youtube.com/watch?v=5JnMutdy6Fw>
1. <https://www.youtube.com/watch?v=rIofV14c0tc>
1. <https://www.youtube.com/watch?v=GkU-VzL-3Vk>
1. <https://www.youtube.com/watch?v=suX147xwWg4>
1. <https://youtu.be/k7X7sZzSXYs>
1. <http://nosebotpress.blogspot.ae/2017/01/scared-straight-educational-ponderables.html#more>
1. <https://www.quora.com/What-is-the-best-freelance-website-for-beginners-and-why>
1. <https://www.youtube.com/watch?v=Sn-beSK3rv4>
1. <https://www.youtube.com/watch?v=29ji7iEwq_I>

### Matplotlib

#### Anatomy of a plot (figures, subplots, axes, layout)

1. <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes>
1. <https://stackoverflow.com/questions/36040605/matplotlibs-figure-and-axes-explanation>
1. fig.add_axes() <http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.add_axes>
1. fig.add_subplot() <http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.add_subplot>
1. gridSpec() and subplot2grid()` <http://matplotlib.org/users/gridspec.html#gridspec-and-subplotspec?>
1. pyplot.subplots <http://matplotlib.org/api/pyplot_api.html?highlight=pyplot%20subplots#matplotlib.pyplot.subplots>

1. **Figure:** the main window or top-level container housing the axes/subplots. So each call to *figure()* creates a new window.
1. **Axes/subplots:** both are the same thing. A window/container housing graphed/plotted data points and the associated ticks etc.
1. **Layout:** arrangement of axes/subplots in a figure
1. **Figure coordinates:**
1. **Axes/Subplot coordinates:**
1. **subplot()"** call creates an axes instance and places it on a *regular* grid
1. **fig.add_axes([left, bottom, width, height])** creates an axes instance and adds it to the figure. The specified dimensions are in figure coordinates (fractions of figure width and height). fig is variable name for `plt.figure()`

    a. **left** - left vertical boundary line of fig. 0 means start at this line; 0.5 means start halfway across from this line;
    b. **bottom** - lower horizontal boundary line of fig. 0 means start at this line; 0.5 means start halfway up from this line
    c. **width** - fractional values. 0 means nothing will show up; 0.5 means half total fig width; 1 means span the entire width of the figure.
    d. **height** - fractional values: 0 means nothing will show up. 0.5 means half total fig height; 1 means span the entire height of the figure.

1. **fig.add_subplot(row,col,plot_no.)** also creates an axes instance. This creates a *regular* rectangular grid with specified number of rows and columns and adds the axes to the position whose number is specified by **plot_no**

1. A call to **pyplot.subplots()** returns a reference to the figure and an array of axes
