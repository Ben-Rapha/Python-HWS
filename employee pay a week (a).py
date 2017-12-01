#CSI_31_KINGSLEY OTTO WORK RATE.PY
#THIS PROGRAM CALCULATE THE NUMBER OF HOURS WORD AND HOURLY RATE.

def intro():
    print("This program calculate total wages for the week.")
    

def getInput():
    name = input("Please enter the employee name: ") 
    hours = eval(input("Please enter number of hours worked: "))
    hourRate= eval(input("Please enter the hourly rate: "))
    return name,hours,hourRate

def main():
    intro()
    name,hours,hourRate=getInput()
    
    if hours > 40:
       overtime=(hourRate*1.5)
       overHours = (hours - 40 )
       overtimePay = (overHours*overtime)
       wage = overtimePay + (hours*hourRate)
       print(name + str("'s"),"total wage is: ","$",wage)

    else:
        wage = hours*hourRate
        print(name + str("'s"),"The total wage is : ","$",wage)


main()
"""
This program calculate total wages for the week.
Please enter the employee name: Raymond
Please enter number of hours worked: 57
Please enter the hourly rate: 12
Raymond's total wage is:  $ 990.0


"""
