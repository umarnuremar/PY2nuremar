class Laptop:
    """
    Базовый класс для ноутбуков

    Атрибуты:
        brand (str): Бренд ноутбука
        model (str): Модель ноутбука
        price (float): Цена ноутбука
    """

    def __init__(self, brand: str, model: str, price: float):
        """
        Инициализация ноутбука

        Аргументы:
            brand (str): Бренд ноутбука
            model (str): Модель ноутбука
            price (float): Цена ноутбука
        """
        self.brand = brand
        self.model = model
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление ноутбука

        Возвращаемое значение:
            str: Строковое представление ноутбука
        """
        return f"Ноутбук {self.brand} {self.model}, цена: {self.price} USD"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление ноутбука

        Возвращаемое значение:
            str: Официальное строковое представление ноутбука
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, price={self.price!r})"

    def display_info(self) -> str:
        """
        Возвращает информацию о ноутбуке

        Возвращаемое значение:
            str: Информация о ноутбуке
        """
        return f"Бренд: {self.brand}, Модель: {self.model}, Цена: {self.price} USD"

    def run_application(self, app_name: str):
        """
        Метод для запуска приложения

        Аргументы:
            app_name (str): Название приложения для запуска
        """
        print(f"Запускаем приложение {app_name} на ноутбуке {self.brand} {self.model}")


class GamingLaptop(Laptop):
    """
    Класс для игровых ноутбуков

    Атрибуты:
        brand (str): Бренд ноутбука
        model (str): Модель ноутбука
        price (float): Цена ноутбука
        gpu (str): Модель графической карты
    """

    def __init__(self, brand: str, model: str, price: float, gpu: str):
        """
        Инициализация игрового ноутбука.

        Аргументы:
            brand (str): Бренд ноутбука
            model (str): Модель ноутбука
            price (float): Цена ноутбука
            gpu (str): Модель графической карты
        """
        super().__init__(brand, model, price)
        self.gpu = gpu

    def __str__(self) -> str:
        """
        Возвращает строковое представление игрового ноутбука

        Возвращаемое значение:
            str: Строковое представление игрового ноутбука
        """
        return f"Игровой ноутбук {self.brand} {self.model}, цена: {self.price} USD, GPU: {self.gpu}"

    def display_info(self) -> str:
        """
        Возвращает информацию об игровом ноутбуке

        Возвращаемое значение:
            str: Информация об игровом ноутбуке

        Причина перегрузки:
            Добавление информации о графической карте
        """
        parent_info = super().display_info()  # Вызов метода родительского класса
        return f"{parent_info}, GPU: {self.gpu}"


if __name__ == "__main__":
    try:
        gaming_laptop = GamingLaptop("ASUS", "ROG Zephyrus G14", 1499.99, "NVIDIA GeForce RTX 3060")
        print(gaming_laptop)
        print(gaming_laptop.display_info())
        print(repr(gaming_laptop))
        gaming_laptop.run_application("Cyberpunk 2077")  # Используем унаследованный метод
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        gaming_laptop.price = -200
    except ValueError as e:
        print(f"Ошибка: {e}")
