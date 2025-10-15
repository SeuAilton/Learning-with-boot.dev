'''
Boots Interview

blá, blá, blá...

(site AI stuff)

'''

'''
Assignment

The calculate_damage function is called 3 times in the example. When the total is returned, which variables are used to store it?

'''

'''
CODE

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total


first_damage = calculate_damage(10, 20, 30)
second_damage = calculate_damage(5, 10, 15)
third_damage = calculate_damage(50, 60, 70)
print(first_damage)
print(second_damage)
print(third_damage)

'''

#Resolution

#first_damage, second_damage, third_damage
