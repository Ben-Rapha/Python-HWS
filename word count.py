#CSI_31_KINGSLEY OTTO NUMBER_COUNT.PY
#THIS PROGRAM COUNT THE NUMBER OF WORDS IN A SENTENCE



def intro():
    print("This program count the number of words in a sentence.\n")

def main():
    intro()
    sentence = input ("Please enter a sentence: ")
    word = sentence.split()
    print("The number of words in",sentence,"is:",len(word))
    
main()

"""
Please enter a sentence: my love for mother nature is insane
The number of words in my love for mother nature is insane is: 7
"""
