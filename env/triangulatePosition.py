from math import sqrt

def triangulatePosition(circle1, circle2, circle3):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    x3,y3,r3 = circle3

    print((r1, r2, r3))
    
    d12 = dis((x1, y1), (x2, y2))

    if d12 > r1+r2:
        print ("#1")
        return None # no solutions, the circles are separate
    if d12 < abs(r1-r2):
        print("#2")
        return None # no solutions because one circle is contained within the other
    if d12 == 0 and r1 == r2:
        print("#3")
        return None # circles are coincident and there are an infinite number of solutions
    
    a = (r1*r1 - r2*r2 + d12*d12)/(2*d12)
    h = sqrt(r1*r1-a*a)
    xm = x1 + a*(x2 - x1)/d12
    ym = y1 + a*(y2 - y1)/d12
    xs1 = xm + h*(y2 - y1)/d12
    xs2 = xm - h*(y2 - y1)/d12
    ys1 = ym - h*(x2 - x1)/d12
    ys2 = ym + h*(x2 - x1)/d12
    
    #return (xs1, ys1), (xs2, ys2)
    p1 = (xs1, ys1)
    p2 = (xs2, ys2)
    
    disToP1 = abs(dis((x3, y3), p1) - r3)
    disToP2 = abs(dis((x3, y3), p2) - r3)
    
    return p1 if disToP1 <= disToP2 else p2
    


def dis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)



def test():
    circle1 = 0, 0, 1
    circle2 = 1, 0, 0.5
    circle3 = 0.5, -0.1, 0.5
    
    return triangulatePosition(circle1, circle2, circle3)


#print(test())