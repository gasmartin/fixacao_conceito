def tipo_triangulo(l1, l2, l3):
    def __is_invalid_parameter(param):
        return param < 0 or param > 99

    def __is_triangle(l1, l2, l3):
        return l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1

    parameter_values = (l1, l2, l3)

    if any(map(__is_invalid_parameter, parameter_values)):
        return 0

    if not __is_triangle(*parameter_values):
        return 4

    if l1 == l2 and l2 == l3:
        return 1

    if l1 == l2 or l2 == l3 or l1 == l3:
        return 2

    return 3
