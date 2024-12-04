import re

with open('./1.txt', 'r') as input_file:
    raw = input_file.readlines()

result = 0
for line in raw:
    for matched in re.finditer(r'mul\((\d+),(\d+)\)', line):
        left, right = matched.group(1), matched.group(2)
        if 0 <= int(left) <= 999 and 0 <= int(right) <= 999:
            result += int(left) * int(right)

print(result)
