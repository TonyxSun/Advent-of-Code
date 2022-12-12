# Advent of code Year 2022 Day 11 solution
# Author = TonyxSun
# Link = https://adventofcode.com/2022/day/11
# Date = December 12, 2022
import collections
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

class Monkey:
    def __init__(self, items, op, test_int, throw_t, throw_f):
        self.items = items
        self.throw_t = throw_t
        self.throw_f = throw_f
        self.op = op
        self.test_int = test_int
        self.inspections = 0

def get_monkeys():
    monkeys = []
    i = 0
    while i < len(input):
        items = [int(x) for x in input[i+1][18:].strip().split(", ")]
        op = input[i+2][19:].strip()
        test_int = int(input[i+3][21:].strip())
        throw_t = int(input[i+4][29:].strip())
        throw_f = int(input[i+5][29:].strip())
        i = i + 7
        monkeys.append(Monkey(items, op, test_int, throw_t, throw_f))
    return monkeys

monkeys = get_monkeys()
LCM = 1
for monk in monkeys:
    LCM *= monk.test_int

for x in range(20):
    for i in range(len(monkeys)):
        monkeys[i].inspections += len(monkeys[i].items)
        for old in monkeys[i].items:
            val = eval(monkeys[i].op) // 3
            target = monkeys[i].throw_t if val % monkeys[i].test_int == 0 else monkeys[i].throw_f
            monkeys[target].items.append(val % LCM)
        monkeys[i].items = []
    
    # for i in range(len(monkeys)):
    #     print(monkeys[i].items)
    # print('----------------------------------------------------------------')

res = sorted([x.inspections for x in monkeys], reverse=True)
print("Part One : "+ str(res[0] * res[1]))

monkeys = get_monkeys()

for x in range(10000):
    for i in range(len(monkeys)):
        monkeys[i].inspections += len(monkeys[i].items)
        for old in monkeys[i].items:
            val = eval(monkeys[i].op) 
            monkeys[monkeys[i].throw_t if val % monkeys[i].test_int == 0 else monkeys[i].throw_f].items.append(val % LCM)
        monkeys[i].items = []
    
    # for i in range(len(monkeys)):
    #     print(monkeys[i].items)
    # print('----------------------------------------------------------------')

res = sorted([x.inspections for x in monkeys], reverse=True)
print(res)

print("Part Two : "+ str(res[0] * res[1]))
