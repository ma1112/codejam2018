import sys
import math



def getResult(D,A,B):
    possibilities = {}
    ADist = [int(d) + int(a) for (d, a) in zip(D, A)]
    BDist = [int(d) - int(b) for (d, b) in zip(D, B)]
    activePossibilities = {}
    prevA = None
    prevB = None
    prevALen = 0
    prevBLen = 0
    for i in range(len(ADist)):
        a = ADist[i]
        b = BDist[i]
        # checking old possibilities:
        killedPossLengths = {}
        toKillKeys = []
        toUpdate = []
        for possibility , length in activePossibilities.items():
            if possibility[0] == a or possibility[1] ==b:
                toUpdate.append(possibility)

        for possibility in toUpdate:
            length = activePossibilities.get(possibility)
            activePossibilities.update({possibility:(length+1)})


        # adding new possibilities

        if i==0:
            prevA = a
            prevB = b
            prevALen = 1
            prevBLen = 1
            if(a,b) not in activePossibilities:
                activePossibilities.update( {(a, b) :1})
        else:
            if (prevA,b) not in activePossibilities:
                activePossibilities.update({(prevA, b) : prevALen+1})
            if (a , prevB) not in activePossibilities:
                activePossibilities.update({(a, prevB) : prevBLen+1})
            if (a,b) not in activePossibilities:
                activePossibilities.update({(a,b) : 1})
            if a == prevA:
                prevALen+=1
            else:
                prevALen = 1

            if b == prevB:
                prevBLen +=1
            else:
                prevBLen =1

            prevA = a
            prevB = b

        for possibility , length in activePossibilities.items():
            if i == len(ADist) -1 or not (possibility[0] == a or possibility[1] ==b):
                if not length in killedPossLengths:
                    if length not in possibilities:
                        possibilities.update({length:1})
                    else:
                        oldNumLen = possibilities.get(length)
                        possibilities.update({length:oldNumLen+1})
                    killedPossLengths.update({length:1})
                toKillKeys.append(possibility)
        print("i", i, "killedPossLengths, ",killedPossLengths)
        for key in toKillKeys:
            del activePossibilities[key]

    maxLen = max(possibilities)
    occurences = possibilities[maxLen]
    return str(maxLen) + " " + str(occurences)














line = sys.stdin.readline()
T = int(line)
for t in range(T):
    D = []
    A = []
    B = []
    S = int(sys.stdin.readline())
    for s in range(S):
        line = sys.stdin.readline()
        line = line.split()
        D.append(int(line[0]))
        A.append(int(line[1]))
        B.append(int(line[2]))

    print("Case #" + str(t+1)+ ": " + str(getResult(D,A,B)))