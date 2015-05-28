import re

text = input("Your text: ")
regex_text = re.sub(r'[^A-Za-z]', "", text).lower()
bward_text = regex_text[::-1]
elist = []
etup = len(regex_text)
for i in range(etup):
    if bward_text[i] == regex_text[i]:
        elist.append(1)
    else:
        elist.append(0)
        
print(elist)

if 0 in elist:
    print("is not a palindrome")
else:
    print("is a palindrome")
