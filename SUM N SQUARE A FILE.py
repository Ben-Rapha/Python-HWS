# CSI 31 KINGSLEY OTTO SUMLIST/SQUAREEACH.PY
# THIS PROGRAM SUMS UP AND SQUARE NUMBERS IN A FILE.



def intro():
    print("This program sums up and square numbers in a file")
    return intro



def sumList(nums):
    sum=0
    for i in range(len(nums)):
        sum = sum+nums[i]
    return sum


def squareEach(nums):
    for i in range(len(nums)):
        nums[1]=nums[i]**2
    return nums


def main():
    intro()
    numbers = input("Please enter the file name that contains the numbers: ")
    infile = open(numbers,'r')
    nums = squareEach(nums)
    sum = sumList(nums)
    print(sum)
    print(nums)

main()

"""

NOTE THE TXT FILE MUST EXIT JUST SO THE CODE DOESN'T BREAK

"""
