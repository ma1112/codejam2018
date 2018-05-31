import sys
from collections import Counter


def play(N):
    allLikes = {i : 0 for i in range(N)}
    flavours = set([i for i in range(N)])
    for i in range(N):
        liked = sys.stdin.readline().split()[1:]
        liked = list(map(int, liked))

        for l in liked:
            allLikes[l] = allLikes[l]+1

        giveThem = chooseFlavour(flavours,liked,allLikes)
        #sys.stderr.write(" choose: " + str(giveThem) + "\n\n" )

        if giveThem >=0:
            flavours.remove(giveThem)
        print(str(giveThem))
        sys.stdout.flush()



def chooseFlavour(flavours,liked,allLikes):
    #sys.stderr.write("Customer likes : " + str(liked) + "\n")
    preferences = {i : allLikes[i] for i in liked}
    #sys.stderr.write("preferences: " + str(preferences) + "\n")
    sortedPreference = sorted(preferences,key=preferences.get)

    for flavour in sortedPreference:
        if flavour in flavours:
            return flavour
    return -1





line = sys.stdin.readline()
T = int(line)
for t in range(T):
    N = int(sys.stdin.readline())
    play(N)
sys.exit()
