#Object oriented Progamming (OOP)
#Technique of using classes to model real world things
#A class is a blueprint to create/instantiate objects from
#Each object will have it's own copy of attributs and methods from the class

class Car:

#constructor method
#a method called __init__ that executes when you instantiate an object
#self refers the object using this method

    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0

    #Methods provide behaviour for an object
    def Honk(self):
        print (f'{self.make}, {self.model} says Beep Beep')

    def Accelerate(self, amount):
        self._speed += amount

    def Decelerate(self, amount):
        self._speed -= amount

    #override the __str__() to return a usefull string when we print an object
    def __str__(self):
        return f'This {self.year} {self.make} {self.model} is travelling {self._speed} km/h'

    def __repr__(self):
        return f'Car({self.make},{self.model},{self.year})'

def main():
    #instantiate a new car called car1
    car1 = Car('Ford','F150',2020)
    car2 = Car('Mazda','3',2017)
    car3 = Car('Mercedes','SmartCar',2010)

    print(car1.model)
    print(car2.model)

    #change attribute values
    car2.model = 6
    print(car2.model)

    #in Python you can add attributes to objects
    car3.seats = 2
    print(car3.seats)

    #Test a method
    car1.Honk()
    car2.Honk()

    #accelerate
    print(f'current speed: {car1._speed}')
    car1.Accelerate(40)
    print(f'current speed: {car1._speed}')
    car1.Accelerate(100)
    print(f'current speed: {car1._speed}')

    #what happen if you print an object?
    #calls __str__() which converts the object into a string
    # containing its memory location. Useless
    #After overriding __str__() we get
   
    print(car1)#__str__
    print(repr(car1))#__repr__
    
if __name__ =='__main__':
    main()

