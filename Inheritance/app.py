from animals import Animal, Dog

def main():
    dog = Dog("Rover","Brown",4,"Schnoodle")
    cat = Animal("Fluffy","Black",3)
    bird = Animal("Buddy","green",2)

    #create a list of the animals
    animals = [dog,cat,bird]

    #Loop through the list and display each animals name, color, num_legs and call make_a_noise(), move(), and eat() for each animal
    
    #Name:
    #Color:
    #Number of Legs:
    #method calls

    for animal in animals:
        print("--------")
        print(animal)
        animal.make_a_noise()
        animal.move()
        animal.eat()
        #check to see if animal is a dog(Dog) that has a chase_car()
        if isinstance(animal,Dog):
            animal.chase_car()

if __name__ == "__main__":
    main()