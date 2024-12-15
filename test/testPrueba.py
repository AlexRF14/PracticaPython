import sys
sys.path.append(".")
from main.main import Calculadora

def test_calculadora():
    calculadora = Calculadora()
    assert calculadora.calculadora(3 , 2) == 5
