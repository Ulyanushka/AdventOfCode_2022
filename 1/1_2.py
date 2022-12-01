max_num = [0,0,0]
buffer = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        # print(f"line={line}, buffer={buffer}, max_num={max_num}")
        if line != "":
            buffer += int(line)
        else:
            for i, num in enumerate(max_num):
                if max(num, buffer) == buffer:
                    for j in range(len(max_num)-1, i, -1):
                        max_num[j] = max_num[j-1]
                    max_num[i] = buffer
                    break
            buffer = 0

print(max_num)
print(sum(max_num))
