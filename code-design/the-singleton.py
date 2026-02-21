# You are managing a Cloud Server Cluster. To save money, your account only allows a maximum of 3 servers to exist at any time.

class CloudServer:
    _server_count: int = 0

    def __init__(self, name: str) -> None:
        if self.get_active_count() == 3:
            raise ConnectionError('Server limit reached!')
        else:
            self.increase_active_acount()
            self.name = name

    @classmethod
    def get_active_count(cls) -> int:
        return cls._server_count
    
    @classmethod
    def increase_active_acount(cls) -> None:
        cls._server_count += 1

CloudServer('1')
CloudServer('2')
CloudServer('3')
CloudServer('4')