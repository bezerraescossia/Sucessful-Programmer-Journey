# You are building a "Server Monitor." You need to be able to list all active servers by name at any time.

class CloudServer:
    _server_count: int = 0
    _registry: list[str] = []

    def __init__(self, name: str) -> None:
        if self.get_active_count() == 3:
            raise ConnectionError('Server limit reached!')
        else:
            CloudServer._server_count += 1
            CloudServer._registry.append(name)
            self.name = name

    def __del__(self) -> None:
        CloudServer._server_count -= 1
        CloudServer._registry.remove(self.name)

    @classmethod
    def get_active_count(cls) -> int:
        return cls._server_count
    
    @classmethod
    def get_all_server_names(cls) -> list[str]:
        return cls._registry


s1 = CloudServer('Alpha')
s2 = CloudServer('Beta')
servers = CloudServer.get_all_server_names()

print(servers)

del s2

servers = CloudServer.get_all_server_names()

print(servers)