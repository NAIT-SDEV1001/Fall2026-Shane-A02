#add 0.1 + 0.2
answer = 0.1 + 0.2
print(answer)
# prints 0.30000000000000004
#Issue is some decimal values cannot be represented accurately in binary

print(round(answer,1))

amount = 1.15
print(f"calculate: {amount * 100}")
print(f"Convert to int: {int(amount * 100)}")
print(f"calculate: {round(amount * 100)}")