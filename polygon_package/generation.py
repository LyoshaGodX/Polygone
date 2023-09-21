import math
import random


def generate_regular_polygon(num_vertices, side_length):
    if num_vertices < 3:
        raise ValueError("Number of vertices should be at least 3.")

    angle = 2 * math.pi / num_vertices

    points = []

    for i in range(num_vertices):
        x = side_length * math.cos(i * angle)
        y = side_length * math.sin(i * angle)
        points.append((x, y))

    return points


def generate_irregular_polygon(num_vertices, radius):
    if num_vertices < 3:
        raise ValueError("Number of vertices should be at least 3.")

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