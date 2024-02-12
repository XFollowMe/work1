if __name__ == "__main__":

    class Plant:
        """ Базовый класс растения. """

        def __init__(self, species: str, age: int):
            self._species = species
            self._age = age

        @property
        def species(self):
            """ Защита от изменения пользователем """
            return self._species
        @property
        def age(self):
            """ Защита от изменения пользователем"""
            return self._age

        def grow(self, years: int) -> None:
            """ Метод для моделирования роста растения. """
            self._age += years
            print(f"{self._species} растет. Возраст увеличен на {years} год(а).")

        def __str__(self) -> str:
            """ Магический метод для представления объекта в виде строки. """
            return f"Растение вида {self._species}, возраст {self._age} лет."

        def __repr__(self) -> str:
            """ Магический метод для представления объекта в виде строки для отладки. """
            return f"{self.__class__.__name__}(species={self._species!r}, age={self._age})"


    class Flower(Plant):
        """ Подкласс унаследованный от Plant"""
        def __init__(self, species: str, age: int, color: str):
            super().__init__(species, age)
            self._color = color

        def bloom(self) -> None:
            """ Метод, представляющий расцветение цветка. """
            print(f"Цветок вида {self._species} цветет! Цвет: {self._color}.")

        def __repr__(self) -> str:
            """ Перегрузка метода __repr__ для добавления цвета в представление объекта. """
            return f"{self.__class__.__name__}(species={self._species!r}, age={self._age}, color={self._color!r})"


    pass
