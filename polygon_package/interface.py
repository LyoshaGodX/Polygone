import copy

from polygon_package.generation import generate_regular_polygon, generate_irregular_polygon
from polygon_package.transformation import scaling_polygon, translate_polygon, rotate_polygon
from polygon_package.visualization import plot_polygon, plot_polygons_transition


def main_menu():
    while True:
        print("Главное меню:")
        print("1. Создать новый многоугольник.")
        print("2. Выйти из программы.")
        choice = input("Выберите опцию: ")

        if choice == "1":
            create_polygon_menu()
        elif choice == "2":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def create_polygon_menu():
    polygon = None  # Инициализируем переменную для хранения многоугольника
    transformations = []  # Хранение истории преобразований
    while True:
        print("\nМеню создания многоугольника:")
        print("1. Создать правильный многоугольник.")
        print("2. Создать неправильный многоугольник.")
        print("3. Вернуться в главное меню.")
        print("4. Выйти из программы.")
        choice = input("Выберите опцию: ")

        if choice == "1":
            polygon = create_regular_polygon()
            transformations = []  # Сбрасываем историю преобразований при создании нового многоугольника
        elif choice == "2":
            polygon = create_irregular_polygon()
            transformations = []  # Сбрасываем историю преобразований при создании нового многоугольника
        elif choice == "3":
            break
        elif choice == "4":
            exit()
        else:
            print("Неверный выбор. Попробуйте снова.")

        if polygon:
            transform_polygon(polygon,
                              transformations)  # Передаем многоугольник и историю преобразований для дальнейших преобразований


def create_regular_polygon():
    num_vertices = None
    side_length = None

    while True:
        if num_vertices is None or side_length is None:
            num_vertices = int(input("Введите количество вершин: "))
            side_length = float(input("Введите длину стороны: "))

        try:
            polygon = generate_regular_polygon(num_vertices, side_length)
            print("Координаты вершин многоугольника:")
            for point in polygon:
                print(point)

            plot_polygon(polygon)

            # После создания многоугольника предложите опции
            print("\n1. Создать новый прямоугольник с текущими параметрами.")
            print("2. Перейти к преобразованиям.")
            print("3. Вернуться в меню создания многоугольника.")
            print("4. Выйти из программы.")
            choice = input("Выберите опцию: ")

            if choice == "1":
                continue  # Создать новый с теми же параметрами
            elif choice == "2":
                transform_polygon(polygon, [])  # Перейти к преобразованиям
            elif choice == "3":
                return  # Вернуться в меню создания многоугольника
            elif choice == "4":
                exit()  # Выйти из программы
            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(e)

def create_irregular_polygon():
    num_vertices = None
    radius = None

    while True:
        if num_vertices is None or radius is None:
            num_vertices = int(input("Введите количество вершин: "))
            radius = float(input("Введите радиус окружности: "))

        try:
            polygon = generate_irregular_polygon(num_vertices, radius)
            print("Координаты вершин многоугольника:")
            for point in polygon:
                print(point)

            plot_polygon(polygon)

            # После создания многоугольника предложите опции
            print("\n1. Создать новый прямоугольник с текущими параметрами.")
            print("2. Перейти к преобразованиям.")
            print("3. Вернуться в меню создания многоугольника.")
            print("4. Выйти из программы.")
            choice = input("Выберите опцию: ")

            if choice == "1":
                continue  # Создать новый с теми же параметрами
            elif choice == "2":
                transform_polygon(polygon, [])  # Перейти к преобразованиям
            elif choice == "3":
                return  # Вернуться в меню создания многоугольника
            elif choice == "4":
                exit()  # Выйти из программы
            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(e)


def transform_polygon(polygon, transformations):
    while True:
        print("\nМеню преобразования многоугольника:")
        print("1. Масштабирование.")
        print("2. Перемещение.")
        print("3. Вращение.")
        if transformations:
            print("4. Вернуться к предыдущему преобразованию.")
        print("5. Вернуться к созданию многоугольника.")
        print("6. Вернуться в главное меню.")
        print("7. Выйти из программы.")
        choice = input("Выберите опцию: ")

        if choice == "1":
            transformations.append(("scale", copy.deepcopy(
                polygon)))  # Глубокая копия многоугольника для сохранения состояния перед преобразованием
            polygon = scale_polygon(polygon, transformations)
        elif choice == "2":
            transformations.append(("translate", copy.deepcopy(polygon)))
            polygon = translate_polygon_menu(polygon, transformations)
        elif choice == "3":
            transformations.append(("rotate", copy.deepcopy(polygon)))
            polygon = rotate_polygon_menu(polygon, transformations)
        elif choice == "4" and transformations:
            _, previous_state = transformations.pop()
            plot_polygons_transition(polygon, previous_state)
            polygon = previous_state
        elif choice == "5":
            return polygon  # Возвращаемся к созданию многоугольника
        elif choice == "6":
            return
        elif choice == "7":
            exit()
        else:
            print("Неверный выбор. Попробуйте снова.")


def scale_polygon(polygon, transformations):
    scale_x = float(input("Введите коэффициент масштабирования по оси X: "))
    scale_y = float(input("Введите коэффициент масштабирования по оси Y: "))

    scaled_polygon = scaling_polygon(polygon, scale_x, scale_y)

    print("Матрица вершин масштабированного многоугольника:")
    for row in scaled_polygon:
        print(row)

    plot_polygons_transition(polygon, scaled_polygon)
    return scaled_polygon  # Возвращаем масштабированный многоугольник


def translate_polygon_menu(polygon, transformations):
    translate_x = float(input("Введите смещение по оси X: "))
    translate_y = float(input("Введите смещение по оси Y: "))

    translated_polygon = translate_polygon(polygon, translate_x, translate_y)

    print("Матрица вершин многоугольника после смещения:")
    for row in translated_polygon:
        print(row)

    plot_polygons_transition(polygon, translated_polygon)
    return translated_polygon  # Возвращаем смещенный многоугольник


def rotate_polygon_menu(polygon, transformations):
    angle = float(input("Введите угол поворота (в градусах): "))
    clockwise = input("По часовой стрелке (да/нет)? ").strip().lower() == "да"

    rotated_polygon = rotate_polygon(polygon, angle, clockwise)

    print("Матрица вершин повернутого многоугольника:")
    for row in rotated_polygon:
        print(row)

    plot_polygons_transition(polygon, rotated_polygon)
    return rotated_polygon  # Возвращаем повернутый многоугольник