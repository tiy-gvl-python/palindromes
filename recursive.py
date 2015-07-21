# Palindrome homework
pal_input = input("Enter any word or sentence to see if it is a Palindrome.  ")
print(pal_input)
pal_input = re.sub(r'[^A-Za-z]', "", pal_input.lower())
print(pal_input)
rev_input = pal_input[::-1]
print(rev_input)

#def comparison(pal_input, rev_input):
count = len(pal_input)

print(pal_input[(count)])
print(count)
    
#    print("Yes. Your text " + "is a palindrome.")
#else:
#    print("Nope.  That text " + "is not a palindrome.")
