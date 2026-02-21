from pydantic import BaseModel, ValidationError
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
dlog = logging.debug


class Coordinates(BaseModel):
    x: float
    y: float

p1 = Coordinates(x=1.1, y=2.2)
dlog(f"p1: {repr(p1)} - {Coordinates.model_fields}")

# Here is where the type coercion occours. 
# We're going to try as input for coordinate an integer and string and let's see what happens

dlog("Creating a p2...")
p2 = Coordinates(x=0, y="2.2") # type: ignore
dlog(f"p2: {repr(p2)} - {type(p2.x)}, {type(p2.y)}")

# We can control the level of type coercion we want. For instance we can set a strict mode

dlog("Creating an instance with wrong type in strict=True")
try:
    Coordinates.model_validate({'x': 0, 'y': '2.2'}, strict=True)
except ValidationError as ve:
    print(ve)