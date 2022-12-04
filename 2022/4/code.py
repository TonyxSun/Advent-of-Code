# Advent of code Year 2022 Day 4 solution
# Author = TonyxSun
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

cnt = 0
for line in input:
    l, r = [x.split('-') for x in line.strip().split(',')]
    l1, l2, r1, r2 = int(l[0]), int(r[0]), int(l[1]), int(r[1])
    if ((l1 <= l2 and r2 <= r1) or # range 2 is inner
        (l2 <= l1 and r1 <= r2)): # range 1 is inner
        cnt += 1
    
print("Part One : "+ str(cnt))

cnt = 0
for line in input:
    l, r = [x.split('-') for x in line.strip().split(',')]
    l1, l2, r1, r2 = int(l[0]), int(r[0]), int(l[1]), int(r[1])
    if ((l1 <= l2 and r1 >= l2) or # end of first range overlaps with second
        (l2 <= l1 and r2 >= l1)):  # end of second range overlaps with first
        cnt += 1

print("Part Two : "+ str(cnt))
