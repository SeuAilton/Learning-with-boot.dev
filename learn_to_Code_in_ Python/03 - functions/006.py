'''
Where to Declare Functions

You've probably noticed that a variable needs to be declared before it's used. For example, the following doesn't work:

print(my_name)
my_name = 'Lane Wagner'
# NameError: 'my_name' is not defined

It needs to be:

my_name = 'Lane Wagner'
print(my_name)
# Lane Wagner

Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after it has been defined.

'''

'''
Assignment

There's a bug! It looks like we are trying to call a function before it was defined! Run the code and read the printed error, then fix it.

'''

'''
CODE

main()

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

'''

#Resolution

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")
main()