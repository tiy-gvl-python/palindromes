# Functions

# Takes a string and returns True if the string is a palindrome.
def palindrome_check(string_):
    if len(string_) < 2:
        return True
    if string_.endswith(string_[0]):
        return palindrome_check(string_[1:-1])
    return False



# Get user input.

# Remove spaces, punctuation, and capitalization from the input

# Algorithm
    # Check to see if first and last characters are the same
        # If they are, continue
        # If they aren't, break
