rules = {
    0 : ["BX", "CY", "AZ"],
    3 : ["AX", "BY", "CZ"],
    6 : ["CX", "AY", "BZ"]
    }

score = 0

with open("input.txt", "r") as file:
    rounds = [line.replace(" ", '') for line in file.read().split("\n")]
    
    for key, value in rules.items():
        for i, v in enumerate(value):
            score += rounds.count(v) * (key + i + 1)

    print(score)
