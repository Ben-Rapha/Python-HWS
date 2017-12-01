# CSI_31_KINGSLEY_OTTO_FINAL_PROJECT.PY
# THIS PROGRAM CHECKS A USER'S ID AND PASSWORD AGAINST A FILE.

import sys
# Introduction to the user
def intro():
    print("This program asks the user for his/her user-ID and password and runs ")
    print("it against a file of user-ID's and passwords.The user has only three")
    print("attempt to get his/her user-ID's and passwords.")
    print()
    return intro

#Get user information
def getInput():
    userID = input ("please enter your user-ID: ")
    passW = input ("Please enter your user password: ")
    print()
    return userID,passW


def verify(userID,passW):    
#Open file containing the user-ID and password
    file = open("unames_passwords.txt", "r")
    try :
         for userpass in file:
             name,passw = userpass.split()
             if name == userID and passw == passW:
                 return True
         else:
             return False
    except (ValueError,TypeError,NameError):
        return False

        

def main():
    intro()
    attempt = 0
    while attempt < 4 :
        userID,passW = getInput()
        attempt += 1
        authentication = verify(userID,passW)
        if authentication:
            print("Your user-ID and Password is recognisable in our directory")
            sys.exit()
        else:
            print("Invalid user-ID or password.Please try again")
            if attempt == 3 :
                print("Authentication failed. Your userID and password is unrecognisable in our system directory")
                sys.exit()
                 
            
main()
        
"""        
This program asks the user for his/her user-ID and password and runs 
it against a file of user-ID's and passwords.The user has only three
attempt to get his/her user-ID's and passwords.

please enter your user-ID: raymond
Please enter your user password: nash

Invalid user-ID or password.Please try again
please enter your user-ID: filarin 
Please enter your user password: quaks

Invalid user-ID or password.Please try again
please enter your user-ID: jdoe
Please enter your user password: mutt

Your user-ID and Password is recognisable in our directory    




"""
