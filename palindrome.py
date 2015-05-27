import re


# Functions

# Takes a string and returns True if the string is a palindrome.
def palindrome_check_recursive(string_):
    print("Checking remaining length.")
    if len(string_) < 2:
        print("Remaining string is less than 2 characters.")
        return True
    print("Remaining string is {}.".format(string_))
    print("Comparing first and last characters.")
    if string_.endswith(string_[0]):
        print("First and last characters are the same.")
        print("Stripping first and last characters from the string.")
        return palindrome_check_recursive(string_[1:-1])
    print("First and last characters are different.")
    return False

# Takes a string and returns all of the letters in lower case.
def reformat(string_):
    print("Removing all non-letters.")
    string_ = re.sub(r'[^A-Za-z]','',string_)
    print("Making string lower case.")
    string_ = string_.lower()
    return string_


# Get user input.
potential_palindrome_input = input("Enter a string > ")

if not potential_palindrome_input:
    print ("You didn't enter anything.")
    exit()

# Remove spaces, punctuation, and capitalization from the input
potential_palindrome = reformat(potential_palindrome_input)

# Algorithm
    # Compare first and last letter.
    # If they are the same, then compare next letters
print("Checking to see if you entered a palindrome.")
is_a_palindrome = palindrome_check_recursive(potential_palindrome)

if is_a_palindrome:
    print("{} is a palindrome.".format(potential_palindrome_input))
else:
    print("{} is not a palindrome.".format(potential_palindrome))
