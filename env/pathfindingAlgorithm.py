from math import floor

def pathfindingToTerminal(startingPoint, 
                          endingPoint,
                          direction, 
                          aeroport):
    visitedPath = [[(-1, -1) for col in range(len(aeroport[0]))] for row in range(len(aeroport))]
    
    queue = [startingPoint]
    visitedPath[startingPoint[0]][startingPoint[1]] = startingPoint
    
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # FIND GATEWAY
    while queue[0] != endingPoint:
        posX, posY = queue.pop(0)
        
        for i in range(4):
            movX, movY = movements[(direction + i) % 4]
            nPos = (posX + movX, posY + movY)
            if validPos(nPos, aeroport, visitedPath):
                queue.append(nPos)
                visitedPath[nPos[0]][nPos[1]] = (posX, posY)
                
    
    # EXTRACT PATH
    stack = [queue[0]]
    while stack[len(stack) - 1] != startingPoint:
        #print(stack[len(stack) - 1])
        posX, posY = stack[len(stack) - 1]
        stack.append( visitedPath[posX][posY] )
    
    
    # DECIDE MOVEMENTS
    if startingPoint == endingPoint:
        return 0, 4
    else:
        stack.pop()
        nextMovement = stack.pop()
        
        movementsNew = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        dx, dy = nextMovement[1] - startingPoint[1], startingPoint[0] - nextMovement[0]
        print((dx, dy))
        if dx != 0:
            movDirection = 1 if dx == 1 else 3
        else:
            movDirection = 0 if dy == 1 else 2
        print (movDirection)
    
        movCounter = 0
        
        lastMovement = nextMovement
        
        while (dx, dy) == movementsNew[movDirection]:
            movCounter = movCounter + 1
            
            nextMovement = stack.pop()
            
            dx, dy = nextMovement[1] - lastMovement[1], lastMovement[0] - nextMovement[0]
            print((dx, dy))
            
            lastMovement = nextMovement
            
        
        return movCounter, movDirection

        
    
    
def validPos(p, aeroport, visitedPath):
    posX, posY = p
    isInRange = posX >= 0 and posX < len(aeroport) and posY >= 0 and posY < len(aeroport[0])
    if isInRange:
        isNotObstacle = aeroport[posX][posY] == 0
        hasNotBeenVisited = visitedPath[posX][posY] == (-1, -1)
        
        return isNotObstacle and hasNotBeenVisited
    else: return False
    

def normalizePositions(pos,
                       aeroport):
    posX, posY = pos
    
    if posX <= 0:
        posX = 0
    elif posX >= len(aeroport[0]):
        posX = len(aeroport) - 1
    else:
        posX = floor(posX)
    
    if posY <= 0:
        posY = 0
    elif posY >= len(aeroport):
        posY = len(aeroport[0]) - 1
    else:
        posY = floor(posY)
    
    return posX, posY


def test():
    A6201MAP = [[1,1,1,1,1,0,1],
            [0,0,0,0,0,0,0],
            [1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0],
            [1,1,1,1,1,1,0],
            [1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0],]
    
    #startingPos = (1, 0)
    #endingPos = (5, 6)
    startingPos = (5, 6)
    endingPos = normalizePositions((1.756, -1.23), A6201MAP)
    startingMov = 2
    
    
    return pathfindingToTerminal(startingPos, endingPos, startingMov, A6201MAP)


print(test())