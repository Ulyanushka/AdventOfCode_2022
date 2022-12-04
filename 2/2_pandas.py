import pandas as pd

df_rules = pd.DataFrame(
    {
    'A': [3, 6, 0],
    'B': [0, 3, 6],
    'C': [6, 0, 3]
    }, index = ['X', 'Y', 'Z'])

s_shapes = pd.Series({'X': 1, 'Y': 2, 'Z': 3})

s_ends = pd.Series({'X': 0, 'Y': 3, 'Z': 6})

score = 0

with open("input.txt", "r") as file:
    rounds = [line.split(" ") for line in file.read().split("\n")]
    for move in rounds:
        score += df_rules.loc[move[1], move[0]]
        score += s_shapes[move[1]]

print(score)
score = 0

with open("input.txt", "r") as file:
    rounds = [line.split(" ") for line in file.read().split("\n")]
    for move in rounds:
        shape = df_rules[
            df_rules[move[0]] == s_ends[move[1]]
            ].index[0]
        score += s_shapes[shape]
        score += s_ends[move[1]]
        
print(score)
