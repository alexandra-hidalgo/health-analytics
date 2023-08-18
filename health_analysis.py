import pandas as pandas
import numpy as np 

#creating a number variable
temperature = 100.4
age = 30 

#creating a string variable
address = """791 sacco pl
north bellmore"""

#creating a list
cars = ['BMW', 'Mercedes', 'Toyota', 'Ford']

#creating a dictionary 
family = {
    "father": {
        'name': "michaelangelo",
        'nationality': 'ecuador',
        'hubbies': ['sing', 'dance', 'play']}, 
        'mother': {
        'name': 'alexandra',
        'nationality': 'colombia',
        'hubbies': ['read, excersice, shopping'
    ]}, 'son': {
        'name': 'michaelangelo',
        'nationality': 'usa',
        'hubbies': ['play', 'eat', 'sleep']}
        }

#functions 

def PeriodontalDisease (Pockets, Boneloss):
    # first, lets check pockets depths

    if Pockets >= 3:
        Pockets_output = 'Disease'
    else:
        Pockets_output = 'healthy'
     #now, lets check for Bone loss
    if Boneloss >= 4:
        Boneloss_output = 'Disease'
    else:
        Boneloss_output = 'healthy'
    output = [Pockets_output, Boneloss_output]
    return output

PocketsInput = 7
BonelossInput = 5

Function_output = PeriodontalDisease (PocketsInput, BonelossInput)

print('Pockets number:', PocketsInput)
print('Pockets interpretation:', Function_output[0])
print('Boneloss number:', BonelossInput)
print('Boneloss interpretation:', Function_output[1])












 


  




