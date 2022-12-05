# Advent of code Year 2022 Day 5 solution
# Author = TonyxSun
# Date = December 2022
import collections
import string
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

# read initial stack (hard coded for input)
stacks = [[] for _ in range(9)] 
pos = 1
for i in range(9):
    for r in range(7, -1, -1):
        if input[r][pos].isalpha():
            stacks[i].append(input[r][pos])
    pos += 4

# make shifts
for i in range(10,len(input)):
    line = input[i].split(" ")
    amount, fr, to = line[1], line[3], line[5]
    for _ in range(int(amount)):
        tmp = stacks[int(fr)-1].pop()
        stacks[int(to)-1].append(tmp)

# read results
res = []
for i in range(9):
    if len(stacks[i]):
        res.append(stacks[i][-1])

print("Part One : "+ str("".join(res)))

# read initial stack (hard coded for input)
stacks = [[] for _ in range(9)]  # can use lists 
pos = 1
for i in range(9):
    for r in range(7, -1, -1):
        if input[r][pos].isalpha():
            stacks[i].append(input[r][pos])
    pos += 4

# make shifts
for i in range(10,len(input)):
    line = input[i].split(" ")
    amount, fr, to = line[1], line[3], line[5]
    tmp = collections.deque()
    for _ in range(int(amount)):
        tmp.appendleft(stacks[int(fr)-1].pop())
    stacks[int(to)-1].extend(tmp)

# read results
res = []
for i in range(9):
    if len(stacks[i]):
        res.append(stacks[i][-1])

print("Part Two : "+ str("".join(res)))