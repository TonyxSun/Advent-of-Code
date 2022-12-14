# Advent of code Year 2022 Day 14 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/14
# Date = December 14, 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

# ---------------------------- Part One ----------------------------
m = [['.' for _ in range(1000)] for __ in range(500)]
m2 = [['.' for _ in range(1000)] for __ in range(500)]

maxY = 0
for line in input:
    path = [[int(x) for x in coords.split(',')] for coords in line.strip().split(" -> ")]

    # draw a line from starting coordinate to the ending coordinate in m
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        maxY = max(maxY, y1)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                m[y][x1] = '#'
                m2[y][x1] = '#'
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                m[y1][x] = '#'
                m2[y1][x] = '#'

maxY += 2
for x in range(1000):
    m[maxY][x] = '#'
    m2[maxY][x] = '#'

def part1StopCondition(x, y):
    return y == maxY-1

def part2StopCondition(x,y):
    return m[y][x] != '.'

def dropRock(x, y) -> bool:
    if stop(x, y):
        print(x, y)
        return False

    if m[y+1][x] == '.': # directly down
        return dropRock(x, y+1)
    elif m[y+1][x-1] == '.': # diagonal down left
        return dropRock(x-1, y+1)
    elif m[y+1][x+1] == '.': # diagonal down right
        return dropRock(x+1, y+1)
    
    # reached the bottom and cannot drop
    m[y][x] = "o"
    return True 
i = 0

stop = part1StopCondition
print(stop)
while dropRock(500, 0):
    i += 1
    # print(i)

print("Part One : "+ str(i))

# ---------------------------- Part Two ----------------------------

stop = part2StopCondition
m = m2 
i = 0
while dropRock(500, 0):
    i += 1

print("Part Two : "+ str(i))
