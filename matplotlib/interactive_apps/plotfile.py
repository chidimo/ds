"""Code chp1/plotfile.py"""

from argparse import ArgumentParser
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = ArgumentParser(description="Plot a csv file")
    parser.add_argument("datafile", help="The CSV file")

    # require at least one column name
    
    parser.add_argument("columns", nargs="+", help="Names of columns to plot")
    parser.add_argument("--save", help="Save the plot as ...")
    parser.add_argument("--no-show", action="store_true", help="Don't show the plot")

    args = parser.parse_args()

    plt.plotfile(args.datafile, args.columns)
    if args.save:
        plt.savefig(args.save)
    if not args.no_show:
        plt.show()
