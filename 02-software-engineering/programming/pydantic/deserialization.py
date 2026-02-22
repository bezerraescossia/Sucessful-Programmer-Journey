from pydantic import BaseModel, ValidationError
from typing import Any


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

# Most simple form os deserialization
print("Testing simple form o deserialization...")
Person(first_name="Rafael", last_name="Bezerra", age=33)

# Deserializing from a dictionary
data: dict[str, Any] = {
    "first_name": "Rafael",
    "last_name": "Bezerra",
    "age": 33
}

# Normal way to load, but not good, it can get bad with nested dictionaries or other situations.
print("Testing normal way of loading dict...")
p = Person(**data)
print(repr(p))

# Pydantic way of loading the data
print("Testing pydantic way for deserialization...")
p = Person.model_validate(data)
print(repr(p))

# Testing validation of data
print("Testing missing values from dict...")
missing_data: dict[str, Any] = {
    "first_name": "Rafael"
}

try:
    p = Person.model_validate(missing_data)
    print(repr(p))
except ValidationError as ve:
    print(ve)


# Loading from a JSON format file
print("Deserializing JSON format file...")
data_json: str = '''
{
    "first_name": "Rafael",
    "last_name": "Bezerra",
    "age": 33
}
'''

p = Person.model_validate_json(data_json)
print(f"Loaded from JSON data: {repr(p)}")


print("Deserializing invalid JSON data...")
data_json_invalid_type: str = '''
{
    "first_name": "Rafael",
    "last_name": "Bezerra",
    "age": "twe"
}
'''

try:
    p = Person.model_validate_json(data_json_invalid_type)
    print(f"Loaded from JSON data: {repr(p)}")
except ValidationError as ve:
    print(ve)