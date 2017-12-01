# CSI 31 KINGSLEY OTTO RECTANGLE.PY
# THIS PROGRAM ALLOWS A USER TO DRAW GRAPHICAL RECTANGLE.

from graphics import*
import math


def intro():
    print("This program allows the user to draw a graphical rectangle.\n")
    return

def main():
    intro()
    win = GraphWin("Rectangle",500,400)
    win.setCoords(0,0,10.0,10.0)
    win.setBackground("brown")
    message = Text(Point(5,9.5),"Please click two points on the window")
    message.draw(win)
    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    rect =  Rectangle(point1,point2).draw(win)
    xValue = abs(point2.getX()-point1.getX())
    yValue = abs(point2.getY()- point1.getY())
    Area = (xValue*yValue)
    Area = "%.4f" % Area
    Perimeter = 2*(xValue+yValue)
    Perimeter = "%.4f" % Perimeter
    area = Text(Point(2.5,1),"The area of the rectangle is :")
    area.draw(win)
    areaa = Text(Point(5.6,1),2)
    areaa.setText(Area)
    areaa.draw(win)
    perimeter = Text(Point(2.7,2),"The perimeter of the triangle is : ")
    perimeter.draw(win)
    perimeterr = Text(Point(5.6,2),0.1)
    perimeterr.setText(Perimeter)
    perimeterr.draw(win)
    
main()
