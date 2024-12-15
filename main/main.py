
class Calculadora():
    def calculadoraSumaResta(self, a , b):
        return a + b
    
    def calculadoraMultiplicacion(self , a , b):
        return a * b
    
    def calculadoraDivision(self , a , b):
        return a / b

if __name__ == "__main__":
    calculadora = Calculadora()
    prueba_calculadora = calculadora.calculadoraSumaResta(a = 3, b = 2)
    print(prueba_calculadora)