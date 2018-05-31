import sys


class Robot:
    def __init__(self, programString):
        program = []
        self.damage = 0
        beam = 1
        for letter in programString:
            if letter == 'C':
                program.append(0)
                beam *=2
            else:
                program.append(beam)
                self.damage += beam
        self.reversedprogram = list(reversed(program))

    def getDamage(self):
        return self.damage

    def reduceDamage(self):
        #finds index where swapping lowers the damage the most.
        swapIndex = None
        for i in range(len(self.reversedprogram)-1):
            if self.reversedprogram[i] > 0 and self.reversedprogram[i+1]==0:
                swapIndex = i
                break
        if swapIndex is None: return (False, self.damage)
        else:
            reducedDamage = self.reversedprogram[i] / 2
            self.reversedprogram[i+1] = reducedDamage
            self.reversedprogram[i] = 0
            self.damage -= reducedDamage
            return(True, self.damage)

    def saveTheWorld(self, D):
        damage = self.getDamage()
        possibleToLower = True
        steps = 0
        while(damage>D and possibleToLower):
            (possibleToLower, damage) = self.reduceDamage()
            if possibleToLower : steps +=1
        if damage>D: return "IMPOSSIBLE"
        else: return str(steps)


line = sys.stdin.readline()
linesToRead = int(line)
for i in range(linesToRead):
    line = sys.stdin.readline()
    parameters = line.split()
    D = int(parameters[0])
    program = parameters[1]

    robot = Robot(program)
    print("Case #" + str(i+1)+ ":" , robot.saveTheWorld(D))