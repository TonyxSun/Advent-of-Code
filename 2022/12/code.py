# Advent of code Year 2022 Day 12 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/12
# Date = December 12, 2022
import collections
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

# ---------------------------- Part One ----------------------------
R = len(input)
C = len(input[0])-1

S, E = (0,0), (0, 0)
for i in range(R):
    s = input[i].find("S")
    e = input[i].find("E")
    if s != -1:
        S = (i, s)
    if e != -1:
        E = (i, e)

print(S, E)

dp = [[ord(input[j][i]) - ord('a') for i in range(C)] for j in range(R)]

dp[S[0]][S[1]] = 0
dp[E[0]][E[1]] = 25
print(dp)

def valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C


deque = collections.deque([(S[0], S[1], 0)])

def findShortestPath(deque):
    seen  = set()
    while deque:
        for i in range(len(deque)):
            r, c, d = deque.popleft()
            if (r,c) in seen:
                continue

            seen.add((r, c))

            if r == E[0] and c == E[1]:
                print("Part One : "+ str(d))
                return

            if valid(r+1, c) and dp[r+1][c] - dp[r][c] <= 1:
                deque.append((r+1, c, d+1))
            if valid(r-1, c) and dp[r-1][c] - dp[r][c] <= 1:
                deque.append((r-1, c, d+1))
            if valid(r, c+1) and dp[r][c+1] - dp[r][c] <= 1:
                deque.append((r, c+1, d+1))
            if valid(r, c-1) and dp[r][c-1] - dp[r][c] <= 1:
                deque.append((r, c-1, d+1))

findShortestPath(deque)
# ---------------------------- Part Two ----------------------------
S_List = []
for i in range(R):
    for j in range(C):
        if input[i][j] == "S" or input[i][j] == "a":
            S_List.append((i, j, 0))

deque = collections.deque(S_List)
findShortestPath(deque)


print("Part Two : "+ str(None))
