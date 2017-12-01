#CSI 31 KINGSLEY OTTO CAESAR CIPHER.PY
#THIS PROGRAM ENCODE AND DECODE MESSAGES USING CAESAR CIPHER

def intro ():
    print("This program encode and decode messages.\n")
    return intro

# Get the message to encode
def main():
    intro()
    message = input ("Please enter the message you wish to encode: ")
    key = eval(input("Enter a shit key from 1-26: "))
    encode =[]
    for ch in message:
        encode.append(ord(ch))
    print(encode)
        
    decode = ""
    for numstr in encode:
        decode = decode + chr(numstr)
    print ("\nThe decoded message is:",decode)
main()


"""
This program encode and decode messages.

Please enter the message you wish to encode: hello bob!
Enter a shit key from 1-26: 4
[104, 101, 108, 108, 111, 32, 98, 111, 98, 33]

The decoded message is: hello bob!
"""
