# *args allows the function to accept a variable number of arguments
# Python collects the arguments into a tuple (often called *args)

def print_numbers (*args):
    #Loop through the tuple (holding the arguments) 
    for number in args:
        print(number)

print_numbers(1,2,3)
print_numbers(100,200)

# Question 1 Snack roll call
# Write display_snacks(*snacks). Print each snack on its own line, starting with a dash. Then print the number of
# snacks. If no snacks are supplied, print only "No snacks packed!". Use a loop and len()

def display_snacks(*snacks):
    if len(snacks) == 0:
        print("no snacks packed")
    else:
        for snack in snacks:
            print(f"- {snack}")
        print(f"Snack count: {len(snacks)}")    

display_snacks ()