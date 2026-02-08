# Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.

# Algoritmo base

# numero = float(input())
# n2 = numero ** 2
# n3 = numero ** 3
# print(f"El número escogido fue: {numero}, su cuadrado es: {n2} y su cubo es: {n3}")


# Ejercicio usando OOP

class Potencias:
    @staticmethod
    def pedir_numero():
        numero = float(input("Ingrese un número a continuación --> "))
        return numero
    
    @staticmethod
    def calcular_potencias(n):
        cuadrado = n**2
        cubo = n**3
        return cuadrado, cubo
    
    @staticmethod
    def mostrar_potencias(n,cua, cub):
        print(f"El número escogido fue: {n}, su cuadrado es: {cua} y su cubo es: {cub}")


numero = Potencias.pedir_numero()
cuadrado, cubo = Potencias.calcular_potencias(numero)

Potencias.mostrar_potencias(numero, cuadrado, cubo)