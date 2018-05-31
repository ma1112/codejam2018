import sys
import itertools


def getResult(saws):
    combinations = getCombinations2(saws)
    return len(combinations) -1

def getCombinations2(saws):
    rs = ["R" for i in range(saws[0])]
    bs = ["B" for i in range(saws[1])]
    R = saws[0]
    B = saws[1]
    letters = rs + bs
    combinations = set()
    lastOkLength = 1

    for L in range(0, len(letters) + 1):
        for subset in itertools.combinations(letters, L):
            if R + B < len(subset) or len(subset) > lastOkLength+2: return combinations
            thisComb = (subset.count("R") , subset.count("B"))
            if thisComb not in combinations and thisComb[0]<=R and thisComb[1] <= B:
                combinations.add(thisComb)
                R -= thisComb[0]
                B -= thisComb[1]
                lastOkLength = len(subset)
    return combinations



def getCombinations(saws):
    R = saws[0]
    B = saws[1]
    done = R+B ==0
    combinations = set()
    combinations.add((0,0))
    while not done:
        nextComb = findNextCombination(combinations,R,B)
        if nextComb is None:
            done = True
        else:
            combinations.add(nextComb)
            R-=nextComb[0]
            B-=nextComb[1]
    return combinations


def findNextCombination(combinations,R,B):
    comb = (0,0)
    result = None
    while True:
        if R - comb[0] > B - comb[1]:
            r = tryAddRed(comb,combinations,R,B)
            if r is not None: return r
            r = tryAddBlue(comb,combinations,R,B)
            if r is not None: return r
        else:
            r = tryAddBlue(comb,combinations,R,B)
            if r is not None: return r
            r = tryAddRed(comb, combinations, R, B)
            if r is not None: return r

        if R - comb[0] > B - comb[1] and R-comb[0] > 0:
            comb = (comb[0]+1,comb[1])
        elif B - comb[1] > 0:
            comb = (comb[0] , comb[1] + 1)
        else:
            return None



def tryAddRed(comb, combinations, R,B):
    currentRed = comb[0]
    currentBlue = comb[1]
    if currentRed+1 <= R:
        if (currentRed+1,0) not in combinations: return (currentRed+1,0)
        if (currentRed+1,currentBlue) not in combinations: return (currentRed+1,currentBlue)
    return None

def tryAddBlue(comb, combinations, R,B):
    currentRed = comb[0]
    currentBlue = comb[1]
    if currentBlue+1 <= B:
        if (0,currentBlue) not in combinations: return (0,currentBlue)
        if (currentRed,currentBlue+1) not in combinations: return (currentRed,currentBlue+1)
    return None






line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline()
    saws = list(map(int, line.split()))
    print("Case #" + str(t+1)+ ": " + str(getResult(saws)))