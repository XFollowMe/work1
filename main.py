class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name
    
    @property
    def author(self):
        return self._author
    
    def __str__(self):  # заменим str на __str__
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):  # заменим repr на __repr__
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"  

    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError
        if pages < 6:
            raise ValueError
        self._pages = pages


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):  # заменим repr() на __repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 1:
            raise ValueError
        self._duration = duration


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):  # заменим repr() на __repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration})"
