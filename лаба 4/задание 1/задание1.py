class Disk:
    """
    Базовый класс, представляющий диск.

    Атрибуты:
        capacity (int): Емкость диска в гигабайтах.
        manufacturer (str): Производитель диска.
        _serial_number (str): Серийный номер диска (инкапсулированный атрибут).

    Методы:
        get_info(): Возвращает информацию о диске.
    """

    def __init__(self, capacity: int, manufacturer: str, serial_number: str) -> None:
        """
        Инициализация объекта Disk.

        Аргументы:
            capacity (int): Емкость диска в гигабайтах.
            manufacturer (str): Производитель диска.
            serial_number (str): Серийный номер диска.
        """
        self.capacity = capacity
        self.manufacturer = manufacturer
        self._serial_number = serial_number  # Инкапсулированный атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Disk.
        """
        return f"Disk(capacity={self.capacity}GB, manufacturer={self.manufacturer})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Disk.
        """
        return f"Disk(capacity={self.capacity}, manufacturer='{self.manufacturer}', serial_number='{self._serial_number}')"

    def get_info(self) -> str:
        """
        Возвращает информацию о диске.

        Возвращает:
            str: Информация о диске.
        """
        return f"Disk with capacity {self.capacity}GB manufactured by {self.manufacturer}."


class CDDisk(Disk):
    """
    Дочерний класс, представляющий CD-диск.

    Атрибуты:
        write_speed (str): Скорость записи CD-диска.

    Методы:
        get_info(): Перегруженный метод, возвращающий информацию о CD-диске.
    """

    def __init__(self, capacity: int, manufacturer: str, serial_number: str, write_speed: str) -> None:
        """
        Инициализация объекта CDDisk.

        Аргументы:
            capacity (int): Емкость диска в гигабайтах.
            manufacturer (str): Производитель диска.
            serial_number (str): Серийный номер диска.
            write_speed (str): Скорость записи CD-диска.
        """
        super().__init__(capacity, manufacturer, serial_number)
        self.write_speed = write_speed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта CDDisk.
        """
        return f"CDDisk(capacity={self.capacity}GB, manufacturer={self.manufacturer}, write_speed={self.write_speed})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта CDDisk.
        """
        return f"CDDisk(capacity={self.capacity}, manufacturer='{self.manufacturer}', serial_number='{self._serial_number}', write_speed='{self.write_speed}')"

    def get_info(self) -> str:
        """
        Перегруженный метод, возвращающий информацию о CD-диске.

        Причина перегрузки: CD-диски имеют дополнительную характеристику - скорость записи,
        которая должна быть включена в информацию о диске.

        Возвращает:
            str: Информация о CD-диске.
        """
        return f"CDDisk with capacity {self.capacity}GB manufactured by {self.manufacturer}, write speed {self.write_speed}."
