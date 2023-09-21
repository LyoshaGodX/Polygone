import math
import random


def generate_regular_polygon(num_vertices, side_length):
    """
    Генерирует координаты вершин правильного многоугольника.

    Parameters:
    ----------
    num_vertices : int
        Количество вершин многоугольника. Должно быть не меньше 3.

    side_length : float
        Длина стороны многоугольника.

    Returns:
    --------
    list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция генерирует координаты вершин правильного многоугольника с заданным количеством вершин `num_vertices`
    и длиной стороны `side_length`. Вершины многоугольника равномерно расположены на окружности.

    Examples:
    ---------
    >>> vertices = 6
    >>> length = 2.0
    >>> polygon = generate_regular_polygon(vertices, length)

    """
    if num_vertices < 3:
        raise ValueError("Количество вершин должно быть не меньше 3")

    angle = 2 * math.pi / num_vertices

    points = []

    for i in range(num_vertices):
        x = side_length * math.cos(i * angle)
        y = side_length * math.sin(i * angle)
        points.append((x, y))

    return points


def generate_irregular_polygon(num_vertices, radius):
    """
    Генерирует координаты вершин неправильного многоугольника.

    Parameters:
    ----------
    num_vertices : int
        Количество вершин многоугольника. Должно быть не меньше 3.

    radius : float
        Радиус окружности, на которой будут расположены вершины многоугольника.

    Returns:
    --------
    list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция генерирует координаты вершин неправильного многоугольника с заданным количеством вершин `num_vertices`
    и радиусом окружности `radius`. Вершины многоугольника располагаются на окружности случайным образом.

    Examples:
    ---------
    >>> vertices = 5
    >>> radius = 3.0
    >>> polygon = generate_irregular_polygon(vertices, radius)

    """
    if num_vertices < 3:
        raise ValueError("Количество вершин должно быть не меньше 3")

    random_angles = []

    for _ in range(num_vertices):
        random_angle = random.uniform(0, 2 * math.pi)
        random_angles.append(random_angle)

    sorted_angles = sorted(random_angles)

    points = []
    for angle in sorted_angles:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))

    return points