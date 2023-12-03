import re
file = open('input3.txt', 'r')
lines = file.readlines()

numsPerLine = []
symPerLine = []
p = re.compile(r'(\d+)')
p2 = re.compile(r'([^\d.\n])')

for row, line in enumerate(lines):
    numsPerLine.append([{"num": int(match.group()), "span": match.span()} for match in p.finditer(line)])
    symPerLine.append([{"sym": match.group(), "span": match.span()} for match in p2.finditer(line)])
    
match = 0
totalRatio = 0
for row, symbolsPerRow in enumerate(symPerLine):
    for sym in symbolsPerRow:
        x1, x2 = sym["span"]
        x1 = max(x1 - 1, 0) # expand the range one entry around the symbol
        x2 = min(x2 + 1, len(lines[0]))
        matches = []
        for otherRow in range(row - 1, row + 2): #rows before and after
            for num in list(numsPerLine[otherRow]):
                y1, y2 = num["span"]
                if x2 - 1 >= y1 and y2 - 1 >= x1: # -1 since the span from regex excludes the last element
                    match += num["num"]
                    numsPerLine[otherRow].remove(num) # remove so we don't count twice...
                    matches.append(num["num"])
        if sym["sym"] == '*' and len(matches) == 2:
            ratio = matches[0]*matches[1]
            totalRatio += ratio
                                                    
print("part1:", match)
print("part2:", totalRatio)