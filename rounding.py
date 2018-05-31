import sys
import math
import collections



def getResult(N, votes):
    (currentPercentage , neededToRoundUp) = getNeededToRoundUp(N,votes)
    votesFor05Perc = int(math.ceil(0.005 * N))
    percForMinimalVotes = (votesFor05Perc / N * 100.0)
    if math.floor(percForMinimalVotes) + 0.5 <= percForMinimalVotes:
        roundedPercForMinimalVotes = math.floor(percForMinimalVotes) +1
    else:
        roundedPercForMinimalVotes = math.floor(percForMinimalVotes)
    remainingVotes = N - sum(votes)
    for neededPair in neededToRoundUp:
        needed = neededPair[0]
        if needed <= votesFor05Perc and needed >= remainingVotes:
            currentPercentage += neededPair[1]
            remainingVotes-= needed
            if remainingVotes <= 0:
                break
    if remainingVotes >0:
        currentPercentage += int(math.floor(remainingVotes / votesFor05Perc)) * roundedPercForMinimalVotes
    return currentPercentage








def getNeededToRoundUp(N, votes):
    neededToRoundUp = []
    totalPercentage = 0
    for vote in votes:
        intPercentage = int(math.floor(vote * 100.0 / N))
        floatPercentage = vote * 100.0 / N
        if floatPercentage >= intPercentage + 0.5:
            currentPercentage = intPercentage +1
            totalPercentage += currentPercentage
        else:
            currentPercentage = intPercentage
            totalPercentage += currentPercentage
            votesNeeded = math.ceil((intPercentage + 0.5 - floatPercentage) * N)
            newPercInt = int(math.floor((vote+votesNeeded) * 100.0 / N))
            newPercFloat = (vote+votesNeeded) * 100.0 / N
            if newPercFloat >= newPercInt + 0.5:
                newPerc = newPercInt + 1
            else:
                newPerc = newPercInt
            neededToRoundUp.append([votesNeeded, newPerc - currentPercentage ])
    return (totalPercentage , sorted(neededToRoundUp))




line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline()
    N = int(line.split()[0])
    line = sys.stdin.readline()
    votes = list(map(int, line.split()))
    print("Case #" + str(t+1)+ ": " + str(getResult(N,votes)))

