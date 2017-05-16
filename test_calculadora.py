from calculadora import calculadora

def test_suma():
    calc = calculadora()
    resultado = calc.suma(2, 3)
    assert resultado == 5

def test_resta():
    calc = calculadora()
    resultado = calc.resta(2, 2)
    assert resultado == 0
