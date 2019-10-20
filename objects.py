# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:30:39 2018

@author: patemi
"""

#https://www.tutorialspoint.com/python/python_classes_objects.htm


class MyObj(object):
    
    
  
    address=''
    def __init__(self):
        self.name = 'Chuck Norris'
        self.phone = '+6661'

obj = MyObj()

# Accessing Object variables
print(obj.name)
print(obj.address)

print(dir(obj))
print(obj.__dict__)


# Delete property of an object
del obj.name

# Delete object
del obj


##########################################

# Collection of objects (as list)


class MyClass(object):
    def __init__(self, number):
        self.number = number

my_objects=[]

for i in range(10):
    my_objects.append(MyClass(i))

# later

for obj in my_objects:
    print(obj.number)
    
########################################


##########################################################

# Class variables vs Instance variables

#Generally speaking, instance variables are for data unique to each instance and class variables 
#are for attributes and methods shared by all instances of the class:    

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs

class Dog2:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

