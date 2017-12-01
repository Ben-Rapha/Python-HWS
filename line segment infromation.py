# CSI 31 KINGSLEY OTTO SLOPE.PY
# THIS PROGRAM ALLOWS A USER TO DRAW GRAPHICAL LINE.

from graphics import*
import math


def intro():
    print("This program allows the user to draw a line segement.\n")
    return

def main():
    win = GraphWin("line segment",500,400)
    win.setCoords(0,0,10.0,10.0)
    win.setBackground("Seashell")
    message = Text(Point(5,9.5),"Please make two mouse click in this window")
    message.draw(win)
    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    line = Line(point1,point2)
    line.setWidth(2.5)
    line.draw(win)

    midPX = (point1.getX() + point2.getX())/2
    midPY = (point1.getY() + point2.getY())/2
    midP = Point(midPX,midPY)
    midP = Circle(midP,0.1)
    midP.setFill("cyan")
    midP.draw(win)
    

    xpoint = (point2.getX()- point1.getX())
    if xpoint == 0:
        noslope = Text(Point(5,9.5),"Oops :( please try again in next window. Vertical lines have no slope")
        noslope.draw(win)
        return main()
    ypoint = (point2.getY()- point1.getY())
    slope = ypoint/xpoint
    slope = "%.4f" % slope
    slopetext = Text (Point(1,1),"The slope is:")
    slopetext.draw(win)
    slopeTextt = Text(Point(2.5,1),2)
    slopeTextt.setText(slope)
    slopeTextt.draw(win)

    length = math.sqrt(abs(xpoint**2 + ypoint**2))
    length = "%.4f" % length
    lengthtext = Text(Point(2.3,2),"The lenght of this segement is :")
    lengthtext.draw(win)
    lengthtextt = Text(Point(5,2),0.1)
    lengthtextt.setText(length)
    lengthtextt.draw(win)
main()
