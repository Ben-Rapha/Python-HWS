# CSI_31_MIDTERM_PROJECT_QUADRATICS.PY
#THIS PROGRAM DETERMINES THE VERTEX AND Y -INTERCEPT OF A PARABOLA

# PRINTS THE INTRODUCTION TO THE USER
def intro():
    print("This program finds the vertex and y-intercept of a parabola")

#GETS A,B AND C VALUES FROM THE USER
def getInputs():
    a,b,c = eval(input("Enter the a,b and c values separating with commas from the f(x)= ax^2+bx+c: "))
    print("\n")
#X-COORDINATE FORMULA
    vertex1 =-b/(2*a)
    print("The x-coordinate of the vertex is:" ,vertex1)
#Y-COODINATE FORMULA
    vertex2 = ((a*vertex1*vertex1)+(b*vertex1)+c)
    print("The y-coordinate of the vertex is:" , vertex2)
#Y-INTERCEPT WHERE X=0
    intercept =(0,c)
    print("And the y-intercept of the parabola is:", intercept)

def main():
    intro()
    print("\n")
    getInputs()
    print("\n")
    print("*************************************************")
    print("*********!!!T H A N K  Y O U!!!******************")
    print("*************************************************")

main()


"""
This program finds the vertex and y-intercept of a parabola


Enter the a,b and c values separating with commas from the f(x)= ax^2+bx+c: 4,6,8


The x-coordinate of the vertex is: -0.75
The y-coordinate of the vertex is: 5.75
And the y-intercept of the parabola is: (0, 8)


*************************************************
*********!!!T H A N K  Y O U!!!******************
*************************************************
"""
