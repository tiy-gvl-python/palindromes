
palindrome = input("What's your palindrome? ")


def check_palindrome(palindrome):
    # for letter in palindrome:
    punc = ['.', ',', ':', ';', "'", "_", "!"]
    for punc_remove in punc:
        palindrome = palindrome.replace(punc_remove, '')
    palindrome = palindrome.lower()
    palindrome_reverse = palindrome[::-1]
    palindrome_reverse = palindrome_reverse.replace(' ', '')
    palindrome = palindrome.replace(' ', '')
    if palindrome == palindrome_reverse:
        print("is a palindrome")
        print(palindrome)
        print(palindrome_reverse)
    else:
        print(palindrome)
        print(palindrome_reverse)
        print("is not a palindrome")

check_palindrome(palindrome)
