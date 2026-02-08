# Hacer un seguimiento (prueba de escritorio) del siguiente grupo de instrucciones.
# INICIO
# SUMA = 0
# X = 20
# SUMA = SUMA + X
# Y = 40
# X = X + Y ** 2
# SUMA = SUMA + X / Y
# ESCRIBA: “EL VALOR DE LA SUMA ES:”, SUMA
# FIN_INICIO

# Algoritmo base:

# suma = 0
# x = 20
# suma += x
# y = 40
# x += y**2
# suma += x/y
# print(f"El valor de la suma es: {suma}")



# Código usando OOP

class AlgoritmoSuma:
    def __init__(self, suma, x, y):
        self.suma = suma
        self.x = x
        self.y = y

    def algoritmo(self):
        self.suma += self.x
        self.x += self.y**2
        self.suma += self.x/self.y

    def mostrarResultado(self):
        print(f"El valor de la suma es: {self.suma}")
        print(f"El valor de x es: {self.x}")
        print(f"El valor de y es: {self.y}")

suma = 0
x = 20
y = 40
operacion = AlgoritmoSuma(suma, x, y)
operacion.algoritmo()
operacion.mostrarResultado()
