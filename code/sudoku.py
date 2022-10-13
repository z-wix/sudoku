"""
FINAL SCRIPT 

WIP

"""


import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, solve_sudoku

# Load in difficulty 5
sudoku_df = generate_sudoku(6)

sudoku_solved = solve_sudoku(sudoku_df)

sudoku_solved

# Save to CSV
sudoku_solved.to_csv("../output/sudoku_super_result.csv")