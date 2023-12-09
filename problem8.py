import re
import math
file = open('input8.txt', 'r')
lines = file.readlines()

remap = {"R": 1, "L" : 0}
instr = [remap[x] for x in lines[0].strip()]

maps = {}
for line in lines[2:]:
    source, left, right = re.findall("(\w+)", line)
    maps[source] = (left, right)

def updateValue(x, n):
    currInstr = instr[n % len(instr)]
    n += 1
    return n, maps[x][currInstr]
    
def part1():
    curr = 0
    curValue = "AAA"
    while curValue != "ZZZ":
        curr, curValue = updateValue(curValue, curr)    
    print("part1", curr)
    
def part2():
    curr = 0
    curValues = [x for x in maps if x[-1] == "A"]
    periods = []
    # the periods are huge, so find the periods and do not bruteforce
    for c in curValues:
        curr = 0
        curValue = c
        while curValue[-1] != "Z":
            curr, curValue = updateValue(curValue, curr)
        periods.append(curr)
    # the final hit will be in the lcm of all the periods
    print("part2", math.lcm(*periods))

part1()
part2()