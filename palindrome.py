import re


# Functions

# Prints string_
def print_string(string_):
    print("Current string: {}".format(string_))

# Takes a string and returns True if the string is a palindrome.
def palindrome_check_recursive(string_):
    print_string(string_)
    if len(string_) < 2:
        return True
    if string_.endswith(string_[0]):
        return palindrome_check_recursive(string_[1:-1])
    return False

# Takes a string and returns all of the letters in lower case.
def reformat(string_):
    print_string(string_)
    string_ = re.sub(r'[^A-Za-z]','',string_)
    print_string(string_)
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
print_string(potential_palindrome)
is_a_palindrome = palindrome_check_recursive(potential_palindrome)

if is_a_palindrome:
    print("{} is a palindrome.".format(potential_palindrome_input))
else:
    print("{} is not a palindrome.".format(potential_palindrome))
