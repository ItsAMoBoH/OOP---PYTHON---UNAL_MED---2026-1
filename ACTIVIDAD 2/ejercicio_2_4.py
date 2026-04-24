import math as mt
from enum import Enum

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return mt.pi * self.radio**2
    
    def perimetro(self):
        return 2 * mt.pi * self.radio
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * self.base + 2 * self.altura
    
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2
    
    def perimetro(self):
        return self.lado * 4
    

class TipoTriangulo(Enum):
    Equilatero = 1
    Isoceles = 2
    Escaleno = 3

class TrianguloRectangulo:
    def __init__(self, cateto_a, cateto_b):
        self.cateto_a = cateto_a
        self.cateto_b= cateto_b

    def area(self):
        return self.cateto_b * self.cateto_a / 2
    
    @property
    def hipotenusa(self):
        return mt.sqrt(self.cateto_a**2 + self.cateto_b**2)
    
    def perimetro(self):
        return self.cateto_b + self.cateto_a + self.hipotenusa
    
    @property
    def tipo_triangulo(self):
        if self.cateto_a == self.cateto_b == self.hipotenusa:
            return TipoTriangulo.Equilatero
        elif self.cateto_a == self.cateto_b != self.hipotenusa:
            return TipoTriangulo.Isoceles
        else:
            return TipoTriangulo.Escaleno
        
def pedir_datos():
    print("\nA continuación se pedirán datos acerca de algunas figuras geométricas:")

    while True:
        try:
            radio = float(input("Ingrese la medida del radio de una circunferencia --> "))
            if radio <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Ha ingresado un valor incorrecto, intente nuevamente")
            print()

    while True:
        try:
            base = float(input("Ingrese la medida de la base de un rectángulo --> "))
            altura = float(input("Ingrese la medida de la altura de un rectángulo --> "))
            if base <= 0 or altura <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Ha ingresado un valor incorrecto, intente nuevamente")
            print()

    while True:
        try:
            lado = float(input("Ingrese la medida del lado de un cuadrado --> "))
            if lado <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Ha ingresado un valor incorrecto intente nuevamente")
            print()

    while True:
        try:
            cateto_a = float(input("Ingrese la medida de un cateto de un triángulo rectángulo --> "))
            cateto_b = float(input("Ingrese la medida de otro cateto de un triángulo rectángulo --> "))
            if cateto_a <= 0 or cateto_b <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Ha ingresado un valor incorrecto, intente nuevamente")

    return radio, base, altura, lado, cateto_a, cateto_b

def main():
    radio, base, altura, lado, cateto_a, cateto_b = pedir_datos()
    bolita = Circulo(radio)
    rectangulo = Rectangulo(base, altura)
    cuadrado = Cuadrado(lado)
    triangulo = TrianguloRectangulo(cateto_a, cateto_b)

    # Mostrar valores
    print(f"\nEl área del círculo es: {bolita.area()}")
    print(f"El perímetro de la circunferencia es: {bolita.perimetro()}")

    print(f"\nEl área del rectángulo es: {rectangulo.area()}")
    print(f"El perímetro del rectángulo es: {rectangulo.perimetro()}")
    
    print(f"\nEl área del cuadrado es: {cuadrado.area()}")
    print(f"El perímetro del cuadrado es: {cuadrado.perimetro()}")

    print(f"\nLa medida de la hipotenusa del triángulo rectángulo es: {triangulo.hipotenusa}")
    print(f"El área del triángulo rectángulo es: {triangulo.area()}")
    print(f"El perímetro del triángulo rectángulo es: {triangulo.perimetro()}")
    print(f"Este triángulo es un triángulo {triangulo.tipo_triangulo.name}")


if __name__ == "__main__":
    main()
