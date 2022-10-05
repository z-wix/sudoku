"""
FINAL SCRIPT 

WIP

"""


import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, solve_sudoku

# Load in difficulty 4
sudoku_df = generate_sudoku(4)

sudoku_master = solve_sudoku(sudoku_df)

sudoku_master

# Save to CSV
sudoku_master.to_csv("../output/sudoku_master_result.csv")