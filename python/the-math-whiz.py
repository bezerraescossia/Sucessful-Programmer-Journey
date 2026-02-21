# Your Goal: Create a class named Calculator that performs a simple calculation without needing to be instantiated.

class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
result = Calculator.add(2, 3)
print(result)