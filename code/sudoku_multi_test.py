"""

This is a WORK IN PROGRESS

"""

import pandas as pd
import plotly.express as px
from sudoku_module import find_missing, generate_sudoku

# Load in Sudoku difficulty = 2
sudoku_df = generate_sudoku(2)

# Get Rows and Columns from df
cols = list(sudoku_df.columns)
rows = list(sudoku_df.index)

# Empty Dataframe to fill in data with
output_matrix = []
finished_sudoku = pd.DataFrame(
    output_matrix,
    columns = cols,
    index = rows
)

# Loop solving column orientation
print("Solving by Column")
for i in cols:
    #print(f'Colummn {i}')
    column = sudoku_df[i]
    for j in rows:
        #print(f'index {j}')
        value = column.loc[j]
        #print(f'the value is {value}')
        if value == 0:
            x_value = find_missing(column.values)
            #print(f'the missing values are {x_value}')
            if len(x_value) == 1:
                finished_sudoku.loc[j,i] = x_value
            else:
                print(f"There are multiple values missing {x_value}")
                finished_sudoku.loc[j,i] = x_value
        else:
            finished_sudoku.loc[j,i] = value

print(finished_sudoku)

# Save to CSV
finished_sudoku.to_csv("../output/multi_column_result.csv")