Figures, subplots, axes, layout
====================================

`Axes <http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes>`_

`tom on SO <https://stackoverflow.com/questions/36040605/matplotlibs-figure-and-axes-explanation>`_

`fig.add_axes() <http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.add_axes`>_

`fig.add_subplot() <http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.add_subplot>`_

`gridSpec() and subplot2grid()` <http://matplotlib.org/users/gridspec.html#gridspec-and-subplotspec?>`_

`pyplot.subplots <http://matplotlib.org/api/pyplot_api.html?highlight=pyplot%20subplots#matplotlib.pyplot.subplots>`_


1. **Figure** - the main window or top-level container housing the axes/subplots. So each call to **figure()** creates a new window.

2. **Axes/subplots** - both are the same thing. A window/container housing graphed/plotted data points and the associated ticks etc.

3. **Layout** - arrangement of axes/subplots in a figure

4. **Figure coordinates** - 

5. **Axes/Subplot coordinates** - 

6. A call to **subplot** creates an axes instance and places it on a *regular* grid

7. **fig.add_axes([left, bottom, width, height])** creates an axes instance and adds it to the figure. The specified dimensions are in figure coordinates (fractions of figure width and height). fig is variable name for plt.figure()

    a. **left** - left vertical boundary line of fig. 0 means start at this line; 0.5 means start halfway across from this line;
        
    b. **bottom** - lower horizontal boundary line of fig. 0 means start at this line; 0.5 means start halfway up from this line
        
    c. **width** - fractional values. 0 means nothing will show up; 0.5 means half total fig width; 1 means span the entire width of the figure.
        
    d. **height** - fractional values: 0 means nothing will show up. 0.5 means half total fig height; 1 means span the entire height of the figure.
        

8. **fig.add_subplot(row,col,plot_no.)** also creates an axes instance. This creates a *regular* rectangular grid with specified number of rows and columns and adds the axes to the position whose number is specified by **plot_no**

9. A call to **pyplot.subplots()** returns a reference to the figure and an array of axes