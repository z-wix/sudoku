"""
This is my Automatic Sudoku Script!

The idea is that it will loop there the empty values
and assign it a temporary value based on the rules 
of Sudoku. If there is only one possible value, then
it will assign that value. The script will keep looping
thru all the empty values until it is filled in.

This script will just be the looping funciton that will
be used by another scipr to fill in the data.

This is a WORK IN PROGRESS

"""

import pandas as pd
import plotly.express as px
from sudoku_module import find_missing, generate_sudoku

# Load in Sudoku Difficulty = 1
sudoku_df = generate_sudoku()

# Test to split into a 3x3 dataset
cols = list(sudoku_df.columns)
rows = list(sudoku_df.index)

#Empty Dataframe to fill in data with
output_matrix = []
finished_sudoku = pd.DataFrame(
    output_matrix,
    columns = cols,
    index = rows
)

# Loop testing column orientation
print("Solving by Rows")
for i in rows:
    # print(f'Row {i}')
    row = sudoku_df.loc[i]
    for j in cols:
        # print(f'Column {j}')
        value = row.loc[j]
        # print(f'the value is {value}')
        if value == 0:
            x_value = find_missing(row.values)
            # print(f'the missing values are {x_value}')
            if len(x_value) == 1:
                finished_sudoku.loc[i, j] = x_value
        else:
            finished_sudoku.loc[i, j] = value

print(finished_sudoku)

finished_sudoku.to_csv("../output/single_row_result.csv")

# sudoku_df[['A', 'B', 'C']].iloc[[0, 1, 2]]