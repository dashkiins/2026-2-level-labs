"""
Programming 2026.

Seminar 11.

Inheritance.
"""

# pylint:disable=too-few-public-methods


class Vehicle:
    """
    Represents a general vehicle.

    Instance attributes:
        max_speed (int): The maximum speed of the vehicle.
        colour (str): The colour of the vehicle.

    Instance methods:
        move() -> None:
            Simulates vehicle movement.
    """
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour
    def move(self) -> None:
        print(f'Максимальная скорость: {self.max_speed}, цвет: {self.colour}')
v = Vehicle(50, 'red')
v.move()



class Car(Vehicle):
    """
    Represents a car, which is a type of vehicle.

    Instance attributes:
        max_speed (int): The maximum speed of the car.
        colour (str): The colour of the car.
        fuel (str): The type of fuel used by the car.

    Instance methods:
        move() -> None:
            Simulates car movement.
        stay() -> None:
            Simulates stopping the car.
    """
    def __init__(self, max_speed, colour, fuel):
        super().__init__(max_speed, colour)
        self.fuel = fuel
    def stay(self) -> None:
        print('Car has stopped')
c = Car(50, 'red', 'petrol')
c.move()
c.stay()



class Bicycle(Vehicle):
    """
    Represents a bicycle, which is a type of vehicle.

    Instance attributes:
        number_of_wheels (int): The number of wheels of the bicycle.
        colour (str): The colour of the bicycle.
        max_speed (int): The maximum speed of the bicycle.

    Instance methods:
        move() -> None:
            Simulates bicycle movement.
        freestyle() -> None:
            Simulates performing a freestyle trick.
    """
    def __init__(self, number_of_wheels, colour, max_speed):
        super().__init__(max_speed, colour)
        self.number_of_wheels = number_of_wheels
    def move(self) -> None:
        print('movement')
    def freestyle(self) -> None:
        print('bunny hop')
b = Bicycle(4, 'red', 25)
b.move()
b.freestyle()



class Aircraft(Vehicle):
    """
    Represents an aircraft, which is a type of vehicle.

    Instance attributes:
        number_of_engines (int): The number of engines of the aircraft.
        colour (str): The colour of the aircraft.
        max_speed (int): The maximum speed of the aircraft.

    Instance methods:
        move() -> None:
            Simulates aircraft movement.
    """
    def __init__(self, number_of_engines, colour, max_speed):
        super().__init__(max_speed, colour)
        self.number_of_engines = number_of_engines
    def move(self) -> None:
        print(f'Воздушное судно с {self.number_of_engines} двигателями {self.colour} цвета летает {self.max_speed} км.ч')
a = Aircraft(2, 'red', 60)
a.move()



def main() -> None:
    """
    Launch listing.
    """
    print("Created inheritance hierarchy: Vehicle -> Car, Bicycle, Aircraft")


if __name__ == "__main__":
    main()
