max_num = 0
buffer = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        if line != "":
            buffer += int(line)
        else:
            max_num = max(max_num, buffer)
            buffer = 0

print(max_num)

max_nums = [0,0,0]
buffer = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        if line != "":
            buffer += int(line)
        else:
            for i, num in enumerate(max_nums):
                if max(num, buffer) == buffer:
                    for j in range(len(max_nums)-1, i, -1):
                        max_nums[j] = max_nums[j-1]
                    max_nums[i] = buffer
                    break
            buffer = 0

print(max_nums)
print(sum(max_nums))
