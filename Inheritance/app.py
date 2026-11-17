from animals import Animal, Dog

def main():
    dog = Dog("Roger","Brown",4,"Poodle")
    cat = Animal("Fluffy","Black",4)
    bird = Animal("Buddy","Green",2)

    #create a list of our animals
    animals = [dog,cat,bird]

    #loop through the animals and have them all make a noise, move and eat
    for animal in animals:
        print("-----------------")
        print(animal)

        animal.make_a_noise()
        animal.move()
        animal.eat()
        #check to see if the animal is a dog so the chase_car method can be used
        if isinstance(animal,Dog):
            animal.chase_car()

if __name__ == '__main__':
    main()