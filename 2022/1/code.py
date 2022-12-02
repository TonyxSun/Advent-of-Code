# Advent of code Year 2022 Day 1 solution
# Author = TonyxSun
# Date = December 2022
import heapq

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

maxCalories = 0
cur = 0
for line in input:
    if line == "\n":
        maxCalories = max(maxCalories, cur)
        cur = 0
        continue
    cur += int(line)


print("Part One : "+ str(maxCalories))

calories = []
cur = 0
for line in input:
    if line == "\n":
        calories.append(cur)
        cur = 0
        continue
    cur += int(line)

heapq.heapify(calories) # O(n)
res = sum(heapq.nlargest(3, calories)) # O(n + log(3))
print("Part Two : "+ str(res))
