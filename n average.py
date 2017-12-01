# CSI 31 KINGSLEY OTTO AVERAGE.PY
# THIS PROGRAM CALCULATE THE AVERAGE OF "n" NUMBERS

# Program design task

# 1. Print an introduction to the user.
# 2. Get n values from the user at the console.
# 3. computes the sum of the numbers entered by the user.
# 4. computes the average of the n numbers entered by the user.
# 5. print the sum of the numbers on the screen.
# 6. print the value of the average to the screen.

# Input: The program will prompt the user to enter how many numbers

        # enter the numbers

# output: The program will print the summation of the numbers
#         The program will print the average of the numbers entered 


def intro():
    print("This program calculate the average of n numbers")
    return


def main():
    intro()
    n = eval(input("How many numbers do you have? "))
    sum = 0
    for i in range(n):
        x = eval(input("Enter a number : "))
        sum = sum + x
        
    print("The sum of the numbers entered is", sum)  
    print("It's average is", sum / n)

    

main()


""""

This program calculate the average of n numbers
How many numbers do you have? 6
Enter a number : 2
Enter a number : 3
Enter a number : 5
Enter a number : 6
Enter a number : 7
Enter a number : 8
The sum of the numbers entered is 31
It's average is 5.166666666666667

"""
