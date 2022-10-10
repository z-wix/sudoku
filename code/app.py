import pandas as pd
from sudoku_fn import generate_sudoku, zero_to_blanks, split_df
from flask import Flask, render_template

app = Flask(__name__)

caption1 = "Unsolved Sudoku"

unsolved_sudoku = generate_sudoku(5)

unsolved = zero_to_blanks(unsolved_sudoku)

unsolved_split = split_df(unsolved)



caption2 = "Solved Sudoku"

solved = pd.read_csv('../output/sudoku_impossible_result.csv', index_col = 0)

solved_split = split_df(solved)

@app.route("/")
def table():
    return render_template(
        "sudoku.html",
        caption1 = caption1,
        unsolved1 = unsolved_split['a'],
        unsolved2 = unsolved_split['d'], 
        unsolved3 = unsolved_split['g'],

        caption2 = caption2,
        solved1 = solved_split['a'],
        solved2 = solved_split['d'],
        solved3 = solved_split['g']
    )