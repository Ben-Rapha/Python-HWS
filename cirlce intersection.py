#CSI_31_KINGSLEY.OTTO_INTERSECTION.PY
#THIS PROGRAM ACCEPT INPUTS FROM A USER AND DRAW A CIRCLE WITH A HORIZONTAL
#INTERSECTION

from graphics import*
import math


def intro():
     print("This program will draw a graphic cirle with a horizontal intersection")
     return intro
     
def main():
    intro()
    radius = eval(input("Please enter a radius of circle: "))
    yinter = eval(input("Please enter the y-intercept: "))
    if radius >= 10:
       radius= eval(input("please enter a radius less than 10: "))
       yinter = eval(input("Please enter the y-intercept: "))
    
    win = GraphWin("Circle and horizontal Intersection",400,400)
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)
    circle = Circle(center,radius)
    circle.setFill("red")
    circle.setOutline("white")
    win.setBackground("black")
    circle.draw(win)  
    x1 = math.sqrt(radius*radius - yinter*yinter)
    x2 = -math.sqrt(radius*radius - yinter*yinter)
    horizonline = Line(Point(x1,yinter),Point(x2,yinter))
    horizonline.draw(win)
    cen1 = Point(x1,yinter)
    smallcir1 = Circle(cen1,0.12)
    smallcir1.setFill('red')
    cen2 = Point(-x1,yinter)
    smallcir2 = Circle(cen2,0.12)
    smallcir2.setFill('red')
    smallcir1.draw(win)
    smallcir2.draw(win)
    input ( ' Please press ENTER to quit')
    win.close()
    print (' the intercections points are',"%.4f" % x1, 'and',"%.4f" % x2)    
        
        
main()


"""
GRAPHICS NEEDS TO BE IMPORTED


This program will draw a graphic cirle with a horizontal intersection
Please enter a radius of circle: 6
Please enter the y-intercept: 3
 Please press ENTER to quit
 the intercections points are 5.1962 and -5.1962
 """

    
