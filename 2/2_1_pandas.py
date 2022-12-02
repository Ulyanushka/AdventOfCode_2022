import pandas as pd

df_ends =pd.DataFrame(
    {
    'A': [3, 6, 0],
    'B': [0, 3, 6],
    'C': [6, 0, 3]
    }, index = ['X', 'Y', 'Z'])

s_shapes = pd.Series({'X': 1, "Y": 2, "Z": 3})

score = 0

with open("input.txt", "r") as file:
    rounds = [line.split(" ") for line in file.read().split("\n")]
    for move in rounds:
        score += int(df_ends.loc[move[1], move[0]])
        score += s_shapes[move[1]]

print(score)
