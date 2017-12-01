# CSI 31 KINGSLEY OTTO CONVERTION.PY
# THIS PROGRAM CONVERT KILOMETERS TO MILES

def intro():
    print("This program converts kilometers to miles")
    return

def main():
    intro()
    kilometers = eval(input("Enter any number to convert: "))
    miles = kilometers * 0.621371
    print(kilometers,"kilometer/kilomters is =",miles,"miles")

main()

"""

This program converts kilometers to miles
Enter any number to convert: 13
13 kilometer/kilomters is = 8.077823 miles

"""
