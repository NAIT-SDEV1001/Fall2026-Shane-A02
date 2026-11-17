class Animal:
    def __init__(self, name:str, color:str, num_legs:int)->None:
        self.name = name 
        self.color = color
        self.num_legs = num_legs

    def __str__(self)->str:
        return (
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Number of Legs: {self.num_legs}\n"
        )

    def __repr__(self) ->str:
        return f"Animal(name = {self.name!r}, color =  {self.color!r}, num_legs = {self.num_legs})"  

    def eat(self)->None:        
        print(f"{self.name} starts eating, yum yum yum")

    def make_a_noise(self)->None:
        print(f"{self.name} makes an interesting noise")

    def move(self)->None:
        print(f"{self.name} runs around!")


    #Create a dog class that will inherit all the attributes/methods from the animal class
class Dog(Animal):
    def __init__(self, name:str, color:str, num_legs:int, breed:str)->None:
        #use the attributes from Animal
        super().__init__(name, color, num_legs)#share these attributes from the Animal class
        # self.name = name 
        # self.color = color
        # self.num_legs = num_legs
        self.breed = breed

    def __str__(self)->str:
        #call the __str__ from Animal to get name, color, num_legs
        return_string = super().__str__()
        #append the breed attribute of the dog
        return_string += f"Breed:{self.breed}\n"
        #return the updated string
        return return_string

    def make_a_noise(self)->None:
        print(f"{self.name} starts barking loudly! Bark Bark!")

    def chase_car(self)-> None:
        print(f"{self.name} chases after the car!")

    


