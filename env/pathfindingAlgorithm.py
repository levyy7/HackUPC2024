from math import floor

def pathfindingToTerminal(startingPoint, 
                          endingPoint, 
                          aeroport):
    visitedTiles = [[False for col in range(aeroport[0].len())] for row in range(aeroport.len())]
    
    queue = [startingPoint]
    
    



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