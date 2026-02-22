from pydantic import BaseModel


class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int

Circle.model_fields

Circle(radius=1)

data = {'radius': 1}
data_json = '{"radius": 1}'

print(Circle.model_validate(data))
print(Circle.model_validate_json(data_json))

Circle(center=(1, 1), radius=2)