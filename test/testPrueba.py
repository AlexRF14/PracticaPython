import pytest
import sys
sys.path.append(".")
from main.main import Calculadora

# set PYTHONPATH=. pytest test/testPrueba.py 

# Suma

def test_calculadoraSuma_1():
    calculadora = Calculadora()
    assert calculadora.calculadoraSumaResta(3 , 2) == 5
    
def test_calculadoraSuma_2():
    calculadora = Calculadora()
    assert calculadora.calculadoraSumaResta(3 , 2) != 6
    
# Resta

def test_calculadoraResta_1():
    calculadora = Calculadora()
    assert calculadora.calculadoraSumaResta(3 , - 2) == 1
    
def test_calculadoraResta_2():
    calculadora = Calculadora()
    assert calculadora.calculadoraSumaResta(3 , - 2) != 0
    
# Multiplicación
    
def test_calculadoraMultiplicación_1():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(2 , 2) == 4

def test_calculadoraMultiplicación_2():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(2 , -2) == -4
    
def test_calculadoraMultiplicación_3():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(1.5 , 2) == 3
    
def test_calculadoraMultiplicación_4():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(1.5 , 3) == 4.5
    
def test_calculadoraMultiplicación_5():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(-2 , -2) == 4
    
def test_calculadoraMultiplicación_6():
    calculadora = Calculadora()
    assert calculadora.calculadoraMultiplicacion(10**10 , 2) == 2 * (10**10)

# Division

def test_calculadoraDivision_1():
    calculadora = Calculadora()
    assert calculadora.calculadoraDivision(2 , 2) == 1

def test_calculadoraDivision_2():
    calculadora = Calculadora()
    assert calculadora.calculadoraDivision(4 , -2) == -2
    
def test_calculadoraDivision_3():
    calculadora = Calculadora()
    assert calculadora.calculadoraDivision(-4 , 2) == -2
    
def test_calculadoraDivision_4():
    calculadora = Calculadora()
    assert calculadora.calculadoraDivision(3 , 2) == 1.5
    
def test_calculadoraDivision_5():
    calculadora = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calculadora.calculadoraDivision(2, 0)

def test_calculadoraDivision_6():
    calculadora = Calculadora()
    assert calculadora.calculadoraDivision(0 , 2) == 0