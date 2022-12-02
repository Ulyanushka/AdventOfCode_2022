# Grigory Vlasov
# https://github.com/Grigoriy457
#
# there can be problems with parsing the last space line

with open("input.txt", "r") as file:
  elves = [sum(map(int, i.split("\n"))) for i in file.read().split("\n\n")]
  print(max(elves))

with open("input.txt", "r", encoding="utf-8") as file:
  elves = [sum(map(int, i.split("\n"))) for i in file.read().split("\n\n")]
  print(sum(sorted(elves)[-3:]))
