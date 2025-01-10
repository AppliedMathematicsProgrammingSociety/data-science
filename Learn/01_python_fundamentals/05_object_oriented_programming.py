# Object-Oriented Programming (OOP) with Car Brands

# Define a Car class (blueprint for car objects)
class Car:
    def __init__(self, brand, model, year, color):  # Constructor (__init__)
        """Initializes a Car object."""
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0  # Initial speed is 0

    def accelerate(self, increment):
        """Increases the car's speed."""
        self.speed += increment

    def brake(self, decrement):
        """Decreases the car's speed."""
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0 # Speed can't be negative

    def describe(self):
        """Prints a description of the car."""
        print(f"This is a {self.year} {self.color} {self.brand} {self.model} going at {self.speed} mph.")


# Create Car objects (instances of the Car class)
my_car = Car("Toyota", "Camry", 2023, "silver")
your_car = Car("Honda", "Civic", 2022, "blue")


# Access object attributes:
print(my_car.brand)  # Output: Toyota
print(your_car.year) # Output: 2022


# Call object methods:
my_car.accelerate(30)
my_car.describe()   # Output: This is a 2023 silver Toyota Camry going at 30 mph.

your_car.accelerate(50)
your_car.brake(20)
your_car.describe() # Output: This is a 2022 blue Honda Civic going at 30 mph.




# Inheritance (Creating specialized classes from a base class)

class SportsCar(Car): # Inherits from the Car class
    def __init__(self, brand, model, year, color, top_speed):
        """Initializes a SportsCar object."""
        super().__init__(brand, model, year, color) # Call the parent class's constructor
        self.top_speed = top_speed

    def describe(self):  # Method overriding (modifying a method inherited from the parent class)
        """Prints a description of the sports car."""
        print(f"This is a {self.year} {self.color} {self.brand} {self.model} with a top speed of {self.top_speed} mph, currently going at {self.speed} mph.")


my_sports_car = SportsCar("Porsche", "911", 2024, "red", 200)
my_sports_car.accelerate(150)
my_sports_car.describe() # Output: This is a 2024 red Porsche 911 with a top speed of 200 mph, currently going at 150 mph.




# Polymorphism (Objects of different classes can respond to the same method call in their own way)

cars = [my_car, your_car, my_sports_car] #  A list of different types of Car objects.

for car in cars:
    car.describe() # Each car object has its own describe() method (polymorphism)