#Same as a list but cannot change
#created with () instead of []

#ask for a month and display if it is a winter month
# winter_months = ("November","December","January")
# month = input("Enter a month: ")

# if month in winter_months:
#     print("Winter Month")
# else:
#     print("Not a winter month")

# #unpacking
# first_name, last_name = ("Shane","Bell")
# print(f"Hello {first_name} {last_name}")

movie_characters = [("R2","D2"),("Ellen","Ripley"),("Harry","Potter")]
print(movie_characters)
index = int(input("Enter an index to display: "))
print(f"The character is: {movie_characters[index][0]} {movie_characters[index][1]}")