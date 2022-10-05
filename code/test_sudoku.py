import pandas as pd
import plotly.express as px
from sudoku_module import generate_sudoku, find_missing, find_sector_columns, find_sector_rows, solve_columnwise, solve_rowwise, solve_quadwise, count_zeros, solve_sudoku

# Load in difficulty 4
df = generate_sudoku(4)

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

# Empty Dataframe to fill in data with
temp_matrix = []
temp_df = pd.DataFrame(
    temp_matrix,
    columns = cols,
    index = rows
)

def check_remaining(lst):
    '''
    check remaining if there are any correct numbers in a give list
    '''
    for i in lst:
        print(i)
        if len(i) == 1:
            complete_lst += i
    return [x for x in range(1,10) if x not in lst]


test_lst = temp_df.loc[1].values
for i in lst:
    print(i)
    if len(i) == 1:
        complete_lst += i


'''
Solves Sudoku by Quadrant orientation
'''

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
                temp_df.loc[i, j] = x_value[0]
            else:
                print(f"There are multiple values missing {x_value} in Row {i} Col {j}")
                output_df.loc[i, j] = 0
                temp_df.loc[i, j] = x_value
        else:
            output_df.loc[i, j] = value
            temp_df.loc[i, j] = value


# temp_df.to_csv("../input/tempvalues_sudoku.csv")



'''
Solves Sudoku by Column orientation
'''

# Empty Dataframe to fill in data with
output_matrix = []
output_df = pd.DataFrame(
    output_matrix,
    columns = cols,
    index = rows
)

# Empty Dataframe to fill in data with
temp_matrix = []
temp_df = pd.DataFrame(
    temp_matrix,
    columns = cols,
    index = rows
)

# Loop to solve by column
print("Solving by Column")
for i in cols:
    #print(f'Colummn {i}')
    column = temp_df[i]
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


'''
Solves Sudoku by Row orientation
'''

# Empty Dataframe to fill in data with
output_matrix = []
output_df = pd.DataFrame(
    output_matrix,
    columns = cols,
    index = rows
)

# Empty Dataframe to fill in data with
temp_matrix = []
temp_df = pd.DataFrame(
    temp_matrix,
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
                temp_df.loc[i, j] = x_value[0]
            else:
                print(f"There are multiple values missing {x_value} in Row {i} Col {j}")
                output_df.loc[i, j] = 0
                temp_df.loc[i, j] = x_value
        else:
            output_df.loc[i, j] = value
            temp_df.loc[i, j] = value





print("Solving New way")
for i in rows:
    print(f'Row {i}')
    row = df.loc[i]
    for j in cols:
        print(f'Column {j}')
        col = df[j]
        value = row.loc[j]
        print(f'the value at position ({i}, {j}) is {value}')
        if value == 0:
            quad = df[find_sector_columns(j)].loc[find_sector_rows(i)]
            x_value = find_missing(quad.values)
            print(f'the missing value(s) at position ({i},{j}) = {x_value}')
            if len(x_value) == 1:
                output_df.loc[i, j] = x_value[0]
                temp_df.loc[i, j] = x_value[0]
            else:
                print(f"There are multiple values missing {x_value} at ({i}, {j})")
                still_missing_numbers = []
                for z in x_value:
                    print(z)
                    if z in row.to_list():
                        print(f'{z} is already in row {i}')
                        continue
                    elif z in col.to_list():
                        print(f'{z} is already in col {j}')
                        continue
                    else:
                        print(f'{z} is not already in a col {j} or row {i}')
                        still_missing_numbers.append(z)
                        output_df.loc[i, j] = z
                if len(still_missing_numbers) == 1:
                    output_df.loc[i, j] = still_missing_numbers[0]
                    temp_df.loc[i, j] = still_missing_numbers[0]
                else:
                    print(f"There are still missing values {still_missing_numbers} at ({i}, {j})")
                    output_df.loc[i, j] = 0
                    temp_df.loc[i, j] = still_missing_numbers
        else:
            output_df.loc[i, j] = value
            temp_df.loc[i, j] = value


def solve_relative_loc(df):
    '''
    Solves Sudoku by using relative location
    or in other words looking to see if possible
    value already exists in relative column or row
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

    print("Solving based on Relative Location")
    for i in rows:
        print(f'Row {i}')
        row = df.loc[i]
        for j in cols:
            print(f'Column {j}')
            col = df[j]
            value = row.loc[j]
            print(f'the value at position ({i}, {j}) is {value}')
            if value == 0:
                quad = df[find_sector_columns(j)].loc[find_sector_rows(i)]
                x_value = find_missing(quad.values)
                print(f'the missing value(s) at position ({i},{j}) = {x_value}')
                if len(x_value) == 1:
                    output_df.loc[i, j] = x_value[0]
                    temp_df.loc[i, j] = x_value[0]
                else:
                    print(f"There are multiple values missing {x_value} at ({i}, {j})")
                    still_missing_numbers = []
                    for z in x_value:
                        print(z)
                        if z in row.to_list():
                            print(f'{z} is already in row {i}')
                            continue
                        elif z in col.to_list():
                            print(f'{z} is already in col {j}')
                            continue
                        else:
                            print(f'{z} is not already in a col {j} or row {i}')
                            still_missing_numbers.append(z)
                            output_df.loc[i, j] = z
                    if len(still_missing_numbers) == 1:
                        output_df.loc[i, j] = still_missing_numbers[0]
                        temp_df.loc[i, j] = still_missing_numbers[0]
                    else:
                        print(f"There are still missing values {still_missing_numbers} at ({i}, {j})")
                        output_df.loc[i, j] = 0
                        temp_df.loc[i, j] = still_missing_numbers
            else:
                output_df.loc[i, j] = value
                temp_df.loc[i, j] = value
    return output_df
