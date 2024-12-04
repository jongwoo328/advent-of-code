with open('./1.txt', 'r') as input_file:
    raw = input_file.readlines()

data = list(map(lambda x: list(map(int, x.strip().split(' '))), raw))

safe_count = 0

for report in data:
    before = None
    safe_increasing = True
    safe_decreasing = True
    for now in report:
        if before is None:
            before = now
            continue

        if not safe_decreasing and not safe_increasing:
            break

        if before <= now:
            safe_decreasing = False
            if now - before < 1 or now - before > 3:
               safe_increasing = False

        if before >= now:
            safe_increasing = False
            if before - now < 1 or before - now > 3:
                safe_decreasing = False

        before = now

    else:
        if safe_increasing or safe_decreasing:
            safe_count += 1

print(safe_count)
