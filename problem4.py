file = open('input4.txt', 'r')
lines = file.readlines()
cardCount = [1] * len(lines)
points = 0
for n, line in enumerate(lines):
    sepCol = line.index(':')
    sepBar = line.index('|')
    win = line[sepCol+1:sepBar].split()
    play = line[sepBar:].split()
    wins = len(set(win) & set(play))
    points += int(2**(wins - 1))
    for i in range(wins):
        cardCount[n + i + 1] += cardCount[n]

print("part1:", points)
print("part2:", sum(cardCount))
