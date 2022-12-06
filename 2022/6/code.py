# Advent of code Year 2022 Day 6 solution
# Author = TonyxSun
# Date = December 2022
import collections

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()[0]

alphabet = [0] *26
fast, slow = 0,0
while fast < len(input):
    f = ord(input[fast]) - 97
    alphabet[f] += 1
    
    if fast - slow == 3:
        if max(alphabet) == 1: # a little slow :/
            break
        
        alphabet[ord(input[slow]) - 97] -= 1
        slow += 1

    fast += 1


print("Part One : "+ str(fast + 1))

counter = collections.Counter(input[0:14])
fast, slow = 14, 0

while fast < len(input)-1:
    if counter.most_common()[0][1] == 1: # I wonder if i can optimize this step
        break
    
    counter[input[fast]] += 1
    counter[input[slow]] -= 1
    fast += 1
    slow += 1

print("Part Two : "+ str(fast))
