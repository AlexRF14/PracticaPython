
class Calculadora():
    def calculadora(self, a , b):
        return a + b

if __name__ == "__main__":
    calculadora = Calculadora()
    prueba_calculadora = calculadora.calculadora(a = 3, b = 2)
    print(prueba_calculadora)