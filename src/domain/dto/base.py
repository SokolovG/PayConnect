import msgspec


class User(msgspec.Struct):
    name: str
    