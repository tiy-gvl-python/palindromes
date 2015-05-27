import re

prompt = input("enter text to test for a palindrome ")

palindrometext = re.sub(r'[^A-Za-z]', '' ,prompt)
false = "not a palindrome"
true = "is a palindrome"

def palindrome_checker(palindrometext, false, true):
    if str.lower(palindrometext) != str.lower(palindrometext[::-1]):
        return false
    else:
        return true

if palindrome_checker(palindrometext, false, true) != true:
    print("is not a palindrome")
else:
    print("is a palindrome")
