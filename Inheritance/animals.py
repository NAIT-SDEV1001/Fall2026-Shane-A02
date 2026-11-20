#create an Animal class with name, color, num_legs attributes
#code the constructor

class Animal:
    def __init__(self, name:str, color:str, num_legs:int)->None:            
        self.name = name
        self.color = color
        self.num_legs = num_legs
    #override __str__ to return:
    # Name: name 
    # Color: color
    # Number of Legs: num_legs 

    def __str__(self)->str:
        return (
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Number of Legs: {self.num_legs}\n"
        )
    def eat(self)->None:
        print(f"{self.name} starts eating. Yum Yum")

    def make_a_noise(self)->None:
        print(f"{self.name} makes an interesting noise....")

    def move(self)->None:
        print(f"{self.name} moves around")


#Dog class which inherits from Animal
class Dog(Animal):
    def __init__(self,name:str,color:str, num_legs:int, breed:str)->None:
        #super() refers to the Parent class(Animal)
        #call the construtor from the Parent(Animal)
        super().__init__(name,color,num_legs)
        self.breed = breed
    #override the __str__ from the parent (Animal) to include breed
    def __str__(self)->str:
        return_string = super().__str__()#get the string from the parent __str__
        return_string += f"Breed: {self.breed}\n"#add on to it the additional string
        return return_string

    #Dog specific method
    def chase_car(self)-> None:
        print(f"{self.name} chases a car")

    #Override make_a_noise() for dog
    def make_a_noise(self)->None:
        print(f"{self.name} starts barking! Woof Woof!")     

class Cat(Animal):
    def __init__(self, name: str,color: str, num_legs: int, pattern: str, anger_level: int) -> None:
        super().__init__(name,color, num_legs)
        self.pattern = pattern
        self.anger_level = anger_level
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"            
            f"Pattern: {self.pattern}\n"
            f"Anger Level: {self.anger_level}"
        )
    def make_a_noise(self)->None:
        if self.anger_level < 10:
            print("Purr purr")
        elif self.anger_level <= 20:
            print("Meow meow")
        else:
            print("Hiss!")

    def knock_things_off_ledge(self) -> None:
        print(f"{self.name} knocks things off a ledge!")

class Bird(Animal):
    def __init__(self, name: str, color: str, num_legs: int, wingspan: float) -> None:
         super().__init__(name,color, num_legs)
         self.wingspan = wingspan

    def __str__(self) -> str:
        return f"{super().__str__()}Wingspan: {self.wingspan}"    

    def eat(self) -> None:
        print(f"{self.name} pecks at the food.")

    def move(self) -> None:
        print(f"{self.name} flies around!")

    def make_a_noise(self) -> None:
        print("I want crackers")
    
#Testing
def main():
    animal1 = Animal("Patrick","Blue",2)
    print(animal1)
    animal1.eat()
    animal1.make_a_noise()
    animal1.move()
    dog1 = Dog("Judas","lime green",4,"Golden Retriever")
    print(dog1)
    dog1.make_a_noise()

if __name__ == "__main__":
    main()