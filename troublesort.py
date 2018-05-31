import sys
from collections import Counter

line = sys.stdin.readline()
T = int(line)
for t in range(T):
    line = sys.stdin.readline()
    length = int(line) # I don't care
    line = sys.stdin.readline()
    array = line.split()

    def method1(array):

        evenIndexed = Counter(array[::2])
        oddIndexed = Counter(array[1::2])
        sortedArray = sorted(array)

        even = True
        badIndex = None
        for i in range(len(sortedArray)):
            element = sortedArray[i]
            if even:
                num = evenIndexed.get(element)
                if num is None or num <1:
                    badIndex = i
                    break
                else: evenIndexed[element] = num-1
            else:
                num = oddIndexed.get(element)
                if num is None or num <1:
                    badIndex = i
                    break
                else: oddIndexed[element] = num-1
            even = not even

        if badIndex is None: result = "OK"
        else: result = str(badIndex)
        return  result


    def method2(array):
        if len(array)<2: return "OK"
        array = list(map(int,array))
        evenIndexed = array[::2]
        oddIndexed = array[1::2]
        sortedEven = sorted(evenIndexed)
        sortedOdd = sorted(oddIndexed)
        L = len(sortedOdd)
        for i in range(L):
            if sortedEven[i] > sortedOdd[i] : return str(2*i)
            if i < L-1 and sortedOdd[i] > sortedEven[i+1] : return str(2*i + 1)
        if len(sortedEven) > len(sortedOdd) and sortedOdd[-1] > sortedEven[-1] : return str(2*L-1)
        return "OK"


    print("Case #" + str(t+1)+ ": " + method2(array))