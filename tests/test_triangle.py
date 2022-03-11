from fixacao_conceito import triangle


def test_equilatero():
    pass


def test_isosceles():
    pass


def test_escaleno():
    pass


def test_nao_eh_triangulo():
    pass


def test_entrada_invalida():
    assertion_error_message = "A função tipo_triangulo não retornou 0 ao passar parâmetros inválidos."

    assert triangle.tipo_triangulo(101, 102, 103) == 0, assertion_error_message
    assert triangle.tipo_triangulo(-1, -2, -3) == 0, assertion_error_message
    assert triangle.tipo_triangulo(-78, 76, 26) == 0, assertion_error_message
    assert triangle.tipo_triangulo(52, -19999, 63) == 0, assertion_error_message
    assert triangle.tipo_triangulo(78, 32, -8) == 0, assertion_error_message
