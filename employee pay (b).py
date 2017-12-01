#CSI_31_KINGSLEY OTTO WORK RATE.PY
#THIS PROGRAM CALCULATE THE NUMBER OF HOURS WORKED AND HOURLY RATE.

def intro():
    print("This program calculate total wages for the week.")
    

def main():
    intro()
    people =eval(input("How many people do you wish to calculate weeekly pay for?: "))
    if people ==1:
        name = input("Please enter the employee name: ") 
        hours = eval(input("Please enter the number of hours worked: "))
        hourRate= eval(input("Please enter the hourly rate: "))
        if hours > 40:
            overtime=(hourRate*1.5)
            overHours = (hours - 40 )
            overtimePay = (overHours*overtime)
            wage = overtimePay + (hours*hourRate)
            print(name + str("'s"),"The total wage is: ","$",wage)
        else:
            wage = hours*hourRate
            print(name + str("'s"),"The total wage is : ","$",wage)
    if people > 1:
        payroll = 0
        for i in range (people):
            name = input("Please enter the employee name: ")
            hours = eval(input("Please enter the number of hours worked: "))
            if hours > 40:
                hourRate= eval(input("Please enter the hourly rate: "))
                overtime=(hourRate*1.5)
                overHours = (hours - 40 )
                overtimePay = (overHours*overtime)
                wage = overtimePay + (hours*hourRate)
                print(name + str("'s"),"The total wage is: ","$",wage)
            elif hours <= 40:
                hourRate= eval(input("Please enter the hourly rate: "))
                wage = hours*hourRate
                print(name + str("'s"),"The total wage is :","$",wage)
                
main()

"""
This program calculate total wages for the week.
How many people do you wish to calculate weeekly pay for?: 2
Please enter the employee name: NU
Please enter the number of hours worked: 3
Please enter the hourly rate: 5
NU's The total wage is : $ 15
Please enter the employee name: 3
Please enter the number of hours worked: 4
Please enter the hourly rate: 3
3's The total wage is : $ 12
"""
