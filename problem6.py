import math
file = open('input6.txt', 'r')
lines = file.readlines()

tms = lines[0].split(':')[1].split()
rcds = lines[1].split(':')[1].split()
times = [int(x) for x in tms]
records = [int(x) for x in rcds]
time2 = int("".join(tms))
record2 = int("".join(rcds))

def solve(time, record):
    root = math.sqrt(time*time - 4*record)
    s1 = (time+root)/2
    s2 = (time-root)/2
    sol2 = math.floor(s1 - 0.0000001)
    sol1 = math.ceil(s2 + 0.0000001)
    return sol2-sol1+1
    

part1 = math.prod([solve(time, record) for time, record in zip(times, records)])    
part2 = solve(time2,record2)

print("part1", part1)
print("part2", part2)    
