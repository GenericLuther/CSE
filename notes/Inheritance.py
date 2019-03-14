
#  field, method


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, mileage):
        super(Car, self).__init__(name)
        self.engine_statue = False
        self.fuel = 100
        self.mileage = mileage

    def start_engine(self):
        self.engine_statue = True
        print("You have turned on the car.")

    def move_forward(self):
        if self.engine_statue is True:
            self.fuel -= 1
            print("The car moves forward.")
        else:
            print("You're car is off")

    def turn_left(self):
        self.fuel -= 1
        print("The car turns left.")

    def turn_off(self):
        self.engine_statue = False
        print("You turn off the engine.")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__('Impala', 25)


class KeylessCar(Car):
    def __init__(self, name, mileage):
        super(KeylessCar, self).__init__(name, mileage)

    def start_engine(self):
        self.engine_statue = True
        print("You push the button and the car turns on")


wiebe_car = KeylessCar("Tesla", 125)


jacob_car = Impala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_off()

class Character(object):
    def __init__(self, name, health, weapon, clothes):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.clothes = clothes

