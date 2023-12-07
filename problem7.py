import functools
file = open('input7.txt', 'r')
lines = file.readlines()

valueMap1 = {x : i for i,x in enumerate("23456789TJQKA")}
valueMap2 = {x : i for i,x in enumerate("J23456789TQKA")}

# how many sets of   1,2,3,4,5 cards there are    
FIVEOFAKIND =       (0,0,0,0,1)
POKER =             (1,0,0,1,0)
FULL =              (0,1,1,0,0)
TRIS =              (2,0,1,0,0)
DOUBLEPAIR =        (1,2,0,0,0)
PAIR =              (3,1,0,0,0) 
HIGHEST =           (5,0,0,0,0)
ordered = [HIGHEST, PAIR, DOUBLEPAIR, TRIS, FULL, POKER, FIVEOFAKIND]

def createCounts(hand):
    vals = [0] * 5
    for x in set(hand):
        vals[hand.count(x) - 1] += 1
    return tuple(vals)
        
def handValuePart1(x):    
    return ordered.index(createCounts(x))
    
def remaphand(x, jackCount):
    if jackCount == 0:
        return x

    # double pair is the only different, since:
    # jack in the pair (e.g. JJAAQ) --> POKER
    # jack by itself (e.g. AAQQJ) --> FULL
    if x == DOUBLEPAIR: 
        return POKER if jackCount == 2 else FULL
       
    # it does not matter where the jacks are, except in the case above.
    # FIVEOFAKIND, POKER and FULL only have two types of cards, so always map to FIVEOFAKIND
    # in tris, jack can only be in the tris or by itself. Same with pair.
    # in highest all cards are equivalent.
    dic = { FIVEOFAKIND : FIVEOFAKIND, POKER : FIVEOFAKIND, FULL : FIVEOFAKIND,
            TRIS: POKER, PAIR: TRIS, HIGHEST : PAIR}
    return dic[x]
    
def handValuePart2(x):
    vals = createCounts(x)
    jacks = x.count("J")
    remapped = remaphand(vals, jacks)
    return ordered.index(remapped)
    
def compare(hand, hand2, valfunc, valueMap):
    vh1 = valfunc(hand[0])
    vh2 = valfunc(hand2[0])
    
    if(vh1 != vh2):
        return vh1 - vh2
    
    for x,y in zip(hand[0], hand2[0]):
        if valueMap[x] != valueMap[y]:
            return valueMap[x] - valueMap[y]
    return 0

def comparePart1(hand, hand2):
    return compare(hand, hand2, handValuePart1, valueMap1)

def comparePart2(hand, hand2):
    return compare(hand, hand2, handValuePart2, valueMap2)

res = [[line.split()[0], int(line.split()[1])] for line in lines]
    
res1 = sorted(res, key=functools.cmp_to_key(comparePart1))
tot1 = sum((i+1)*score for i, [hand, score] in enumerate(res1))    
res2 = sorted(res, key=functools.cmp_to_key(comparePart2))
tot2 = sum((i+1)*score for i, [hand, score] in enumerate(res2))    
 
print("part1", tot1)
print("part2", tot2)