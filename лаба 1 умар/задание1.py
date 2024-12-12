# TODO: Подробно описать три произвольных класса


class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, make: str, model: str, year: int, color: str = "black"):
        """
        Конструктор автомобиля.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска (целое число >= 1900).
        :param color: Цвет автомобиля (по умолчанию черный).
        :raises TypeError: Если год выпуска меньше 1900.
        """
        if year < 1900:
            raise TypeError("Год выпуска автомобиля должен быть больше или равен 1900.")
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет автомобиля.

        :param new_color: Новый цвет автомобиля.
        """
        self.color = new_color

    def get_info(self) -> str:
        """
        Возвращает информацию об автомобиле в формате 'Марка Модель, Год выпуска, Цвет'.

        :return: Строку с информацией об автомобиле.
        """
        return f"{self.make} {self.model}, {self.year}, {self.color}"


class Tree:
    """Класс, представляющий дерево."""

    def __init__(self, height: float, species: str, age: int = 0):
        """
        Конструктор дерева.

        :param height: Высота дерева (в метрах, положительное число).
        :param species: Вид дерева.
        :param age: Возраст дерева (по умолчанию 0 лет).
        :raises TypeError: Если высота дерева отрицательная.
        """
        if height <= 0:
            raise TypeError("Высота дерева должна быть положительной.")
        self.height = height
        self.species = species
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на указанное количество лет.

        :param years: Количество лет, на которое увеличивается возраст (целое число >= 0).
        :raises TypeError: Если количество лет отрицательное.
        """
        if years < 0:
            raise TypeError("Количество лет должно быть неотрицательным числом.")
        self.age += years

    def get_height_and_age(self) -> tuple[float, int]:
        """
        Возвращает высоту и возраст дерева.

        :return: Кортеж (высота, возраст).
        """
        return self.height, self.age


class SocialNetwork:
    """Представляет социальную сеть с названием и количеством пользователей."""

    def __init__(self, name: str, num_users: int):
        """Инициализирует объект социальной сети."""
        self.name = name
        if not isinstance(num_users, int) or num_users < 0:
            raise TypeError("Количество пользователей должно быть целым неотрицательным числом.")
        self.num_users = num_users

    def add_users(self, num_new_users: int) -> int:
        """Добавляет новых пользователей к социальной сети.

        Аргументы:
            num_new_users (int): Количество новых пользователей для добавления. Должно быть неотрицательным.

        Возвращает:
            int: Обновленное количество пользователей.

        Исключения:
            TypeError: если num_new_users является отрицательным числом.

        Пример использования:
        >>> sn = SocialNetwork("ПримернаяСеть", 1000)
        >>> sn.add_users(500)
        1500
        """
        if num_new_users < 0:
            raise TypeError("Количество новых пользователей не может быть отрицательным.")
        self.num_users += num_new_users
        return self.num_users

    def get_user_count(self) -> int:
        """Возвращает текущее количество пользователей."""
        return self.num_users
