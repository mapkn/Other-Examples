# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:03:44 2018

@author: patemi
"""

import re

line = "Cats are smarter than dogs"

# https://docs.python.org/3/howto/regex.html
# https://www.tutorialspoint.com/python/python_reg_expressions.htm


# Match function, Returns a corresponding match object if zero or more characters at the beginning of 
# string match the pattern. Else it returns None, if the string does not match the given pattern


# r , the raw string literal
if re.match(r'Cat',line):
    print("Match")
else:
    print("No match")


#the search() function checks for a match anywhere in the string.


# \s - Matches a single whitespace character like: space, newline, tab, return

match2=re.search(r'Eat\scake', 'Eat cake')
if match2:
    print(match2.group())


# \w - Lowercase w. Matches any single letter, digit or underscore.
print(re.search(r'Co\wk\we', 'Cookie').group())


# \W - Uppercase w. Matches any character not part of \w (lowercase w).
print(re.search(r'C\Wke', 'C@ke').group())


# \d - Lowercase d. Matches decimal digit 0-9.
print(re.search(r'c\d\dkie', 'c00kie').group())




#The group() function returns the string matched by the re
#A period. Matches any single character except newline character







# Parts of a regular expression pattern bounded by parenthesis() are called groups
# The parenthesis does not change what the expression matches, but rather forms groups 
# within the matched sequence
email_address = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
if match:
  print(match.group()) # The whole matched text
  print(match.group(1)) # The username (group 1) 
  print(match.group(2)) # The host (group 2)