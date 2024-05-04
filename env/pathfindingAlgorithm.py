from math import floor

def pathfindingToTerminal(startingPoint, 
                          endingPoint, 
                          aeroport):
    


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
        posY = aeroport.len() - 1
    else:
        posY = floor(posY)
    
    return posX, posY