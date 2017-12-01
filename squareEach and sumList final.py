#CSI 31 KINGSLEY OTTO SQUAREEACH AND SUMLIST.PY
#THIS PROGRAM SQUARES AND SUM NUMBERS IN A FILE.


def intro():
    print("This program squares and sum numbers in a file.\n")
    return intro
          
def toNumbers(nums):
    new_nums = []
    for n in nums:
        new_nums.append(int(n))
    return new_nums

def squareEach(nums):
    for i in range(len(nums)):
        nums[i]= (nums[i])*(nums[i])
    return nums   
def main():
    intro()   
    numbers = input("Please enter the file name that contains the numbers: ")
    infile = open(numbers,'r')
    nums = []
    for line in infile:
        nums.append(line)
    nums = toNumbers(nums)
    print()
    print("The numbers in the file are:")
    print(nums)
    summ = 0
    nums = squareEach(nums)
    summ = 0
    for i in range(len((nums))):
        summ = summ + nums[i]
    print()
    print("The square of each number in the file is:")
    print(nums)
    print()
    print("The sum of squared numbers in the file is:")
    print(summ)

main()
"""
This program squares and sum numbers in a file.

Please enter the file name that contains the numbers: nums.txt

The numbers in the file are:
[8, 9, 7, 4, 6, 5, 15, 11, 13, 16, 23, 1, 4, 3, 2, 12, 18, 21]

The square of each number in the file is:
[64, 81, 49, 16, 36, 25, 225, 121, 169, 256, 529, 1, 16, 9, 4, 144, 324, 441]

The sum of squared numbers in the file is:
2510
"""
