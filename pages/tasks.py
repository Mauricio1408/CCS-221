import matplotlib.pyplot as plt
import numpy as np

plt.title('Lines')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

def MIDPOINT(x1, y1, x2, y2):
    fig = plt.figure()
    dx = x2 - x1
    dy = y2 - y1
    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2
    #initialize the decision parameter
    d = dy - (dx/2)
    x = x1
    y = y1
#     print('x = %s, y = %s' % (x, y))
    #initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while(x < x2):
        x += 1
        #East is chosen
        if (d < 0):
            d += dy
        
        #North East is chosen
        else:
            d += (dy - dx)
            y += 1
        
        xcoordinates.append(x)
        ycoordinates.append(y)
#         print('x = %s, y = %s' % (x, y))
#         print('Midpoint is at', xMid, yMid)
    plt.plot(xcoordinates, ycoordinates)
    plt.plot(int(xMid), int(yMid), 'b.')
    plt.grid()
    plt.scatter(xcoordinates, ycoordinates, color='Red', s=25)

    return fig  

def Midpoint(x, y, x2, y2):
    xMid = (x + x2)/2
    yMid = (y + y2)/2
    plt.plot(int(xMid), int(yMid), 'b.')

def BRESENHAMS_LINE(x1, y1, x2, y2, color):
    fig = plt.figure()
    X_coordinates = [x1]
    Y_coordinates = [y1]
    dx = x2 - x1
    dy = y2 - y1
    Pk = 2*dy-dx 
#     print("     1   |   Pk    |     Xk+1     |    Yk+1    |     Plot       ")
#     print("         |         |        %d    |      %d    |      (%d,%d)   " % (x1, y1, x1, y1))
    for i in range(dx):
        if Pk < 0:
            Pkn = Pk + (2*dy)
            x1 += 1
#             print(" %d     |    %d     |    %d     |    %d      |    %d    | (%d,%d)    " % (1, Pk, Pkn, x1, y1, x1, y1))
            Pk = Pkn

        else:
            Pkn = Pk + (2*dy - 2*dx)
            x1 += 1
            y1 += 1
            print(" %d     |    %d     |    %d     |    %d      |    %d    | (%d,%d)    " % (1, Pk, Pkn, x1, y1, x1, y1))
            Pk = Pkn
        X_coordinates.append(x1)
        Y_coordinates.append(y1)
        X = (X_coordinates[0], X_coordinates[-1])
        Y = (Y_coordinates[0], Y_coordinates[-1])

    plt.plot(X, Y, 'lightblue', linewidth="1")    
    Midpoint(x1, y1, x2, y2)
    plt.scatter(X_coordinates, Y_coordinates, color='BLACK', s=25)
    plt.grid()
    
    return fig

    

