# CSI 31 KINGSLEY OTTO SLOPE.PY
# THIS PROGRAM CALCULATE SQUARE ROOT OF POSITIVE NUMBERS.

import math
def intro():
    print("This program calculate square root of positive numbers")


def main():
    intro()
    x = eval(input("Enter the positive number you want square root of:  "))
    guess = eval(input("Enter a guess number for the square root entered: "))
    n = eval(input("How many times do you want to improve the guess: ?"))
    
    final  =(guess+(x/guess))/2
    print(final)
    
    for i in range(n):
        finalans  =(final+(x//final))/2
        print(finalans)
    import decimal
    finalans ="%.5f" % finalans
    diff = abs(x-guess**2)
    diff = "%.5f" % diff
    print("The square root is approximately:" , finalans)
    print ("The difference between your positive number entered and your guess is: ",diff)

    
main()




""""
This program calculate square root of positive numbers
Enter the positive number you want square root of:  27
Enter a guess number for the square root entered: 5.2
How many times do you want to improve the guess: ?5
5.196153846153846
5.098076923076923
5.098076923076923
5.098076923076923
5.098076923076923
5.098076923076923
The square root is approximately: 5.09808
The difference between your positive number entered and your guess is:  0.04000
"""
