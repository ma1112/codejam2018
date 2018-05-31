import sys
import math

class Field:
    def __init__(self, background, startA, startB, b,a):
        self.startA = startA
        self.startB = startB
        self.a = a
        self.b = b
        self.field = [ background for i in range(a*b)]
    def _getIndex(self,i,j):
        i = i - self.startA
        j = j- self.startB
        result = i * self.a + j

        return result
    def _getCoordinates(self,c):
        i = self.startA +  int(math.floor(c/self.a))
        j = self.startB + c % self.a
        return (i,j)
    def setValue(self,i,j,value):
        index = self._getIndex(i,j)
        self.field[index] = value
    def lowerValue(self,i,j):
        index = self._getIndex(i,j)
        if index < 0 or index >= len(self.field): return
        self.field[index] -=1
    def getValueForCoordinates(self, i, j):
        index = self._getIndex(i,j)
        return self.getvalue(index)
    def getvalue(self,c):
        return self.field[c]
    def getmaxCoordinates(self):
        c = self.field.index(max(self.field))
        return self._getCoordinates(c)





class Gopher:
    def __init__(self, area):
        self.area = area
        self._getSidesOfWorkfield()
        self._generateHeatMaps()

    def _getSidesOfWorkfield(self):
        squareSide  = math.sqrt(self.area)
        self.a = int(math.ceil(squareSide))
        self.b = int(math.ceil(self.area / self.a))

    def _generateHeatMaps(self):
        if self.a < 3 : self.a = 3
        if self.b < 3 : self.b = 3

        startA = 500 - int(math.ceil(self.a)/2)
        startB = 500 - int(math.ceil(self.b)/2)
        self.heatmap = Field(-2000,startA,startB,self.a, self.b)
        endA = startA + self.a
        endB = startB + self.b
        for a in range(startA+1, endA+1-2):
            for b in range(startB + 1, endB +1-2):
                self.heatmap.setValue(a,b,8)
        #self.heatmap[startA + 1 : endA + 1 -1, startB + 1 : endB+1-1] =8
        #self.plan = np.zeros((1000,1000))
        #self.plan[startA : endA + 1, startB : endB +1] = 1
        self.work = Field(0,startA,startB,self.a, self.b)

    def _registerWorkDone(self,i,j):
        isChanged = (self.work.getValueForCoordinates(i,j) == 0)
        if not isChanged: return
        self.work.setValue(i,j,1)
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):
                self.heatmap.lowerValue(ii,jj)
        #self.heatmap[i-1:i+2, j-1:j+2] -=1

    def _interact(self):
        #(i,j) = np.unravel_index(np.argmax(self.heatmap, axis=None), self.heatmap.shape)
        (i,j) = self.heatmap.getmaxCoordinates()
        print(i+1,j+1)
        sys.stdout.flush()
        (i,j) = map(int,sys.stdin.readline().split())
        if i==0 and j==0: return 0
        elif i<0 or j <0: return -1stdout
        self._registerWorkDone(i-1,j-1)
        return 1

    def go(self):
        digging = True
        while digging:
            result = self._interact()
            if result == -1:
                #sys.stderr.write("Could dig " + str(np.sum(self.work))+" holes out of " + str(np.sum(self.plan)))
                sys.exit()
            if result == 0 : digging = False



line = sys.stdin.readline()
T = int(line)
for t in range(T):
    area = int(sys.stdin.readline())
    gopher = Gopher(area)
    gopher.go()
sys.exit()