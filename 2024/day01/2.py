from collections import defaultdict

with open('./2.txt', 'r') as input_file:
    raw = input_file.readlines()

data = list(map(lambda x: list(map(int, x.strip().split(' ' * 3))), raw))

left = []
right = []

for l, r in data:
    left.append(l)
    right.append(r)

counter = defaultdict(int)
for r in right:
    counter[r] = counter[r] + 1

result = 0

for l in left:
    result += counter[l] * l
print(result)
