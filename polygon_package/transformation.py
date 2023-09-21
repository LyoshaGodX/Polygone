import math


def multiply_matrices(matrix1, matrix2):
    result = []

    for point in matrix1:
        x_result = point[0] * matrix2[0][0] + point[1] * matrix2[1][0]
        y_result = point[0] * matrix2[0][1] + point[1] * matrix2[1][1]

        result.append((x_result, y_result))

    return result


def scaling_polygon(polygon, scale_x, scale_y):

    scaling_matrix = [[scale_x, 0], [0, scale_y]]

    return multiply_matrices(polygon, scaling_matrix)


def translate_polygon(polygon, translate_x, translate_y):
    translated_polygon = []

    for x, y in polygon:
        new_x = x + translate_x
        new_y = y + translate_y
        translated_polygon.append((new_x, new_y))

    return translated_polygon


def rotate_polygon(polygon, angle, clockwise=True):
    angle_rad = math.radians(angle)

    if clockwise:
        rotation_matrix = [[math.cos(angle_rad), -math.sin(angle_rad)],
                           [math.sin(angle_rad), math.cos(angle_rad)]]
    else:
        rotation_matrix = [[math.cos(angle_rad), math.sin(angle_rad)],
                           [-math.sin(angle_rad), math.cos(angle_rad)]]

    return multiply_matrices(polygon, rotation_matrix)