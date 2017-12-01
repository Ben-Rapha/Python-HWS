# CSI 31 KINGSLEY OTTO SLOPE.PY
# THIS PROGRAM CALCULATE THE SLOPE OF A LINE.

# INTRDUCTION TO THE PROGRAM
def intro():
    print("This program calculate the slope of a line.\n")
    return
#GET CO-ORDINATES FROM THE USER    
def getInputs():
    intro()
    x1 = eval(input("Enter the first x cordinate: "))
    x2 = eval(input("Enter the second x cordinate: "))
    y1 = eval(input("Enter the first y cordinate: ")) 
    y2 = eval(input("Enter the second y cordinate: "))
    a  =(x2-x1)
    

    if a==0:
        print("\n")
        print("oops :( that is a vertical line not slope")
        x1= eval(input("Enter the first x cordinate again:"))
        x2= eval(input("Enter the second x codinate different from the first one:"))

    return x1,x2,y1,y2

def main():
    x1,x2,y1,y2=getInputs()
    print("\n")
    a  =(x2-x1)
    b  =(y2-y1)
    slope= float(a/b)
    print("The slope of the line is :",slope)
   
    
            

main()


"""
This program calculate the slope of a line.

Enter the first x cordinate: 4
Enter the second x cordinate: 8
Enter the first y cordinate: 7
Enter the second y cordinate: 9


The slope of the line is : 2.0



This program calculate the slope of a line.

Enter the first x cordinate: 6
Enter the second x cordinate: 6
Enter the first y cordinate: 7
Enter the second y cordinate: 9


oops :( that is a vertical line not slope
Enter the first x cordinate again:6
Enter the second x codinate different from the first one:2


The slope of the line is : -2.0
"""
