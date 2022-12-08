# Advent of code Year 2022 Day 7 solution
# Author = TonyxSun
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

class obj:
    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.parent = parent
    
    def calcSize(self):
        return self.size

class dir(obj):
    def __init__(self, name, parent=None):
        self.children = {} # name : object
        obj.__init__(self, name, parent)
        
    def calcSize(self):
        for name, item in self.children.items():
            self.size += item.calcSize()
        return self.size

class file(obj):
    def __init__(self, name, size):
        self.name = name
        self.size = size


root = dir('/')
curr = root

i = 0
while i < len(input):
    line = input[i].strip()
    cmd = line[2:4]
    if cmd == 'ls':
        i += 1
        while i < len(input) and input[i][0] != '$':
            if input[i][:3] == 'dir':
                name = input[i][4:].strip()
                d = dir(name, curr)
                curr.children[name] = d
            else:
                f = input[i].split(" ")
                f[1] = f[1].strip()
                curr.children[f[1]] = file(f[1], int(f[0]))
            i += 1
        continue
    else: # cd
        if line[5:] == '/':
            curr = root
        elif line[5:] == "..":
            curr = curr.parent
        else:
            curr = curr.children[line[5:]]
    i += 1

small = []
root.calcSize()

def dfs(root):
    if not root:
        return
    if type(root) == file:
        return
    if root.size <= 100000:
        small.append(root.size)
        
    for k,val in root.children.items():
        dfs(val)
dfs(root)

res = sum(small)
print("Part One : "+ str(res))

required_space = 30000000 - (70000000 - root.size)
smallest_over_threshold = [root]
print(required_space)
def dfs(root):
    if not root:
        return
    if type(root) == file:
        return
    if root.size <= required_space:
        return
        
    smallest_over_threshold[0] = min(smallest_over_threshold[0], root, key=lambda x: x.size)
        
    for k,val in root.children.items():
        dfs(val)

dfs(root)

print("Part Two : "+ str(smallest_over_threshold[0].size))
