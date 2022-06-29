"""
FINAL SCRIPT 

WIP

"""

import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, solve_columnwise, solve_rowwise, solve_quadwise, count_zeros, solve_sudoku

# Load in difficulty 3
sudoku_df = generate_sudoku(3)

sudoku_knight = solve_sudoku(sudoku_df)

sudoku_knight

# Save to CSV
sudoku_knight.to_csv("../output/sudoku_hard_result.csv")



