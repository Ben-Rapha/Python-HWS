# CSI 31 KINGSLEY OTTO CONVERTION.PY
# THIS PROGRAM CALCULATE THE VOLUME OF A BOX


# Pragram task

# 1. print introduction to the user.
# 2. get lenght, width and height values from the user at the console.
# 3. computes the volume of the bocx by multiplying lenght*width*height
# 4. prints the volume on the screen

# input: the program will prompt the user to enter 3 numbers , length,width and height respectively.
#        enter the numbers


# output: the programe will print the volume of the box


def intro():
    print("This program calculates the volume of a box")
    return

def main():
    intro()
    lenght,width,height = eval(input("Enter the lenght,width and height of the box respectively separating with commas: "))
    volume = lenght*width*height
    print("The volume of the box is",volume,"cubic")
    
main()

"""

This program calculates the volume of a box
Enter the lenght,width and height of the box respectively separating with commas: 12,13,17
The volume of the box is 2652 cubic

"""


 

