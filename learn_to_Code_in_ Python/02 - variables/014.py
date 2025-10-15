'''
Math With Strings

When working with strings the + operator performs a "concatenation", which is a fancy word that means "joining two strings". Generally speaking, it's better to use string interpolation with f-strings over + concatenation.

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"

full_name now holds the value "Lane Wagner".

Notice the extra space at the end of "Lane " in the first_name variable. That extra space is there to separate the words in the final result: "Lane Wagner".

'''

'''
Assignment

We have a second player in our game!

We need to tell each of our players how much health they have left.

"Only print "You have x health" once for each player, nothing else."

'''

'''
CODE

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print()
print()

'''

#Resolution

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(f"You have {player1_health} health")
print(f"You have {player2_health} health")
