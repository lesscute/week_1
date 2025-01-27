

#%%
# These are helper functions for the below script
# you do not need to do anything with this and we will cover functions later!
#   
# Please scroll down to the 
# READING BEGINS HERE comment


def displayValues(name,age,height,is_student):

    # Print the variables and their types
    print("Name:", name, " | Type:", type(name))
    print("Age:", age, " | Type:", type(age))
    print("Height:", height, " | Type:", type(height))
    print("Is Student:", is_student, " | Type:", type(is_student))



def dataCheck(name,age,height,is_student):

    message = None

    if not isinstance(name,str):
        message = 'name is not a string'

    if not isinstance(age,int):
        message = 'age is not an int'

    if not isinstance(height,float):
        message = 'height is not a float'

    if not isinstance(is_student,bool):
        message = 'is_student is not a boolean'
    
    return message






##### READING BEGINS HERE #####


#%%
# Declare global variables with different data types

name = "Alice"           # String
age = 25                 # Integer
height = 5.5             # Float
is_student = False        # Boolean


# call function to display to screen
displayValues(name,age,height,is_student)


# %%
# Variable Manipulation

##### ASSIGNMENT STARTS HERE #####

'''
Because these are variables, we can modify their values!

Please enter in whatever values you'd like to display. 

What does it output?

They can be real or fake, it does not matter!

That said - what happens when you input the same values?

ASSIGNMENT GOAL:
- Make "Variable Manipulation" cell output types match first cell


'''
def displayValues(name,age,height,is_student):
    print(f"Name : {name}")
    print(f"Age: {age}")
    print(f"Height: {height} ft")
    print(f"Students: {'Yes' if is_student else 'no'}")

name = input('Please enter a name: ')
age = int(input('Please enter an age: '))
height = float(input('Please enter a height: '))
is_student = bool(input('Please enter whether or not you are a student (yes/no): ').lower)

displayValues(name, age, height, is_student)
##### ASSIGNMENT ENDS HERE #####
#I researched this and also tried my best but I don't know if I did it correctly
#AI assisted 

#%%
# Run this cell when you're ready to check your data!
message = dataCheck(name,age,height,is_student)

if message == None:
    print('Data types check out - well done!')
    print('Assignment Complete')

else:
    print(message)
