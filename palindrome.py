
import re
string = input("Write a phrase, word or sentence")
def palin_drome(string):
  response = str.lower(string)
  response = re.sub(r'[A-Za-z]',"", response)

  print(response[::-1])
  if response == response[::-1]:
    print("{} is a palindome".format(string))
  else:
    print("{} is not a palindome".format(string))
palin_drome(string)
