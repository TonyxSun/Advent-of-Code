# Advent of code Year 2022 Day 3 solution
# Author = TonyxSun
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

# print(ord('a'), ord('z'), ord('Z')) 97, 122, 90

priority = 0
for line in input:
    line = line.strip()
    n = len(line)
    l, r = line[:n//2], line[n//2:]
    assert(len(l) == len(r))

    c = [x for x in set(l).intersection(r)][0]

    if c.isupper():
        priority += ord(c) - 38
    else:
        priority += ord(c) - 96
    

print("Part One : "+ str(priority))

priority = 0

for i in range(0, len(input), 3):
    line1 = input[i].strip()
    line2 = input[i + 1].strip()
    line3 = input[i + 2].strip()

    union_first = set(line1).intersection(line2)
    c = [ x for x in union_first.intersection(line3)][0]

    if c.isupper():
        priority += ord(c) - 38
    else:
        priority += ord(c) - 96

print("Part Two : "+ str(priority))
