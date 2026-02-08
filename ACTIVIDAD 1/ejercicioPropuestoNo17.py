# Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud
# de la circunferencia.

import math as mt

# Algoritmo base

# radio = float(input("Ingrese el valor del radio de la circunferencia --> "))
# circunferencia = mt.pi * radio * 2
# area = mt.pi * radio**2
# print(f"Para la circunferencia de radio {radio}, su longitud es {circunferencia}")
# print(f"Para el círculo de radio {radio}, su área es {area}")

# Código usando OOP

class Circunferencia:
    @staticmethod
    def pedir_radio():
        radio = float(input("Ingrese el radio de una circunferencia/círculo a continuación --> "))
        return radio

    def __init__(self, radio):
        self.radio = radio

    def calcular_area_y_circunferencia(self):
        self.area = self.radio**2 * mt.pi
        self.circunferencia = 2 * mt.pi * self.radio
    
    def mostrar_medidas(self):
        print(f"Para la circunferencia de radio {self.radio}, su longitud es {self.circunferencia}")
        print(f"Para el círculo de radio {self.radio}, su área es {self.area}")


radio = Circunferencia.pedir_radio()
bolita = Circunferencia(radio)
bolita.calcular_area_y_circunferencia()
bolita.mostrar_medidas()