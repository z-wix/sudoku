'''
The purpose of this script is a module that I 
can just load into each of my scripts that will
custom functions and different levels of input
sudokus ranging in difficulty.
'''

import pandas as pd
import plotly.express as px

# Test using a Matrix
sudoku_matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],

    [0, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 0, 6, 7],

    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 0, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]


print(sudoku_matrix)

# Test using a dataset
sudoku_df = pd.DataFrame(
    sudoku_matrix,
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
)

sudoku_df.to_csv("../input/simple_sudoku.csv")


# Functions

def find_missing(lst):
    return [x for x in range(1,10) if x not in lst]

def add_char(char, incr = 1):
    int = ord(char[0])
    next_char = chr(int + incr)
    return next_char

def find_sector_columns(current_column):
    # possible column sectors
    columns1 = ['A', 'B', 'C']
    columns2 = ['D', 'E', 'F']
    columns3 = ['G', 'H', 'I']

    # Loop to determin which column sector it is in
    if current_column in columns1:
        return columns1
    elif current_column in columns2:
        return columns2
    else:
        return columns3


def find_sector_rows(current_row):
    # possible row sectors
    rows1 = ['a', 'b', 'c']
    rows2 = ['d', 'e', 'f']
    rows3 = ['g', 'h', 'i']

    # Loop to determin which row sector it is in
    if current_row in rows1:
        return rows1
    elif current_row in rows2:
        return rows2
    else:
        return rows3