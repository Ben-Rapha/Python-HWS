#CSI 31 KINGSLEY OTTO CONVERTER.PY
#THIS PROGRAM COVERT FAHRENHEIT TO CELSIUS

from graphics import *

def main():
    win = GraphWin("Fahrenheit Converter", 500, 400)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(0.8,3)," Fahrenheit Temperature:").draw(win)
    Text(Point(0.8,1.5),"Celsius Temperature:").draw(win)
    input = Entry(Point(1.5,3), 5)
    input.setText(" 0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.3),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.8), Point(2,2.8)).draw(win)
    win.getMouse()
    Fahrenheit = eval(input.getText())
    Celsius =(Fahrenheit  -  32)*  5/9
    output.setText(round(Celsius,4))
    button.setText("quit")
    win.getMouse()
    win.close()
main()
