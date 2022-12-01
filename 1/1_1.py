max_num = 0
buffer = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        # print(f"line={line}, buffer={buffer}, max_num={max_num}")
        if line != "": buffer += int(line)
        else:
            max_num = max(max_num, buffer)
            buffer = 0

print(max_num)
