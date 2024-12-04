import re

with open('./2.txt', 'r') as input_file:
    raw = input_file.readlines()

result = 0
do = True
for line in raw:
    for matched in re.finditer(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', line):
        text = matched.group()
        if text == 'do()':
            do = True
        elif text == 'don\'t()':
            do = False
        else:
            if do:
                result += int(matched.group(2)) * int(matched.group(3))

print(result)
