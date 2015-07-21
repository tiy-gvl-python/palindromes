# Check for Palindrome
import re

pal_input = input("Enter any word or sentence (using quotes) to see if it is a Palindrome.  ")
print(pal_input)
pal_input = re.sub(r'[^A-Za-z]', "", pal_input.lower())
print(pal_input)
rev_input = pal_input[::-1]
print(rev_input)


def palindrome_check(pal_input, rev_input):
    if pal_input == rev_input:
        print("Yes. Your text is a palindrome.")
    else:
        print("Nope.  That text is not a palindrome.")

palindrome_check(pal_input, rev_input)
