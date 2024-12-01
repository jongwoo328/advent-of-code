with open('./1.txt', 'r') as input_file:
    raw = input_file.readlines()

data = list(map(lambda x: list(map(int, x.strip().split(' ' * 3))), raw))

left = []
right = []

for l, r in data:
    left.append(l)
    right.append(r)

left.sort()
right.sort()

result = 0
for l, r in zip(left, right):
    result += abs(r - l)

print(result)
