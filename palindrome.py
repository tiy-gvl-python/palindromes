import re

print("I am a program that determines if a word or phrase is a palindrome.")


initial = input("\nType your word or phrase here: ")

def phrase(initial):
# save initial input for the output so that sentences dont appear jumbled
    phrase = initial

    # change all letters to lowercase in string
    phrase = phrase.lower()

    # ignore all special characters and numbers
    phrase = re.sub('[0-9]+[\c]','',phrase)

    # remove spaces in string
    phrase = phrase.replace(' ','')
    return(phrase)




def forward_equals_backward(phrase):
    # take the altered string and reverses it
    b = phrase[::-1]
    if phrase == '':
        print("Invalid argument please enter a word or a phrase")
    elif phrase == b:
        print("\n{}".format(initial) + " is a palindrome")
    else:
        print("\n{}".format(initial) + " is not a palindrome")

forward_equals_backward(initial)
