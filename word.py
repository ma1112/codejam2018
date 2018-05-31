
import sys
from collections import Counter


def getResult(N,L,words):
    letters = []
    phrases = []

    for i in range(L):
        letters.append([])
        phrases.append([])

    for word in words:
        phrase = ""
        for i in range(L):
            letter = word[i]
            letters[i].append(letter)
            phrase += letter
            phrases[i].append(phrase)
    letterCounter = []
    for i in range(L):
        letterCounter.append([])
    for i in range(L):
        letterCounter[i] = Counter(letters[i])

    result = addLetter("",letterCounter,0,L,words)
    if result is False: return chr(45)
    else: return result


def addLetter(currentPhrase, letterCounter, index, L, words):
    if index >=L:
        if currentPhrase in words:
            return False
        else:
            return currentPhrase
    else:
        possibleLetters = letterCounter[index].most_common()
        for i in range(len(possibleLetters)):
            nextPhrase = currentPhrase + possibleLetters[i][0]
            withNewLetter = addLetter(nextPhrase, letterCounter, index+1,L,words)
            if withNewLetter is not False: return withNewLetter
        return False












line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline().split()
    N = int(line[0])
    L = int(line[1])
    words = []
    for l in range(N):
        line = sys.stdin.readline()
        words.append(line.splitlines()[0])
    print("Case #" + str(t+1)+ ": " + getResult(N,L,words))