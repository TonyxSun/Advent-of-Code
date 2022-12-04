# Advent of code Year 2022 Day 4 solution
# Author = TonyxSun
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

cnt = 0
for line in input:
    first, second = line.strip().split(',')
    l1,r1 = first.split('-')
    l2,r2 =  second.split('-')
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)
    if ((l1 <= l2 and r2 <= r1) or # range 2 is inner
        (l2 <= l1 and r1 <= r2)): # range 1 is inner
        cnt += 1
    
print("Part One : "+ str(cnt))

cnt = 0
for line in input:
    first, second = line.strip().split(',')
    l1,r1 = first.split('-')
    l2,r2 =  second.split('-')
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)
    if ((l1 <= l2 and r1 >= l2) or # range 2 is inner
        (l2 <= l1 and r2 >= l1)): # range 1 is inner
        cnt += 1

print("Part Two : "+ str(cnt))
