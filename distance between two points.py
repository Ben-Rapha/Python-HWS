# CSI 31 KINGSLEY OTTO SLOPE.PY
# THIS PROGRAM CALCULATE THE DISTANCE BETWEEN TWO POINTS.

import math 


def intro():
    print("This program calculate the distance between a line.\n")


#GET INPUTS FROM USER

def main():
    intro()
    x1 = eval(input("Enter the first x cordinate: "))
    
    x2 = eval(input("Enter the second x cordinate: "))
    
    y1 = eval(input("Enter the first y cordinate: "))
    
    y2 = eval(input("Enter the second y cordinate: "))

#FORMULA FOR COMPUTING THE DISTANCE BETWEEN A LINE    
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    print("The distance between the two points is:\n", distance)
    

main()



"""
This program calculate the distance between a line.

Enter the first x cordinate: 3
Enter the second x cordinate: 6
Enter the first y cordinate: 6
Enter the second y cordinate: 2
The distance between the two points is:
 5.0
"""
