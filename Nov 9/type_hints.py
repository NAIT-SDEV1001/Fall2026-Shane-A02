#type hints describe what datatypes are expected for parameters and return values
#they are documentation only

def greet (name: str)->str:
    return f'Hello {name}'

def shout(name: str)-> None:
    print (f'HEY {name.upper()}!')

def shoutShane(name: str) -> str | None:
    if name == 'Shane':
        return f'HEY {name.upper()}!'
    else:
        return None


