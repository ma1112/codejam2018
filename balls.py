import sys


def getResult(ballsOnBottom):
    route = getRoute(ballsOnBottom)
    if route is None: return "IMPOSSIBLE"
    else:
        resultString = str(len(route)) + "\n"
        for row in route:
            for character in row:
                resultString += character
            resultString+="\n"
        return resultString


def getRoute(ballsOnBottom):
    result = []
    if ballsOnBottom[0] == 0 or ballsOnBottom[-1] == 0:
        return None
    if ballsOnBottom == [1 for i in ballsOnBottom]:
        return [["." for i in ballsOnBottom]]
    ballGoes = whereBallGoes(ballsOnBottom)
    ballsNow = [[1,goes] for goes in ballGoes]
    done = False
    numRows = 0
    while not done:
        changed = False
        numRows+=1
        ballsNext = [None for goes in ballGoes]
        row = ["." for i in ballsOnBottom]
        for i in range(1,len(ballsNow)-1):
            if ballsNow[i] is None: continue
            ball = ballsNow[i]
            if ball[1] > i:
                changed = True
                row[i] = "\\"
                if ballsNext[i+1] is None: ballsNext[i+1] = [ ball[0] ,ball[1]]
                else:
                    ballsNext[i+1][0] = ballsNext[i+1][0] + ball[0]
                    if ballsNext[i+1][1] != ball[1]: raise Exception("smething went wrong.")
            elif ball[1] < i and row[i-1] != "\\":
                changed = True
                row[i] = "/"
                if ballsNext[i-1] is None: ballsNext[i-1] = [ ball[0],ball[1]]
                else:
                    ballsNext[i-1][0] = ballsNext[i-1][0] + ball[0]
                    if ballsNext[i-1][1] != ball[1] : raise Exception("smething went wrong.")
            else:
                if ballsNext[i] is None: ballsNext[i] = [ ball[0] , ball[1]]

        result.append(row)
        ballsNow = ballsNext
        if not changed:
            done = True
            return result







def whereBallGoes(ballsOnBottom):
    sortedIndices = sorted(range(len(ballsOnBottom)), key=lambda x: ballsOnBottom[x])[::-1]
    sortedIndices = sorted(range(len(ballsOnBottom)), key=lambda x: min(len(ballsOnBottom)-1 - x , x))
    availableIndices = list(range(len(ballsOnBottom)))
    result = [-1 for i in ballsOnBottom]
    for nextBigestWellIndex in sortedIndices:
        ballsInWell = ballsOnBottom[nextBigestWellIndex]
        nearestIndices = sorted([(i , abs(nextBigestWellIndex - i)) for i in availableIndices] , key = lambda x: x[1])
        indicesGoHere = nearestIndices[:ballsInWell]
        for i in indicesGoHere:
            availableIndices.remove(i[0])
            result[i[0]] = nextBigestWellIndex
    return result








line = sys.stdin.readline()
T = int(line)
for t in range(T):
    C = int(sys.stdin.readline())
    line = sys.stdin.readline()
    ballsOnBottom = list(map(int, line.split()))
    print("Case #" + str(t+1)+ ": " + str(getResult(ballsOnBottom)))