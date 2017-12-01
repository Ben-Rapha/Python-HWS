#CSI_31_KINGSLEY OTTO SYRACUSE SEQUENCE.PY
#THIS PROGRAM IS A SYRACUSE SEQUENCE.

def intro():
    print("This is a syracuse sequence program")
    return intro


def sequence():
    number = eval(input("Please enter a natural number:"))
    
    print("The syracuse sequence of",number,"is:\n")
    syr = number
    if syr < 1:
        syr = eval(input("Please enter a number greater than 1: "))
    while syr > 1:
        if syr % 2 == 0:
            syr = syr//2
        else :
          syr = 3*syr+1
        print((syr),end=" ")

sequence()
    
