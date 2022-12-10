# Advent of code Year 2022 Day 9 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/9
# Date = December 09, 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

visited = set()

startingH = (0, 0)
head  = startingH
tail = startingH
visited.add(startingH)

def move(dir, loc):
    r, c = loc[0], loc[1]
    if dir == 'R':
        c += 1
    elif dir == 'L':
        c -= 1
    elif dir == "U":
        r += 1
    else:
        r -= 1
    return (r, c)

def invalid(head, tail):
    return (abs(head[0] - tail[0]) > 1 )or (abs(head[1] - tail[1]) > 1)

for line in input:
    dir, amt = line.strip().split(" ")
    amt = int(amt)
    # if ((dir in ["R", "L"] and head[1] == tail[1]) or
    # (dir in ["U", "D"] and head[0] == tail[0])): # where the cur position of head will not be counted 
    for i in range(amt):
        prevHead = head
        head = move(dir, head)
        if invalid(head, tail):
            tail = prevHead
            visited.add(tail)

    # print(head, tail)
    # print(len(visited), sorted(visited))

print("Part One : "+ str(len(visited)))

visited = set()

startingH = (0, 0)
rope = [(0,0) for _ in range(10)] 
visited.add(startingH)

def freeMove(knot, head):
    r, c = knot[0], knot[1]
    if r - head[0] > 0:
        r -= 1
    elif r - head[0] < 0:
        r += 1
    if c - head[1] > 0:
        c -= 1
    elif c - head[1] < 0:
        c += 1
    return (r,c)

# for line in input:
#     dir, amt = line.strip().split(" ")
#     amt = int(amt)
#     # if ((dir in ["R", "L"] and head[1] == tail[1]) or
#     # (dir in ["U", "D"] and head[0] == tail[0])): # where the cur position of head will not be counted 
#     for i in range(amt):
#         # prev = rope[0]
#         rope[0] = move(dir, rope[0])
#         for knot in range(1,10):
#             if not valid(rope[knot-1], rope[knot]):
#                 rope[knot] = freeMove(rope[knot], rope[knot-1])
#                 # print(rope[knot-1], rope[knot])
#                 # rope[knot], prev = prev, rope[knot]
#                 # print(i, knot, prev)
#                 if knot == 9:
#                     visited.add(rope[knot])
#             else:
#                 break
#     #     print(rope)
#     # print(rope)
#     print(len(visited), sorted(visited))

for line in input:
    dir, amt = line.strip().split(" ")
    amt = int(amt)
    # if ((dir in ["R", "L"] and head[1] == tail[1]) or
    # (dir in ["U", "D"] and head[0] == tail[0])): # where the cur position of head will not be counted 
    for i in range(amt):
        rope[0] = move(dir, rope[0])
        for knot in range(1,10):
            if invalid(rope[knot-1], rope[knot]):
                rope[knot] = freeMove(rope[knot], rope[knot-1])

            visited.add(rope[9])

print("Part Two : "+ str(len(visited)))

