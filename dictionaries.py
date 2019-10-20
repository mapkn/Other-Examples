# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:38:32 2018

@author: patemi
"""


#https://chrisalbon.com/python/basics/compare_two_dictionaries/

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict1 = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict2 = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict3 = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict4 = dict([(1,'apple'), (2,'ball')])


my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
#print(my_dict)


# add item to dictionary
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
#print(my_dict)


# How to check if the keys in two dictionaries are exactly the same
#print(set(my_dict1.keys()) == set(my_dict3.keys()))


# Retrieve an item from dictionary using given key
d=my_dict.get('address')



print(my_dict[1])



importers = {'El Salvador' : 1234,
             'Nicaragua' : 152,
             'Spain' : 252
            }

exporters = {'Spain' : 252,
             'Germany' : 251,
             'Italy' : 1563
             }

for key in my_dict:
    print (key, 'corresponds to', my_dict[key])


# Duplicate key
# Find the intersection of importers and exporters
print(importers.keys() & exporters.keys())

# Difference in keys
# Find the difference between importers and exporters
#y= dict(importers.keys() - exporters.keys())
print(importers.keys() - exporters.keys())

# Key, value pairs in common
# Find countries where the amount of exports matches the amount of imports
print(importers.items() & exporters.items())


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    print(added)
    print(removed)
    print(modified)
    print(same)
    return added, removed, modified, same

x = dict(Category='Equity', IssueCountry='AU', IssuerSector='Fin')
y = dict(Category='Equity', IssueCountry='*', IssuerSector='*')
added, removed, modified, same = dict_compare(x, y)



def check_diffs(d):
    # Input: dictionary of differences
    # Value will be a two element tuple
 #   l=[]
 #   for key in d:
 #       l[]
    
    list2=['T' for key in d if d[key][0]=='AU']
    #{TRUE for key,value in my_dict.items() if d[key]=='*'}
    return list2

    #list3=[x for x in list1 if x>0]    





# dicitonary of dictoinaries, adding to a dicitonary

FromAttributes={1:{'EquityCountry':'AU', 'IndexID':'*', 'IssueID':'*','IssuerCountry':'*','IssuerID':'*', 'IssuerIsLargeCap':'*', 'IssuerSector':'*'},
                2:{'EquityCountry':'NZ', 'IndexID':'*', 'IssueID':'*','IssuerCountry':'*','IssuerID':'*', 'IssuerIsLargeCap':'*', 'IssuerSector':'*'},
                3:{'EquityCountry':'*', 'IndexID':'*', 'IssueID':'*','IssuerCountry':'*','IssuerID':'*', 'IssuerIsLargeCap':'*', 'IssuerSector':'*'},}

# New dictionary
New = {'EquityCountry':'US', 'IndexID':'*', 'IssueID':'*','IssuerCountry':'*','IssuerID':'*', 'IssuerIsLargeCap':'*', 'IssuerSector':'*'}

# Add new dictionary to existing
FromAttributes[4]=New