class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        if not isinstance(pages,int):
            raise TypeError
        if pages < 6:
            raise ValueError
        self.pages = pages

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        if not isinstance(duration,(float,int)):
            raise TypeError
        if duration <= 1:
            raise ValueError
        self.duration = duration
