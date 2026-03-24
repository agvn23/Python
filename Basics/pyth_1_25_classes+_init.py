### Classes ###

class Car:
    # The __init__ method initializes a new Car object with given attributes
    def __init__(self, make, color):
        self.make = make    # Property: make of the car
        self.color = color    # Property: color of the car
        self.speed = 0        # Default speed property
    
    # Method to simulate accelerating the car
    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.color} {self.make} accelerates to {self.speed} mph.")
    
    # Method to simulate braking the car
    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        print(f"The {self.color} {self.make} slows down to {self.speed} mph.")
    
    # Method to display the car's current status
    def status(self):
        print(f"{self.color.capitalize()} {self.make} is moving at {self.speed} mph.")

# Creating an object (instance) of the Car class
my_car = Car(make="Toyota", color="red")

# Accessing object properties and methods
my_car.status()           # Display initial status
my_car.accelerate(30)     # Increase speed
my_car.brake(10)          # Decrease speed
my_car.status()           # Display updated status

print(type(my_car))

### __init__ is a special method in Python classes, called when an object is created. 
# It is used to initialize the object's attributes. 
# The __init__ method takes at least one parameter, self, which refers to the instance 
# being created, and can take additional parameters to set up the object's properties.

# Class representing a person with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Class representing a rectangle with width and height
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Class representing a dog with a name and a breed, with a default breed value
class Dog:
    def __init__(self, name, breed="Unknown"):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Class representing a book with title, author, and year
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def summary(self):
        print(f"'{self.title}' by {self.author}, published in {self.year}.")

# Creating instances and using their methods
alice = Person("Alice", 30)
alice.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.

reagan = Person("Reagan", 42)
reagan.introduce() # Output: Hi, I'm Reagan and I'm 42 years old.

rect = Rectangle(5, 10)
print("Rectangle area:", rect.area())  # Output: Rectangle area: 50

dog1 = Dog("Buddy")
dog2 = Dog("Max", breed="Labrador")
dog1.bark()  # Output: Buddy says woof!
dog2.bark()  # Output: Max says woof!

book1 = Book("1984", "George Orwell", 1949)
book1.summary()  # Output: '1984' by George Orwell, published in 1949.


book2 = Book("The Hobbit", "John Ronald Reuel Tolkien", 1937)
book2.summary()  # Output: 'The Hobbit' by John Ronald Reuel Tolkien, published in 1937.