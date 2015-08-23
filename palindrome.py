import re

text = input("Your text: ")
regex_text = re.sub(r'[^A-Za-z\s]', "", text).lower()
backward_text = regex_text[::-1]
empty_list = []
text_length = len(regex_text)
for i in range(text_length):
    if backward_text[i] == regex_text[i]:
        empty_list.append(1)
    else:
        empty_list.append(0)

if 0 in empty_list:
    print("is not a palindrome")
else:
    print("is a palindrome")
