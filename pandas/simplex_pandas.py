"""Doctstring"""

from fractions import Fraction
import numpy as np
import pandas as pd

def read_file(file_name):
    """Docstring
    Notes
    ------   
    Line 1. Number of variables
    Line 2. Number of equations
    Line 3 to 3+number of equations-1: equation coefficients with constant term
    Last line: "normalized" objective function
    """
    with open(file_name, "r") as file_hand:
        data = file_hand.readlines()
        no_of_variables = int(data[0].strip())
        no_of_equations = int(data[1].strip())
        coefficients = data[2:-1]
        objective_func = data[-1]

        diagonal = np.zeros((no_of_equations, no_of_equations))
        i, j = np.indices(diagonal.shape)
        diagonal[i == j] = 1
        headings = ['x{}'.format(i+1) for i in range(no_of_equations + no_of_variables)]
        headings.append('z')

        coefficient_list = []

        for idx, dat in enumerate(coefficients):
            terms = dat.split()
            coeff = [int(x.strip()) for x in terms[:-1]]
            coeff.extend(list(diagonal[idx]))
            coeff.append(terms[-1])
            coefficient_list.append(coeff)

        obj = [int(x.strip()) for x in objective_func.split()]

        obj.extend([0 for x in range(no_of_equations)])
        coefficient_list.append(obj)
        return headings, coefficient_list

def create_tableau(data):
    """Docstring"""
    headings = data[0]
    coeffs = data[1]

    values_dict = {headings[idx] : [each[idx] for each in coeffs]
                   for idx, dat in enumerate(headings)}

    dff = pd.DataFrame(values_dict)
    dff['z'] = pd.to_numeric(dff['z'], errors='coerce')
    return dff

def series_to_fraction(series):
    """Transform values of series to fraction"""
    series = series.apply(str) # convert to string object
    for each in series.index:
        series[each] = Fraction(series[each])
    return series

def simplify(dff):
    """Perform single step operation on a tableau based
    on a single indicator

    Parameter
    ----------
    Tableau : DataFrame
    
    Notes
    ------
    Steps for stage 2: row transformations
    perform row operations to transform all entries in 
    pivot column to zero
    each non-pivot row operation is performed as follows
    get a multiplier for that row which is given by
    (-1) * row coefficient in pivot column
    get a new row as follows: multiply pivot row by the multiplier
    adding the new row to the row to be transformed
    """
    pivot_column = dff.iloc[-1].idxmin()
    div_series = dff['z']/dff[pivot_column]

    # select min from non-zero and non-negative values
    pivot_row = div_series[div_series > 0].idxmin()

    pivot_value = dff.loc[pivot_row, pivot_column]

    # normalize pivot
    dff.iloc[pivot_row] /= pivot_value

    # stage 2: row transformations
    for each in dff.index:
        if each == pivot_row:
            continue
        else:
            multiplier = (-1) * (dff.loc[each, pivot_column])
            new_row_from_pivot = dff.iloc[pivot_row] * multiplier
            dff.iloc[each] += new_row_from_pivot
    return dff

def simplex(tableau):
    """Perform tableau operations till indicator
    row has no negative number
    
    Parameters
    ------------
    tableau : DataFrame
    """
    # test for negative number in last row
    indicator = (tableau.iloc[-1] < 0).any()

    while indicator:
        tableau = simplify(tableau)
        print(tableau.apply(series_to_fraction))
        print()
        indicator = (tableau.iloc[-1] < 0).any()

def maximize():
    """Main"""
    data = read_file("simplex.txt")
    dff = create_tableau(data)
    simplex(dff)

if __name__ == "__main__":
    maximize()
