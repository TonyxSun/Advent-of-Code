# Advent of code Year 2022 Day 8 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/8
# Date = December 08, 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

R, C = len(input), len(input[0].strip())

visited = set()

# def dfs(r, c, prev):
#     if (r, c) in visited:
#         return
#     if (r not in range(R) or
#         c not in range(C) or
#         int(input[r][c]) <= prev):
#         return
#     print(r, c)
#     visited.add((r, c))
#     val = int(input[r][c])
#     for dir in [(-1, 0), (1,0), (0,-1), (0, 1)]:
#         dfs(r + dir[0], c + dir[1], val)

# for i in range(R):
#     dfs(i, 0, -1)
#     dfs(i, C -1, -1)
# for i in range(C):
#     dfs(0, i, -1)
#     dfs(R-1, i , -1)

row = [-1] * R
for c in range(C):
    for r in range(R):
        if int(input[r][c]) > row[r]:
            visited.add((r,c))
            row[r] = int(input[r][c])
row = [-1] * R
for c in range(C-1, -1, -1):
    for r in range(R):
        if int(input[r][c]) > row[r]:
            visited.add((r,c))
            row[r] = int(input[r][c])
cols = [-1] * C
for r in range(R):
    for c in range(C):
        if int(input[r][c]) > cols[c]:
            visited.add((r,c))
            cols[c] = int(input[r][c])
cols = [-1] * C
for r in range(R-1, -1, -1):
    for c in range(C):
        if int(input[r][c]) > cols[c]:
            visited.add((r,c))
            cols[c] = int(input[r][c])


print("Part One : "+ str(len(visited)))

# it is possible that a tree not visible is the most scenic. consider
"""
55555
51115
51215
51115
55555
"""
def multiply(l):
    res = 1
    for i in l:
        res *= i
    return res 

res = 0
for r in range(R):
    for c in range(C):
        if r in [0, R-1] or c in [0, C-1]:
            continue
        score = [R-1 -r, C-1-c, r, c]
        val = int(input[r][c])

        for i in range(r+ 1, R):
            if int(input[i][c]) >= val:
                score[0] = i-r
                break
        for i in range(c+ 1, C):
            if int(input[r][i]) >= val:
                score[1] = (i-c)
                break
        for i in range(r-1,-1, -1):
            if int(input[i][c]) >= val:
                score[2] = (r-i)
                break
        for i in range(c-1,-1,-1):
            if int(input[r][i]) >= val:
                score[3] = (c-i)
                break
        res = max(res, multiply(score))
        
print("Part Two : "+ str(res))
