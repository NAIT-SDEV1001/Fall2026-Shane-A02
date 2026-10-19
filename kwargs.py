# **kwarg accepts any number of keyword arguments(name = value)
# Python collect them into a dictionary

def print_settings(**kwargs):

    for key, value in kwargs.items():    
        print(f"{key}: {value}")

print_settings(theme = "dark", font = "arial", size = 12)