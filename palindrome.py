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
        return palindrome_check(string_[1:-1])
    print("First and last characters are different.")
    return False

# Takes a string and returns all of the letters in lower case.
def reformat(string_):
    string_ = re.sub(r'[^A-Za-z]','',string_)
    string_ = string_.lower()
    return string_


# Get user input.

# Remove spaces, punctuation, and capitalization from the input

# Algorithm
    # Check to see if first and last characters are the same
        # If they are, continue
        # If they aren't, break
