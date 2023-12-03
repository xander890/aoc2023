import re
import math 

file = open('input2.txt', 'r')
lines = file.readlines()
target = {'red' : 12, 'green' : 13, 'blue' : 14}

idSum = 0
powSum = 0
for line in lines:  
    res = re.findall(r'(\d+) (\w+)', line)
    gameid = int(re.findall(r'Game (\d+)', line)[0])
    current = {'red' : 0, 'green' : 0, 'blue' : 0}
    for val, color in res:
        current[color] = max(current[color], int(val))

    powSum += math.prod([x for x in current.values() if x > 0])
    if all([current[c] <= target[c] for c in target]):
       idSum += gameid

print("part1:", idSum)
print("part2:", powSum)