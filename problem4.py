file = open('input4.txt', 'r')
lines = file.readlines()
cardCount = [1 for x in range(len(lines))]
points = 0
for n, line in enumerate(lines):
    win, play = line.split(':')[1].split('|')
    win = [int(s) for s in win.split()]
    play = [int(s) for s in play.split()]
    wins = len([x for x in win if x in play])
    points += int(2**(wins - 1))
    for i in range(wins):
        cardCount[n + i + 1] += cardCount[n]

print("part1:", points)
print("part2:", sum(cardCount))    
