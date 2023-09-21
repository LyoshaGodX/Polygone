from matplotlib import pyplot as plt


def plot_polygon(polygon, dpi=150, margin=0.1):
    """
    Рисует графическое представление многоугольника и его вершин на графике.

    Parameters:
    ----------
    polygon : list of tuple
        Список кортежей с координатами вершин многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    dpi : int, optional
        Разрешение графика (по умолчанию 150).

    margin : float, optional
        Отступ многоугольника от границ графика (по умолчанию 0.1).

    Raises:
    -------
    ValueError
        Если входной список `polygon` пуст.

    Returns:
    --------
    None

    Notes:
    ------
    Функция отображает графическое представление многоугольника, включая его вершины на графике.
    Многоугольник соединяется линиями между вершинами и маркируется точками. Координаты вершин выводятся рядом с точками.
    График автоматически подстраивается под размеры многоугольника.

    Examples:
    ---------
    >>> polygon = [(0, 0), (1, 1), (2, 0)]
    >>> plot_polygon(polygon)
    """
    if not polygon:
        raise ValueError("Нельзя распечатать пустоту")

    x_values, y_values = zip(*polygon)

    x_values += (x_values[0],)
    y_values += (y_values[0],)

    plt.figure(dpi=dpi)
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title("Многоугольник")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    texts = []
    for i, (x, y) in enumerate(polygon):
        text = f"({x:.2f}, {y:.2f})"
        texts.append(plt.text(x, y, text, ha='center', va='bottom'))

    plt.margins(x=margin, y=margin)

    plt.show()


def plot_polygons_transition(polygon1, polygon2, dpi=150, margin=0.1):
    """
    Рисует графическое представление двух многоугольников и переход между ними на графике.

    Parameters:
    ----------
    polygon1 : list of tuple
        Список кортежей с координатами вершин первого многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    polygon2 : list of tuple
        Список кортежей с координатами вершин второго многоугольника.
        Каждый кортеж содержит два значения (x, y) для координаты точки.

    dpi : int, optional
        Разрешение графика (по умолчанию 150).

    margin : float, optional
        Отступ многоугольника от границ графика (по умолчанию 0.1).

    Raises:
    -------
    ValueError
        Если хотя бы один из многоугольников пуст.

    Returns:
    --------
    None

    Notes:
    ------
    Функция отображает графическое представление двух многоугольников и переход между ними на графике.
    Первый многоугольник представлен серыми линиями, второй многоугольник обозначен маркерами.
    Координаты вершин второго многоугольника выводятся рядом с маркерами.

    Examples:
    ---------
    >>> polygon1 = [(0, 0), (1, 1), (2, 0)]
    >>> polygon2 = [(0, 0), (2, 2), (4, 0)]
    >>> plot_polygons_transition(polygon1, polygon2)
    """
    if not polygon1 or not polygon2:
        raise ValueError("Нельзя распечатать пустоту")

    x_values1, y_values1 = zip(*polygon1)
    x_values2, y_values2 = zip(*polygon2)

    x_values1 += (x_values1[0],)
    y_values1 += (y_values1[0],)
    x_values2 += (x_values2[0],)
    y_values2 += (y_values2[0],)

    plt.figure(dpi=dpi)
    plt.plot(x_values1, y_values1, color='gray', alpha=0.5, label='Polygon 1')
    plt.plot(x_values2, y_values2, marker='o', label='Polygon 2')

    for x, y in polygon2:
        plt.plot(x, y, markersize=5)
        plt.text(x, y, f"({x:.2f}, {y:.2f})", ha='center', va='bottom')  # Координаты точек на графике

    plt.title("Преобразование")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    plt.margins(x=margin, y=margin)

    plt.show()