#KINGSLEY.OTTO_FINALE_PROJECT.PY
#CSI31_GRAPHWIN_CIRCLE_PROGRAM.

from graphics import*

#INSTRUCTION TO THE USER.
def intro():
    print("This program allows the user to move a graphic circle to different")
    print("areas in a graphic window.\n")
    return intro

#SHAPE OF THE CIRCLE.
def drawShape(win):
    shape = Circle(Point(50,50),20)
    shape.setOutline("white")
    shape.setFill("red")
    shape.draw(win)
    return shape


#THIS FUNCTION IS TO MOVE THE CIRCLE TO DIFFRENT AREAS
def moveShape(win,shape,n):  
    for i in range (n):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    return moveShape

def main():
    intro()
    n = eval(input("How many times do you wish to move the circle? :"))
    win = GraphWin("Circle", 300, 300)
    win.setBackground("black")
    shape = drawShape(win)
    moveShape(win,shape,n)
    win.close()
    print("*******************************************************************")
    print("*******************************************************************")
    print("                 THANK YOU FOR USING THIS PROGRAM                  ")
    print("*******************************************************************")
    print("*******************************************************************")

main()
    
