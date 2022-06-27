"""
FINAL SCRIPT 

WIP

"""

import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, solve_columnwise, solve_rowwise, solve_quadwise

# Load in Sudoku difficulty = 1
sudoku_df = generate_sudoku(2)

# Columnwise
column_sudoku = solve_columnwise(sudoku_df)

print(column_sudoku)

# Rowwise
row_sudoku = solve_rowwise(column_sudoku)

print(row_sudoku)

# Quadrantwise
quad_sudoku = solve_quadwise(row_sudoku)

print(quad_sudoku)

# Save to CSV
quad_sudoku.to_csv("../output/rowcolquad_simple_result.csv")

