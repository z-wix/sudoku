"""
FINAL SCRIPT 

WIP

"""

import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, solve_columnwise, solve_rowwise, solve_quadwise, count_zeros

# Load in Sudoku difficulty = 1
sudoku_df = generate_sudoku(2)

count0 = count_zeros(sudoku_df)

print(f'There are {count0} missing values left')

# Columnwise
column_sudoku = solve_columnwise(sudoku_df)

count0 = count_zeros(column_sudoku)

print(f'There are {count0} missing values left')

# print(column_sudoku)

# Rowwise
row_sudoku = solve_rowwise(column_sudoku)

count0 = count_zeros(row_sudoku)

print(f'There are {count0} missing values left')

# print(row_sudoku)

# Quadrantwise
quad_sudoku = solve_quadwise(row_sudoku)

count0 = count_zeros(quad_sudoku)

print(f'There are {count0} missing values left')

print(quad_sudoku)

# Save to CSV
quad_sudoku.to_csv("../output/rowcolquad_simple_result.csv")



