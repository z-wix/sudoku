'''
The purpose of this script is a module that I 
can just load into each of my scripts that will
custom functions and different levels of input
sudokus ranging in difficulty.
'''

import pandas as pd
import plotly.express as px

# Functions

def generate_sudoku(difficulty = 1):
    '''
    Generates an unfinished Sudoku
    Three difficulty levels:
     - 1 : single value missing per col/row/quad
     - 2 : double values missing per col/row/quad
     - 3 : 20 missing values, multiple per col/row/quad
     - 4 : mostly missing values, hardest level
     Work in Progress
    '''
    if difficulty == 1:
        youngling_sudoku_matrix = [
            [1, 2, 3, 4, 5, 6, 7, 0, 9],
            [4, 5, 0, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 0, 4, 5, 6],

            [0, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 0, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 0, 6, 7],

            [3, 4, 5, 6, 7, 8, 9, 1, 0],
            [6, 7, 8, 0, 1, 2, 3, 4, 5],
            [9, 0, 2, 3, 4, 5, 6, 7, 8]
            ]

        # Test using a dataset
        youngling_sudoku_df = pd.DataFrame(
            youngling_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        youngling_sudoku_df.to_csv("../input/simple_sudoku.csv")

        return youngling_sudoku_df

    elif difficulty == 2:
        padawan_sudoku_matrix = [
            [1, 2, 3, 4, 0, 6, 7, 0, 9],
            [4, 5, 0, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 0, 4, 5, 6],

            [0, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 0, 1, 2, 0, 4],
            [8, 0, 1, 2, 3, 4, 0, 6, 7],

            [3, 4, 5, 6, 7, 8, 9, 1, 0],
            [6, 7, 8, 0, 1, 2, 3, 4, 5],
            [9, 0, 2, 3, 4, 5, 6, 7, 8]
            ]

        # Test using a dataset
        padawan_sudoku_df = pd.DataFrame(
            padawan_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        padawan_sudoku_df.to_csv("../input/medium_sudoku.csv")

        return padawan_sudoku_df

    elif difficulty == 3:
        knight_sudoku_matrix = [
            [1, 2, 3, 4, 0, 6, 7, 0, 9],
            [0, 5, 0, 7, 8, 9, 0, 2, 3],
            [7, 8, 9, 1, 2, 0, 4, 5, 0],

            [0, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 0, 8, 0, 1, 2, 0, 4],
            [8, 0, 1, 2, 3, 4, 0, 6, 7],

            [3, 4, 5, 6, 7, 8, 0, 1, 0],
            [6, 7, 0, 0, 1, 2, 3, 4, 5],
            [9, 0, 2, 0, 4, 5, 0, 7, 8]
            ]

        # Test using a dataset
        knight_sudoku_df = pd.DataFrame(
            knight_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        knight_sudoku_df.to_csv("../input/hard_sudoku.csv")

        return knight_sudoku_df
    else:
        master_sudoku_matrix = [
            [1, 2, 3, 4, 0, 6, 7, 0, 9],
            [0, 5, 0, 7, 8, 9, 0, 2, 3],
            [7, 8, 0, 1, 2, 0, 4, 5, 0],

            [0, 3, 4, 5, 0, 7, 8, 9, 1],
            [5, 6, 0, 8, 0, 1, 2, 0, 4],
            [8, 0, 0, 2, 3, 4, 0, 6, 7],

            [3, 4, 5, 6, 7, 8, 0, 1, 0],
            [6, 7, 0, 0, 1, 2, 3, 4, 5],
            [9, 0, 2, 0, 4, 5, 0, 7, 8]
            ]

        # Test using a dataset
        master_sudoku_df = pd.DataFrame(
            master_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        master_sudoku_df.to_csv("../input/master_sudoku.csv")

        return master_sudoku_df

def find_missing(lst):
    '''
    Finds missing values between 1-9 for a given list of values
    '''
    return [x for x in range(1,10) if x not in lst]

def add_char(char, incr = 1):
    '''
    Increments Alphabetical Letters
    '''
    int = ord(char[0])
    next_char = chr(int + incr)
    return next_char

def find_sector_columns(current_column):
    '''
    Finds Quadrant Columns for given column.
    '''
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
    '''
    Find Quadrant Rows for given row
    '''
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

def solve_columnwise(df):
    '''
    Solves Sudoku by Column orientation
    '''
    # Get Rows and Columns from df
    cols = list(df.columns)
    rows = list(df.index)

    # Empty Dataframe to fill in data with
    output_matrix = []
    output_df = pd.DataFrame(
        output_matrix,
        columns = cols,
        index = rows
    )

    # Loop to solve by column
    print("Solving by Column")
    for i in cols:
        #print(f'Colummn {i}')
        column = df[i]
        for j in rows:
            #print(f'index {j}')
            value = column.loc[j]
            #print(f'the value is {value}')
            if value == 0:
                x_value = find_missing(column.values)
                #print(f'the missing values are {x_value}')
                if len(x_value) == 1:
                    output_df.loc[j,i] = x_value[0]
                else:
                    print(f"There are multiple values missing {x_value} in Row {j} Col {i}")
                    output_df.loc[j,i] = 0
            else:
                output_df.loc[j,i] = value
    return output_df

def solve_rowwise(df):
    '''
    Solves Sudoku by Row orientation
    '''
    # Get Rows and Columns from df
    cols = list(df.columns)
    rows = list(df.index)

    # Empty Dataframe to fill in data with
    output_matrix = []
    output_df = pd.DataFrame(
        output_matrix,
        columns = cols,
        index = rows
    )

    # Loop solving row orientation
    print("Solving by Row")
    for i in rows:
        # print(f'Row {i}')
        row = df.loc[i]
        for j in cols:
            # print(f'Column {j}')
            value = row.loc[j]
            # print(f'the value is {value}')
            if value == 0:
                x_value = find_missing(row.values)
                # print(f'the missing values are {x_value}')
                if len(x_value) == 1:
                    output_df.loc[i, j] = x_value[0]
                else:
                    print(f"There are multiple values missing {x_value} in Row {i} Col {j}")
                    output_df.loc[i, j] = 0
            else:
                output_df.loc[i, j] = value
    return output_df

def solve_quadwise(df):
    '''
    Solves Sudoku by Quadrant orientation
    '''
    # Get Rows and Columns from df
    cols = list(df.columns)
    rows = list(df.index)

    # Empty Dataframe to fill in data with
    output_matrix = []
    output_df = pd.DataFrame(
        output_matrix,
        columns = cols,
        index = rows
    )

    # Loop solving quad orientation
    print("Solving by Quadrant")
    for i in rows:
        # print(f'Row {i}')
        row = df.loc[i]
        for j in cols:
            # print(f'Column {j}')
            value = row.loc[j]
            # print(f'the value is {value}')
            if value == 0:
                quad = df[find_sector_columns(j)].loc[find_sector_rows(i)]
                x_value = find_missing(quad.values)
                # print(f'the missing values are {x_value}')
                if len(x_value) == 1:
                    output_df.loc[i, j] = x_value[0]
                else:
                    print(f"There are multiple values missing {x_value} in Row {i} Col {j}")
                    output_df.loc[i, j] = 0
            else:
                output_df.loc[i, j] = value
    return output_df

def count_zeros(df):
    '''
    Counts Zeros present in Dataframe
    '''
    count0 = 0
    for i in df.columns:
        n = (df[i] == 0).sum()
        count0 += n
    print(f'There are {count0} missing values left')
    return count0


def solve_sudoku(df):
    '''
    Solves the Sudoku using all three methods.
    First counts if there are any 0's (missing values) in the sudoku.
    Then does a while loop thru the three functions until there are no
    more 0's and prints out the finished sudoku.
    '''
    count0 = count_zeros(df)
    while count0 > 0:
        df = solve_columnwise(df)
        col0 = count_zeros(df)
        df = solve_rowwise(df)
        row0 = count_zeros(df)
        df = solve_quadwise(df)
        count0 = count_zeros(df)
        if count0 == col0:
            print("Unsolvable")
            return df
    return df