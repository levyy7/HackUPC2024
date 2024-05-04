from math import floor

def pathfindingToTerminal(startingPoint, 
                          endingPoint,
                          direction, 
                          aeroport):
    visitedPath = [[(-1, -1) for col in range(aeroport[0].len())] for row in range(aeroport.len())]
    
    queue = [startingPoint]
    visitedPath[startingPoint[0]][startingPoint[1]] = startingPoint
    
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # FIND GATEWAY
    while queue[0] != endingPoint:
        posX, posY = queue.pop(0)
        
        for i in range(4):
            movX, movY = movements[(direction + i) % 4]
            nPos = (posX + movX, posY + movY)
            if validPos(nPos):
                queue.append(nPos)
                visitedPath[nPos[0]][nPos[1]] = (posX, posY)
                
    
    # EXTRACT PATH
    stack = [queue.top()]
    while stack[stack.len() - 1] != startingPoint:
        posX, posY = stack[stack.len() - 1]
        stack.append( visitedPath[posX][posY] )
    
    
    # DECIDE MOVEMENTS
    if startingPoint == endingPoint:
        return 0, 4
    else:
        stack.pop()
        nextMovement = stack.pop()
        
        dx, dy = nextMovement[0] - startingPoint[0], nextMovement[1] - startingPoint[1]
        if dx != 0:
            movDirection = 1 if dx == 1 else 3
        else:
            movDirection = 0 if dy == 1 else 2
    
        movCounter = 0
        
        while (dx, dy) == movements[movDirection]:
            movCounter = movCounter + 1
            
            nextMovement = stack.pop()
            dx, dy = nextMovement[0] - startingPoint[0], nextMovement[1] - startingPoint[1]
            
        
        return movCounter, movDirection

        
            
def tuple_sum(t1, t2):
   return tuple(a + b for a, b in zip(t1, t2))
    
    
def validPos(p, aeroport, visitedPath):
    posX, posY = p
    isInRange = posX >= 0 and posX < aeroport.len() and posY >= 0 and posY < aeroport[0].len()
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
    elif posX >= aeroport.len():
        posX = aeroport.len() - 1
    else:
        posX = floor(posX)
    
    if posY <= 0:
        posY = 0
    elif posY >= aeroport.len():
        posY = aeroport[0].len() - 1
    else:
        posY = floor(posY)
    
    return posX, posY