class IterableNull:
    def __init__(self) -> None:
        self.end = False

    def __next__(self):
        if self.end: raise StopIteration
        self.end = True
        return Null()


class Null(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Null, cls).__new__(cls)
        return cls.instance

    def __iter__(self):
        return IterableNull()
