"""
What is Pydantic?
1. Pydantic is a framework to create specialized Python classes.
1.1. lass attributes are called fields
1.2. the specialized class is called model
2. It provides a simple way to load data from a dictionary or JSON into a model (which is a Python class) (deserializing).
3. Simple way to extract model instance data to a dictionary or JSON (serializing)
4. provides a robust system to validate data during deserialization
5. enable us to work with our data in an OOP manner
6. Normal flow for pydantic is deserialization -> validation -> serialization (if necessary)
"""
from pydantic import BaseModel, ValidationError


# class Person:
#     def __init__(self, first_name: str, last_name: str, age: int) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"

try:
    p1 = Person(first_name="Rafael", last_name="Bezerra",age=33)
    # p2 = Person(first_name="Rafael", last_name="Bezerra", age="thirty three")
except ValidationError as ve:
    print(ve)