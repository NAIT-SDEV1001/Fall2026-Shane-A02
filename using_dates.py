from datetime import datetime

#date as a string
my_birthday = "01/20/72"

#read the string date into a datetime object
my_birthday_dateTime_object = datetime.strptime(my_birthday,"%m/%d/%y").date()

#print the object
print(my_birthday_dateTime_object)

#back to a string
my_birthday_string = my_birthday_dateTime_object.strftime("%m/%d/%Y")

print(my_birthday_string)
print(my_birthday_dateTime_object.strftime("%A"))

# %m	Month number	11
# %d	Day of the month	18
# %y	Two-digit year	26
# %Y	Four-digit year	2026
# %b	Abbreviated month name	Nov
# %B	Full month name	November
# %a	Abbreviated weekday name	Wed
# %A	Full weekday name	Wednesday


