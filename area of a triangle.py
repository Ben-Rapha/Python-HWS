# CSI 31 KINGSLEY OTTO AREA.PY
# THIS PROGRAM CALCULATE THE AREA OF A TRIANGLE.


def intro():
    print("This program calculate the area of a triangle.\n")

import math

def getInputs():
    a = float(input("Enter the first lenght of the triangle: "))
    b = float(input("Enter the second lenght of the triangle: "))
    c = float(input("Enter the third lenght of the triangle: "))
    
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is :",area)
    print("\n")
    
# CALCULATING THE DISTANCE BETWEEN EACH POINT
def distance():
    x1 = eval(input("Enter the first x cordinate: "))
    x2 = eval(input("Enter the second x cordinate: "))
    y1 = eval(input("Enter the first y cordinate: "))
    y2 = eval(input("Enter the second y cordinate: "))
    
    return x1,x2,y1,y2
# GET INPUT FROM USER

def main():
    intro()
    getInputs()
    print("To find the distance between the first points of the triangle")
    x1,x2,y1,y2 = distance()
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("\n")
    print("The distance between the points is :", d)
    print("\n")
    print ("To find the distance between the second points")
    x1,x2,y1,y2 = distance()
    r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The distance between the points is :", r)
    print("\n")
    print ("To find the distance between third points")
    x1,x2,y1,y2 = distance()
    z = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The distance between the points is :", z)    
    
    

main()

"""
This program calculate the area of a triangle.

Enter the first lenght of the triangle: 4
Enter the second lenght of the triangle: 6
Enter the third lenght of the triangle: 8
The area of the triangle is : 11.61895003862225


To find the distance between the first points of the triangle
Enter the first x cordinate: 4
Enter the second x cordinate: 6
Enter the first y cordinate: 8
Enter the second y cordinate: 3


The lenght between the points is : 5.385164807134504


To find the distance between the second points
Enter the first x cordinate: 5
Enter the second x cordinate: 6
Enter the first y cordinate: 8
Enter the second y cordinate: 2
The lenght between the points is : 6.082762530298219


To find the distance between third points
Enter the first x cordinate: 3
Enter the second x cordinate: 5
Enter the first y cordinate: 7
Enter the second y cordinate: 8
The lenght between the points is : 2.23606797749979
"""
