import random
import pandas as pd

# for loops

for x in range(0,10):
    print(x,'',end="")

    print('\n')


grocery_list=['Juice', 'Tomaoes', 'Potatoes', 'Bananas']

for y in grocery_list:

    print(y)

for x in [2,4,6,8,10]:
    print(x)


num_list=[[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# while loops

random_num=random.randrange(0,100)

while(random_num!=15):
    print(random_num)
    random_num=random.randrange(0,100)

i=0

######################################
##############Exiting a loop ############

while(i<=20):
    if(i%2==0):
        print(i)
    elif(i==9):
        break
    else:
        i +=1 # i=i+1
        continue

    i+=1

########################################

# Create new DF...using a dictionary
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2011, 2012, 2013, 2014, 2015], 
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])


# Iterating over dataframe rows
for x in range(len(df.index)):
    print(df['year'].iloc[x])