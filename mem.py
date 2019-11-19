# The beginning of a tool that can be used to split strings.

import random
import re

wordlist = ['1=one', '2=two', '3=three', '4=four',]

def seperate_wordlist(wordlist):
  string = re.split("=", random.choice(wordlist))
  return string

word = seperate_wordlist(wordlist)[0]
value = seperate_wordlist(wordlist)[1]
string = seperate_wordlist(wordlist)

print(word)
print(value)
print(string) 
