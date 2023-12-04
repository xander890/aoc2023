import re
file = open('input3.txt', 'r')
lines = file.readlines()

digits = re.compile(r'(\d+)')
symbols = re.compile(r'([^\d.\n])')

def processLine(row):
    if row < 0 or row >= len(lines):
        return None
    return [{"num": int(match.group()), "span": match.span()} for match in digits.finditer(lines[row])]

total = totalRatio = 0
prevLine = curLine = nextLine = None

for row in range(len(lines)):
    prevLine = curLine if curLine else processLine(row - 1)
    curLine = nextLine if nextLine else processLine(row)
    nextLine = processLine(row + 1)
    for match in symbols.finditer(lines[row]):
        sym = match.group()
        x1, x2 = match.span()
        x1 = max(x1 - 1, 0) # expand the range one entry around the symbol
        x2 = min(x2 + 1, len(lines[0]) + 1)
        matches = []
        for otherRow in [prevLine, curLine, nextLine]:
            for num in list(otherRow):
                y1, y2 = num["span"]
                if x2 - 1 >= y1 and y2 - 1 >= x1: # -1 since the span from regex excludes the last element
                    total += num["num"]
                    otherRow.remove(num) # remove so we don't count twice...
                    matches.append(num["num"])

        if sym == '*' and len(matches) == 2:
            ratio = matches[0] * matches[1]
            totalRatio += ratio

print("part1:", total)
print("part2:", totalRatio)