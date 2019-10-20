# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:04:12 2018

@author: patemi
"""


#Useful reference for regular expressions here: https://docs.python.org/3/howto/regex.html

# For regular expressions
import re


string='22360773.4091043,18606788.4459305,14863525.4679527,11131089.7262056,7409586.47172355,3699171.34836793,0,-3687927.57338023,-7364611.37177277,-11029899.4495286,-14683639.8609986,-18325734.9800496,-21956087.1805482'

string2='4898206.07972646,4076298.08322978,3256617.78598046,2439157.19649696,1623908.32329774,810859.734944761,0,-808670.881536543,-1615152.90966487,-2419456.86029756,-3221593.5093472,-4021569.41462517,-4819391.13394284'


############################### Convert String to list ###############################

# returns a list of strings after breaking the given string by the specified separator
y=string.split(",")


alternate = map(''.join, zip(y[::2], y[1::2]))

print(alternate)

y1=string2.split(",")



#The method join() returns a string in which the string elements of sequence have been joined by str separator.

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print(s.join( seq ))



Factor='Equity.[].[*].[AU].[*].[*].[*].[*]'


tst='abcd'

#x=re.findall('\[',Factor)
x=re.findall('\[(.*?)\]',Factor)


yy=Factor.split("[")


# Find the first occurrence
z=string.find('Int')


# Elements between "," and "r"
print(string[string.find(","):string.find("r")])


jacobian={}


list=[x for x in y if x[:3]!='Int']



# Zip functoin on strings

country_name = ['South Africa', 'India', 'United States']
country_code = ['ZA', 'IN', 'US']
x= zip(country_name, country_code) # zip returns an iterator of tuples
for item in x:
    print(item)


def left(aString, howMany):
    if howMany <1:
        return ''
    else:
        return aString[:howMany]

def right(aString, howMany):
    if howMany <1:
        return ''
    else:
        return aString[-howMany:]

def mid(aString, startChar, howMany):
    if howMany < 1:
        return ''
    else:
        return aString[startChar:startChar+howMany]

# Find n-th occurrence in a string
def find_nth(string, substring, n):
    if (n == 1):
       return string.find(substring)
    else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)


print(find_nth('foo bar bar bar','bar',3))

print('foo bar bar bar'.replace('bar', 'XXX', 0).find('bar'))

print(left(string,5))
print(right(string,5))


# Uppper / Lower case of a string
w='y'
print(w.upper())


y=' bb '
print(y.strip())


z='56,,'
print(z.index(','))


#for item in y[::-1]:
#    #print(item[:3])
#    
#    if item[:3]==':Ba':
#        jacobian[item]==
#        print(item)
#       # jacobian[item]
        
    
    #jacobian[i]
