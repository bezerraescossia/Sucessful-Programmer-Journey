# You are building a system for a high-security vault. Access codes must be exactly 6 digits long and numeric.

class Vault:
    def __init__(self, code: str) -> None:
        if self.is_valid_code(code):
            self.code = code
        else:
            raise ValueError('Invalid access code!')

    @staticmethod
    def is_valid_code(code: str) -> bool:
        if (len(code) == 6):
            return True
        else:
            return False

v1 = Vault('123456')
v2 = Vault('ABC')