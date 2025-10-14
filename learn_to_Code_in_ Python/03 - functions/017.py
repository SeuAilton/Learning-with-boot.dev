'''
Default Values

In Python you can specify a default value for a function argument. It's nice for when a function has arguments that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.

A default value is created by using the assignment (=) operator in the function signature.

def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

get_greeting("lane@example.com", "Lane")
# Hello Lane welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there welcome! You've registered your email: lane@example.com

If the second parameter is omitted, the default "there" value will be used in its place. As you may have guessed, for this structure to work, optional arguments (the ones with defaults) must come after all required arguments.

'''

'''
Assignment

Complete the get_punched and get_slashed functions. They both take 2 integers as arguments, health and armor.

  *Complete the get_punched function:
    1 - Change the armor parameter to have a default value of 0
    2 - Create a damage variable equal to 50 minus the armor. (The armor reduces the damage.)
    3 - Create a new_health variable equal to the input health minus damage - we apply the damage
    4 - Return new_health

  *Complete the get_slashed function
    1 - Change the armor parameter to have a default value of 0
    2 - Create a damage variable equal to 100 minus the armor
    3 - Create a new_health variable equal to the input health minus damage
    4 - Return new_health

'''

'''
CODE

def get_punched(health, armor):
    # ?


def get_slashed(health, armor):
    # ?


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)

'''

#Resolution

def get_punched(health, armor = 0):
    damage = 50 - armor
    new_health = health - damage
    return new_health

def get_slashed(health, armor = 0):
    damage = 100 - armor
    new_health = health - damage
    return new_health

# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)
