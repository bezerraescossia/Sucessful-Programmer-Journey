from typing import Protocol, List


# Challenge 01
# Inside the editor, complete the following steps:
# 1. Create a class called Person
# 2. Add an __init__ method that takes name and age as parameters
# 3. Add a method called greet that prints "Hello, my name is " followed by the name
# 4. Create an object p1 of the class with name "John" and age 36
# 5. Call the greet method on p1

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}')

p1 = Person('John', 36)
p1.greet()

# Challenge 2
# Inside the editor, complete the following steps:
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

class DogClass:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says Woof!')
    
d1 = DogClass('Buddy', 3)
d1.bark()

# Challenge 3
# Inside the editor, complete the following steps:
# Create a class called Car
# Add an __init__ method with a brand parameter, and store it as a property
# Add a method called show that prints the brand
# Create an object c1 of the Car class with brand "Ford"
# Call the show method on c1

class Car:
    def __init__(self, brand: str):
        self.brand = brand

    def show(self):
        print(self.brand)
    
c1 = Car('Ford')
c1.show()

# Challenge 4
# Inside the editor, complete the following steps:
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student:
    def __init__(self, name: str, grade: str) -> None:
        self.name = name
        self.grade = grade

s1 = Student('Anna', 'A')
print(s1.grade)
s1.grade = 'B'
print(s1.grade)

# Challenge 5
# Inside the editor, complete the following steps:
# Create a class called Rectangle
# Add an __init__ method with width and height, and store them as properties
# Add a method called area that returns the width multiplied by the height
# Create an object r1 with width 5 and height 3
# Print the area of r1

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    
r1 = Rectangle(5, 3)
print(r1.area())

# Challenge 6
# Inside the editor, complete the following steps:
# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print(self.name)

class Dog(Animal):
    pass

d1 = Dog('Rex')
d1.speak()

# Challenge: Polymorphism
# Inside the editor, complete the following steps:
# Create a class Cat with a method sound that prints "Meow"
# Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
# Create objects c1 = Cat() and f1 = Fox()
# Call sound() on both objects

class AnimalWithSound(Protocol):
    def sound(self) -> None:
        ...

class Cat:
    def sound(self) -> None:
        print('Meow')

class Fox:
    def sound(self) -> None:
        print('Wa-pa-pa-pa-pa-pow!')

c1 = Cat()
f1 = Fox()

animals: List[AnimalWithSound] = [c1, f1]

for x in animals:
    x.sound()

# Protected and private properties
# Challenge Encapsulation
# Inside the editor, complete the following steps:
# Create a class ScoreBoard
# Add an __init__ with a score parameter and store it as a private attribute
# Add a method called get_score that returns the private score
# Create an object s1 with a score of 0
# Print the score of s1

class ScoreBoard:
    def __init__(self, score: int) -> None:
        self.__score = score

    def get_score(self) -> int:
        return self.__score
    
s1 = ScoreBoard(0)
print(s1.get_score())