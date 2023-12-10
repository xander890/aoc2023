from collections import namedtuple
Point = namedtuple("Point", "x y")
PointChar = namedtuple("PointChar", "x y char")
file = open('input10.txt', 'r')
maze = file.readlines()

N = Point(0, -1)
S = Point(0, 1)
W = Point(-1, 0)
E = Point(1, 0)
INVALID = Point(0,0)

dirs = {"|": [N,S], "-": [E,W], "L": [N,E], "J": [N,W], "7": [S,W], 
        "F": [S,E], "S": [INVALID], ".": [INVALID], "\n": [INVALID]}

def minus(p):
    return Point(-p.x, -p.y)

def add(p1,p2):
    return Point(p1.x + p2.x, p1.y + p2.y)

def nextDirection(newChar, currentDir):
    directionFrom = minus(currentDir)
    availableDirs = dirs[newChar]
    if directionFrom in availableDirs:
        return availableDirs[1 - availableDirs.index(directionFrom)] #the other one is direction to
    else:
        return INVALID
    
def runPath(startPosition, startDirection):
    curPos = startPosition
    curDir = startDirection
    curChar = 'S'
    path = []
    while True:        
        path.append(PointChar(*curPos, curChar))
        curPos = add(curPos, curDir)        
        curChar = maze[curPos.y][curPos.x]
        if curChar == 'S' or curDir == INVALID:
            break
        curDir = nextDirection(curChar, curDir)

    if curChar == 'S':
        for d,v in dirs.items():
            if startDirection in v and minus(curDir) in v:
                path[0] = PointChar(*curPos, d)
    return path

startCoords = INVALID
for y,l in enumerate(maze):
    for x,c in enumerate(l):
        if c == 'S':
            startCoords = Point(x,y)

def part1():
    maxPath = max([len(runPath(startCoords, D)) for D in [N,S,W,E]])          
    maxPathDist = int(maxPath / 2)
    print("part1:", maxPathDist) 
    
def part2():
    paths = [runPath(startCoords, D) for D in [N,S,W,E]]
    maxPath = max(paths, key=lambda x : len(x))
    inside = 0
    for y, line in enumerate(maze):
        pathIntersection = sorted([p for p in maxPath if p.y == y and p.char != '-'])
        outside = True
        for x1,x2 in zip(pathIntersection[:-1], pathIntersection[1:]):
            bend = x1.char + x2.char

            if bend == 'L7' or bend == 'FJ': # s-bends count as 1, so do not flip outside
                continue # bends only contain parts of path, so do not count them

            if bend == 'LJ' or bend == 'F7': # u-bends count as 2, so do flip outside flag
                outside = not outside
                continue # bends only contain parts of path, so do not count them

            outside = not outside
            if not outside:
                inside += x2.x - x1.x - 1
    print('part2:', inside)

part1()
part2()    