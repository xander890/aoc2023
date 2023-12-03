import regex
file1 = open('input1.txt', 'r')
Lines = file1.readlines()
nums = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", \
        "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def solve(regexVal):
    total = 0
    for line in Lines:
        res = regex.findall(regexVal, line, overlapped=True)
        res = [nums[x] if x in nums else x for x in res]
        value = int(res[0] + res[-1])
        total = total + value
    return total

print("part1", solve( r'([1-9])'))
print("part2", solve( r'([1-9]|'+ '|'.join(nums.keys()) +')'))