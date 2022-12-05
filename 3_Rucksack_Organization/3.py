import string

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def find_sum_priorities(list_of_types):
    return sum([alphabets.index(some_type)+1
        for some_type in list_of_types])

with open("input.txt", "r") as file:
    items = [[line[:(len(line)//2)], line[(len(line)//2):]]
        for line in file.read().split("\n")]

    item_types = [''.join(set(item[0]) & set(item[1]))
        for item in items]

    print(find_sum_priorities(item_types))

with open("input.txt", "r") as file:
    rucksacks = [line for line in file.read().split("\n")]
    iter_rucksacks = iter(rucksacks)
    
    group_types  = [''.join(set(one) & set(two) & set(three))
        for one, two, three in zip(iter_rucksacks, iter_rucksacks, iter_rucksacks)]

    print(find_sum_priorities(group_types))
