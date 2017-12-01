# CSI 31 KINGSLEY OTTO CONVERTION.PY
# THIS PROGRAM CONVERT METERS TO FEETS

def intro():
    print("This program convert meter/meters to feets")
    return
        
def main():
    intro()
    meters = eval(input("Enter the number of meter/meters to convert: "))
    feets = meters * 3.28084
    print(meters,"meter/meters is =",feets,"feets")
    
main()


"""

This program convert meter/meters to feets
Enter the number of meter/meters to convert: 14
14 meter/meters is = 45.93176 feets

"""

