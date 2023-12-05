import re
file = open('input5.txt', 'r')
lines = file.readlines()

seeds = [int(x) for x in lines[0].split(':')[1].split()]
seeds1 = [[s, 1] for s in seeds] # part one is all starts with size 1
seeds2 = list(zip(seeds[0::2], seeds[1::2])) #even is start, odd is size

def processIntervals(seeds, transforms):
    newSeeds = []
    transforms = sorted(transforms, key=lambda x: x[1])       
    for seed in seeds:
        seedStart, seedCount = seed
        seedEnd = seedStart + seedCount - 1        
        # currentSeed tracks where we are in the current range, covers all the transforms that fall in it.
        # the current seed pack is split into multiple ranges, depending on mapping
        currentSeed = seedStart
        for over in transforms:
            destinationStart, transformStart, transformSize = over
            transformEnd = transformStart + transformSize - 1

            # transform does not overlap... no need to process it, it will not generate new seed packs.
            # the if after the loop will cover the case of no transforms, where the whole range gets mapped to itself.
            if transformEnd < seedStart or transformStart > seedEnd:
                continue

            # transform starts after currentSeed. 
            # We are at the beginning of a gap, at the start or between two transforms.
            # insert an identity map to cover the range
            if currentSeed < transformStart:
                newLen = transformStart - currentSeed
                newSeeds.append([currentSeed, newLen])
                currentSeed += newLen

            deltaStart = currentSeed - transformStart # must be positive after the previous if

            # the transform is in the seed pack range: calculate boundaries and clamp to seed pack end
            newStart = transformStart + deltaStart # "clamps" to the start of the boundary...
            newEnd = min(transformEnd, seedEnd)            
            newLenT = newEnd - newStart + 1 # recalculate length based on new bounds
            newSeeds.append([destinationStart + deltaStart, newLenT]) # remap to the new range
            currentSeed += newLenT;

        # this covers the eventual leftover space left at the end of the seed pack range after all tranforms.
        if currentSeed <= seedEnd:
            newLen = seedEnd - currentSeed + 1
            newSeeds.append([currentSeed, newLen])
            currentSeed += newLen
        # currentSeed is now seedEnd + 1, we are done. Can't be bothered to assert
    return newSeeds


mappings = []

#parse that file babyyyy
for line in lines[2:]:
    if "map" in line:
        mappings.append([])
    else:
        res = re.findall("(\d+) (\d+) (\d+)", line)
        if len(res) == 1:
            mappings[-1].append([int(x) for x in res[0]])

def process(seeds):
    for currentTranforms in mappings:
        seeds = processIntervals(seeds, currentTranforms)
    return min([s[0] for s in seeds])

print("part1:", process(seeds1))
print("part2:", process(seeds2))