import pandas as pd

def generate_sudoku(difficulty = 1):
    '''
    Generates an unfinished Sudoku
    Five difficulty levels:
     - 1 : single value missing per col/row/quad
     - 2 : double values missing per col/row/quad
     - 3 : 20 missing values, multiple per col/row/quad
     - 4 : mostly missing values, hardest level
     - 5 : an example from my book expert level
    '''
    if difficulty == 1:
        youngling_sudoku_matrix = [
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
            [7, 8, 0, 1, 2, 0, 4, 5, 0],

            [0, 3, 4, 5, 0, 7, 8, 9, 1],
            [5, 6, 0, 8, 0, 1, 2, 0, 4],
            [8, 0, 0, 2, 3, 4, 0, 6, 7],

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
    elif difficulty == 4:
        master_sudoku_matrix = [
            [0, 2, 0, 4, 0, 6, 7, 0, 9],
            [0, 0, 0, 7, 0, 9, 0, 0, 3],
            [0, 8, 0, 0, 2, 0, 4, 5, 0],

            [0, 0, 4, 5, 0, 7, 8, 9, 1],
            [5, 6, 0, 8, 0, 0, 2, 0, 4],
            [8, 0, 0, 2, 0, 4, 0, 6, 7],

            [3, 4, 0, 6, 7, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 3, 0, 5],
            [9, 0, 2, 0, 0, 5, 0, 0, 8]
            ]

        # Test using a dataset
        master_sudoku_df = pd.DataFrame(
            master_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        master_sudoku_df.to_csv("../input/master_sudoku.csv")

        return master_sudoku_df
    elif difficulty == 5:
        impossible_sudoku_matrix = [
            [2, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 9, 0],
            [9, 0, 6, 0, 2, 7, 1, 0, 0],

            [0, 6, 4, 0, 0, 0, 0, 0, 1],
            [0, 9, 0, 7, 0, 6, 0, 3, 0],
            [3, 0, 0, 0, 0, 0, 5, 4, 0],

            [0, 0, 1, 4, 5, 0, 8, 0, 9],
            [0, 2, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 5]
            ]

        # Test using a dataset
        impossible_sudoku_df = pd.DataFrame(
            impossible_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        impossible_sudoku_df.to_csv("../input/impossible_sudoku.csv")

        return impossible_sudoku_df
    else:
        super_sudoku_matrix = [
            [1, 0, 0, 0, 0, 8, 0, 6, 0],
            [0, 4, 0, 0, 0, 7, 1, 0, 3],
            [8, 0, 2, 0, 0, 0, 9, 0, 0],

            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [3, 0, 0, 0, 9, 0, 0, 0, 7],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],

            [0, 0, 7, 0, 0, 0, 8, 0, 4],
            [9, 0, 5, 7, 0, 0, 0, 2, 0],
            [0, 8, 0, 1, 0, 0, 0, 0, 6]
            ]

        # Test using a dataset
        super_sudoku_df = pd.DataFrame(
            super_sudoku_matrix,
            columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        )

        super_sudoku_df.to_csv("../input/super_sudoku.csv")

        return super_sudoku_df

def add_char(char, incr = 1):
    '''
    Increments Alphabetical Letters
    '''
    int = ord(char[0])
    next_char = chr(int + incr)
    return next_char

    
def split_df(df):
    dict_of_df = {}

    for i in df.index[::3]:
        start = i
        end = add_char(i, 2)
        dict_of_df["{}".format(i)] = df.loc[start:end,].values
    return dict_of_df


def zero_to_blanks(df):
    for col in df.columns:
        df[col].replace(0, "", inplace = True)
    return df