import math


def multiply_matrices(matrix1, matrix2):
    """
    Умножает матрицу вершин на матрицу преобразования и возвращает новую матрицу вершин.

    Parameters:
    ----------
    matrix1 : list of tuple
        Матрица вершин, представленная списком кортежей с координатами точек.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    matrix2 : list of list
        Матрица преобразования 2x2, представленная списком списков.
        Матрица должна иметь форму [[a, b], [c, d]].

    Returns:
    --------
    list of tuple
        Новая матрица вершин, представленная списком кортежей с координатами точек.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция выполняет умножение матрицы вершин `matrix1` на матрицу преобразования `matrix2`.
    Это применяется для преобразования координат точек с использованием матричных операций.

    Examples:
    ---------
    >>> matrix1 = [(1, 2), (3, 4), (5, 6)]
    >>> matrix2 = [[2, 0], [0, 3]]
    >>> result = multiply_matrices(matrix1, matrix2)

    """
    result = []

    for point in matrix1:
        x_result = point[0] * matrix2[0][0] + point[1] * matrix2[1][0]
        y_result = point[0] * matrix2[0][1] + point[1] * matrix2[1][1]

        result.append((x_result, y_result))

    return result


def scaling_polygon(polygon, scale_x, scale_y):
    """
    Масштабирует многоугольник по осям X и Y и возвращает новый многоугольник.

    Parameters:
    ----------
    polygon : list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    scale_x : float
        Коэффициент масштабирования по оси X.

    scale_y : float
        Коэффициент масштабирования по оси Y.

    Returns:
    --------
    list of tuple
        Новый многоугольник, представленный списком кортежей с координатами вершин.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция выполняет масштабирование многоугольника по осям X и Y с использованием коэффициентов
    масштабирования `scale_x` и `scale_y`. Масштабирование осуществляется путем умножения координат
    вершин на соответствующие коэффициенты масштабирования.

    Examples:
    ---------
    >>> polygon = [(1, 2), (3, 4), (5, 6)]
    >>> scaled_polygon = scaling_polygon(polygon, 2, 3)

    """
    scaling_matrix = [[scale_x, 0], [0, scale_y]]

    return multiply_matrices(polygon, scaling_matrix)


def translate_polygon(polygon, translate_x, translate_y):
    """
    Сдвигает многоугольник на заданное расстояние по осям X и Y и возвращает новый многоугольник.

    Parameters:
    ----------
    polygon : list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    translate_x : float
        Расстояние смещения по оси X.

    translate_y : float
        Расстояние смещения по оси Y.

    Returns:
    --------
    list of tuple
        Новый многоугольник, представленный списком кортежей с координатами вершин.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция выполняет смещение многоугольника на заданные расстояния `translate_x` и `translate_y`
    по осям X и Y соответственно. Смещение осуществляется путем прибавления расстояний к координатам вершин.

    Examples:
    ---------
    >>> polygon = [(1, 2), (3, 4), (5, 6)]
    >>> translated_polygon = translate_polygon(polygon, 2, 3)

    """
    translated_polygon = []

    for x, y in polygon:
        new_x = x + translate_x
        new_y = y + translate_y
        translated_polygon.append((new_x, new_y))

    return translated_polygon


def rotate_polygon(polygon, angle, clockwise=True):
    """
    Поворачивает многоугольник на заданный угол относительно начала координат и возвращает новый многоугольник.

    Parameters:
    ----------
    polygon : list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    angle : float
        Угол поворота в градусах.

    clockwise : bool, optional
        Определяет направление поворота (по часовой стрелке или против часовой стрелки).
        По умолчанию установлено значение True, что соответствует повороту по часовой стрелке.

    Returns:
    --------
    list of tuple
        Новый многоугольник, представленный списком кортежей с координатами вершин.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    Notes:
    ------
    Функция выполняет поворот многоугольника на указанный угол `angle` в градусах относительно начала координат.
    Направление поворота (по часовой стрелке или против часовой стрелки) задается параметром `clockwise`.

    Examples:
    ---------
    >>> polygon = [(1, 2), (3, 4), (5, 6)]
    >>> rotated_polygon = rotate_polygon(polygon, 45, clockwise=False)

    """
    angle_rad = math.radians(angle)

    if clockwise:
        rotation_matrix = [[math.cos(angle_rad), -math.sin(angle_rad)],
                           [math.sin(angle_rad), math.cos(angle_rad)]]
    else:
        rotation_matrix = [[math.cos(angle_rad), math.sin(angle_rad)],
                           [-math.sin(angle_rad), math.cos(angle_rad)]]

    return multiply_matrices(polygon, rotation_matrix)