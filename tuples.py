#same as a list but cannot change
#Create with () instead of []

#ask user for a month
#Display if it is a winter month

winter_months = ("December","January", "February")
user_month = input("Enter a month: ")
if user_month in winter_months:
    print("Winter")
else:
    print("Not Winter")

#unpacking a tuple/list
first_name,last_name = ("Shane","Bell")
print (f"Hello {first_name} {last_name}")

#list of tuples
movie_character = [("R2","D2"),("Darth","Vader"),("Bobba","Fett")]
print(movie_character)

#ask the user for an index and disply the first and lastname of that character
character_index = int(input("Enter an index to display: "))
print(f"The character at index {character_index} is {movie_character[character_index][0]}  {movie_character[character_index][1]}")

