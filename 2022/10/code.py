# Advent of code Year 2022 Day 10 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/10
# Date = December 10, 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

i, cycle = 0, 1 # i -> track input
ans = 0
X = 1
prev = 0
log = [20, 60, 100, 140, 180, 220]
while i < len(input) and cycle < 222:
    X += prev
    if cycle in log:
        print((cycle ) * X)
        ans += (cycle ) * X
    cmd = input[i][0:4]
    if cmd == "addx":
        num = int(input[i].split()[1].strip())
        if (cycle + 1) in log:
            print((cycle + 1) * X)
            ans += (cycle + 1) * X
        prev = num
        cycle += 2
    else:
        cycle += 1
        prev = 0
    i += 1

print("Part One : "+ str(ans))

matrix = [['.']*40 for _ in range(6)]
i, cycle = 0, 1 # i -> track input
X = 1
prev = 0
while i < len(input) and cycle < 242:
    X += prev

    r, c = (cycle - 1) // 40, (cycle - 1) % 40
    cS = (X ) % 40
    if c >= cS - 1 and c <= cS + 1:
        matrix[r][c] = '#'

    cmd = input[i][0:4]
    if cmd == "addx":
        num = int(input[i].split()[1].strip())
        prev = num

        r, c = (cycle) // 40, (cycle) % 40
        if c >= cS - 1 and c <= cS + 1:
            matrix[r][c] = '#'
        
        cycle += 2
    else:
        cycle += 1
        prev = 0
    i += 1

for i in ["".join(x) for x in matrix]:
    print(i)
