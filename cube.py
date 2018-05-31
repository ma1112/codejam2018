import math
import sys

def get_result(area):
    if area ==1:
        return get_nonrotated_cube()
    if area <=math.sqrt(2):
        return get_rotated_around_one_axis(area)
    else:
        return get_rotated_around_two_axis(area)

def get_nonrotated_cube():
    return[[0.5, 0, 0] , [0, 0.5, 0], [0,0,0.5]]

def get_rotated_around_one_axis(area):
    Z1 = math.sqrt(max(0, 2.0 - area * area)) / 2.0
    scalarProd = 2*Z1 + area
    cosRot = scalarProd / 2.0
    sinRot = math.sqrt(max(0,1.0 - cosRot * cosRot))
    (P1,P2,P3)  = get_points()
    return rotAs(P1,P2,P3,sinRot,cosRot)

def get_points():
    return([-0.5,0,0] , [0,0.5,0] , [0,0,0.5])

def rotAs(P1,P2,P3,sinRot,cosRot):
    P1 = rotA(P1,cosRot,sinRot)
    P2 = rotA(P2,cosRot,sinRot)
    P3 = rotA(P3,cosRot,sinRot)
    return(P1,P2,P3)

def rotBs(P1,P2,P3,sinRot,cosRot):
    P1 = rotB(P1,cosRot,sinRot)
    P2 = rotB(P2,cosRot,sinRot)
    P3 = rotB(P3,cosRot,sinRot)
    return(P1,P2,P3)


def rotA(P,cosRot,sinRot):
    result =[P[0],
             P[1] *cosRot - P[2] * sinRot,
             P[1] * sinRot + P[2] * cosRot]
    return result




def rotB(P,cosRot,sinRot):
    result = [P[0] * cosRot + P[2] * sinRot,
              P[1],
              -P[0] * sinRot + P[2] * cosRot]
    return result

def get_rotated_around_two_axis(area):
    cosRotB = 1.0/3.0 * (math.sqrt(2) * area - math.sqrt(max(0,3-area*area)))
    sinRotB = math.sqrt(1.0 - cosRotB * cosRotB)

    (P1,P2,P3) = get_rotated_around_one_axis(math.sqrt(2))
    (P1, P2, P3) = rotBs(P1,P2,P3,sinRotB,cosRotB)
    return(P1,P2,P3)


def printCoordinate(P):
    print(P[0], P[1], P[2])


line = sys.stdin.readline()
T = int(line)
for t in range(T):
    area = float(sys.stdin.readline())
    (P1,P2,P3) = get_result(area)
    print("Case #" + str(t+1)+ ":")
    printCoordinate(P1)
    printCoordinate(P2)
    printCoordinate(P3)

