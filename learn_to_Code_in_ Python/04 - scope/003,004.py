'''
Scope Quiz

pi = 3.14

def get_area_of_circle(radius):
    area = pi * radius * radius
    return area

'''

'''
1 - Does the get_area_of_circle function have access to the pi variable?

2 - Can the area variable inside the get_area_of_circle function be accessed outside of the function?
'''

#Resolution

#1 - Yes, becouse the pi variable is in the global scope

#2 - No, variables defined inside a function are not accessible outside of it