#Bresenham's Line
import matplotlib.pyplot as plt
import numpy as np

plt.title("BRESENHAM LINE")
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")

def Midpoint(x, y, x2, y2):
    xMid = (x + x2)/2
    yMid = (y + y2)/2
    plt.plot(int(xMid), int(yMid), 'b.')
    print('The midpoint is: ', xMid, yMid)

def BRESENHAMS_LINE(x1, y1, x2, y2, color):
    X_coordinates = [x1]
    Y_coordinates = [y1]
    dx = x2 - x1
    dy = y2 - y1
    Pk = 2*dy-dx 
    print("     1   |   Pk    |     Xk+1     |    Yk+1    |     Plot       ")
    print("         |         |        %d    |      %d    |      (%d,%d)   " % (x1, y1, x1, y1))
    for i in range(dx):
        if Pk < 0:
            Pkn = Pk + (2*dy)
            x1 += 1
            print(" %d     |    %d     |    %d     |    %d      |    %d    | (%d,%d)    " % (1, Pk, Pkn, x1, y1, x1, y1))
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
    plt.scatter(X_coordinates, Y_coordinates, color='BLACK', s=25)

def main():
    print("Coordinates of First Point")
    x, y = map(int, input().split())
    print("Coordinates of Second Point")
    xEnd, yEnd = map(int, input().split())
    color = 'b'
    BRESENHAMS_LINE(x, y, xEnd, yEnd, color)
    Midpoint(x, y, xEnd, yEnd)
    plt.grid()
    plt.show()

if __name__ == '__main__':
  main()
