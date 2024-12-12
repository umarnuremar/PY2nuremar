from task_1 import Car, Tree, SocialNetwork


def main():
    try:
        car = Car(make="Toyota", model="Corolla", year=2023, color="Red")
        tree = Tree(height=15.0, species="Oak", age=30)
        social_network = SocialNetwork(name="TwitterClone", num_users=100000)
    except TypeError as e:
        print(f"Ошибка при создании объекта: {e}")

    try:
        car.change_color(new_color="Blue")  # Изменение цвета машины
        print(f"Новый цвет автомобиля: {car.get_info()}")
    except TypeError as e:
        print(f"Ошибка: неправильные данные")

    try:
        tree.grow(years=5)  # Увеличение возраста дерева
        print(f"Текущая высота и возраст дерева: {tree.get_height_and_age()}")
    except TypeError as e:
        print(f"Ошибка: неправильные данные")

    try:
        social_network.add_users(num_new_users=500)  # Добавление новых пользователей
        print(f"Текущее количество пользователей: {social_network.get_user_count()}")
    except TypeError as e:
        print(f"Ошибка: неправильные данные")


if __name__ == "__main__":
    main()
