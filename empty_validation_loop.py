#loop until something is entered
while True:
    value = input("Enter something. Cannot be nothing!")
    #if after removing extra spaces, there is still text, then stop looping
    if value.strip():    
        break

#a variable that has a value will evalute to True in a condition. Otherwise it will evaluate to false
