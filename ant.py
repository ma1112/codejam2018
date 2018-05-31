import sys
import operator





def getResultOld(ants):
    possibilities = {}
    for ant in ants:

        newPossibilities = {ant:1}

        for weight, length in possibilities.items():
            if weight > ant*6: continue
            newWeight = weight + ant
            newLength = length+1
            if newWeight not in newPossibilities or newPossibilities[newWeight] < newLength:
                newPossibilities[newWeight] = newLength

        for newWeight , newLength in newPossibilities.items():
            if newWeight not in possibilities or possibilities[newWeight] < newLength:
                possibilities[newWeight] = newLength


    return possibilities[max(possibilities.items(), key=operator.itemgetter(1))[0]]

def getResult(ants):
    possibilities = {}
    for ant in ants:

        newPossibilities = {1:ant}

        for length, weight in possibilities.items():
            if weight > ant*6: continue
            newWeight = weight + ant
            newLength = length+1
            if newLength not in newPossibilities or newPossibilities[newLength] > newWeight:
                newPossibilities[newLength] = newWeight

        for newLength, newWeight in newPossibilities.items():
            if newLength not in possibilities or possibilities[newLength] > newWeight:
                possibilities[newLength] = newWeight

    return max(possibilities.items(), key=operator.itemgetter(1))[0]

















line = sys.stdin.readline()
T = int(line)
for t in range(T):
    N = int(sys.stdin.readline())
    line = sys.stdin.readline()
    ants = list(map(int, line.split()))
    print("Case #" + str(t+1)+ ": " + str(getResult(ants)))