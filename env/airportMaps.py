#Each node of a map represents a 1m X 1m square
#The top of the map represents north

#0: empty spot
#1: obstacle

<<<<<<< HEAD
def getA6201MAP():
    A6201MAP = [[1,1,1,1,1,0,1],
                [0,0,0,0,0,0,0],
                [1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0],
                [1,1,1,1,1,1,0],
                [1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0],]
    return A6201MAP

def getA3001MAP():
    A3001MAP = [[0,0,0,0,0,0,0,0,0],#0
                [0,0,0,1,1,1,0,0,0],#1
                [0,0,0,0,0,0,0,0,0],#2
                [0,1,1,1,0,1,1,1,0],#3
                [0,1,1,1,0,1,1,1,0],#4
                [0,1,1,1,0,1,1,1,0],#5
                [0,1,1,1,0,1,1,1,0],#6
                [0,1,1,1,0,1,1,1,0],#7
                [0,1,1,1,0,1,1,1,0],#8
                [0,1,1,1,0,1,1,1,0],#9
                [0,1,1,1,0,1,1,1,0],#10
                [0,1,1,1,0,1,1,1,0],#11
                [0,0,0,0,0,0,0,0,0],#12
                [0,0,0,0,0,0,0,0,0],]#13
    return A3001MAP


def getA3001GATE():
    A3001GATE = [
        (0, 8),
        (0, 0),
        (13, 0)
    ]
    return A3001GATE
=======

A3001MAP = [[0,0,0,0,0,0,0,0,0,0,0,0,0],#0
            [0,0,1,1,1,1,1,1,1,1,0,0,0],#1
            [0,0,1,1,1,1,1,1,1,1,0,0,0],#2
            [0,0,1,1,1,1,1,1,1,1,0,1,0],#3
            [0,0,0,0,0,0,0,0,0,0,0,1,0],#4
            [0,0,1,1,1,1,1,1,1,1,0,1,0],#5
            [0,0,1,1,1,1,1,1,1,1,0,0,0],#6
            [0,0,1,1,1,1,1,1,1,1,0,0,0],#7
            [0,0,0,0,0,0,0,0,0,0,0,0,0],#8
            #0,1,2,3,4,5,6,7,8,9,10,11,12
            ]
>>>>>>> 16a494625ab0d58796c1e74eb983c2b7c9b3d59a
