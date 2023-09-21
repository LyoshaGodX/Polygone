from matplotlib import pyplot as plt


def plot_polygon(polygon, dpi=150, margin=0.1):
    if not polygon:
        raise ValueError("Polygon should not be empty.")

    x_values, y_values = zip(*polygon)

    x_values += (x_values[0],)
    y_values += (y_values[0],)

    plt.figure(dpi=dpi)
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title("Polygon")
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
    if not polygon1 or not polygon2:
        raise ValueError("Polygons should not be empty.")

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
        plt.text(x, y, f"({x:.2f}, {y:.2f})", ha='center', va='bottom')  # Добавляем координаты точек

    plt.title("Transformation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    plt.margins(x=margin, y=margin)

    plt.show()