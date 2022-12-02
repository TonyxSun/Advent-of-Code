# Advent of code Year 2022 Day 2 solution
# Author = TonyxSun
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

score = 0
dic = {'X': 'A', "Y": "B", "Z": "C"}
print(ord('A')) # 65
for line in input:
    op, me = line.strip().split(" ")
    me = dic[me]
    print(op, me)
    if op == me:
        score += 3 + (ord(me) - 64)
    elif (ord(me) - ord(op) == 1 
        or ord(me) - ord(op) == -2):
        score += 6 + (ord(me) - 64)
    else:
        score += (ord(me) - 64)

print("Part One : "+ str(score))

score = 0
# for line in input:
#     op, outcome = line.strip().split(" ")
#     if outcome == "Z":
#         me = chr(ord(op) + 1)
#         if ord(me) > ord('C'):
#             me = "A"
#         score += 6 + ord(me) - 64
#     elif outcome == "Y":
#         score += 3 + ord(op) - 64
#     else:
#         me = chr(ord(op) - 1)
#         if ord(me) < ord('A'):
#             me = "C"
#         score += 0 + ord(me) - 64

for line in input:
    op, outcome = line.strip().split(" ")
    op = ord(op) % 64
    if outcome == "Z": # win
        me = (op) % 3 + 1
        score += 6 + me
    elif outcome == "Y": # draw
        score += 3 + op
    else: # lose
        me = (op - 1) 
        if me == 0:
            me = 3
        score += 0 + me


print("Part Two : "+ str(score))
