file = open('input9.txt', 'r')
lines = file.readlines()

tot = 0
tot2 = 0
for line in lines:
    nums = [int(n) for n in line.split()]
    lists = [nums]
    while any(n != 0 for n in nums):
        nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        lists.insert(0, nums)
    tot += sum([l[-1] for l in lists])
    part = 0
    for l in lists:
        part = l[0] - part
    tot2 += part

print("part1:", tot)    
print("part2:", tot2)    
