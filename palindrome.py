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
    string_ = re.sub(r'[^A-Za-z]','',string_)
    print_string(string_)
    string_ = string_.lower()
    print_string(string_)
    return string_

def palindrome_check(string_):
    print_string(string_[::-1])
    return string_ == string_[::-1]

def palindrome_check_iterative(string_):
    for index, letter in enumerate(string_[::-1]):
        if letter == string_[index]:
            continue
        return False
    return True

# Get user input.
potential_palindrome_input = input("Enter a string > ")
print_string(potential_palindrome_input)

if not potential_palindrome_input:
    print ("You didn't enter anything.")
    exit()

# Remove spaces, punctuation, and capitalization from the input
potential_palindrome = reformat(potential_palindrome_input)

# Algorithm
is_a_palindrome = palindrome_check_recursive(potential_palindrome)
is_a_palindrome = palindrome_check(potential_palindrome)
is_a_palindrome = palindrome_check_iterative(potential_palindrome)

if is_a_palindrome:
    print("{} is a palindrome.".format(potential_palindrome_input))
else:
    print("{} is not a palindrome.".format(potential_palindrome))
