
#CSI_31_KINGSLEY OTTO WORD_COUNT.PY
#THIS_PROGRAM_COUNT_THE_NUMBER_OF_WORDS,LINES AND CHARACTERS_IN_A_FILE


def intro():
    print("This program counts the number of words,lines and characters in a file\n")
    

def main():
    intro()
    filename = input("Please enter the file name: ")
    file = open(filename)
    fileread = file.read()
    filesplit = fileread.split()
    # for number of words
    words =len(filesplit)
    print("The number of words in",filename,"is",words,"\n")
    
    # for number of lines
    file = open(filename)
    numlines = 0
    for lines in file:
        numlines= numlines + 1
    print("The number of lines in",filename,"is",numlines,"\n")
    
    # for number of characters
    print("The number of characters in",filename,"is",len(fileread))
    
    
        
    


main()

"""
This program counts the number of words,lines and characters in a file

Please enter the file name: colour.txt
The number of words in colour.txt is 25 

The number of lines in colour.txt is 6 

The number of characters in colour.txt is 164
"""

    
