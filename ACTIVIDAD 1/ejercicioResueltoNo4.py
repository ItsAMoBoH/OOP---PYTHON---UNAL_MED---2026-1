# A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
# edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
# la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro.


# Algoritmo Base:
# edad_juan = float(input("Ingrese la edad de Juan --> "))
# edad_alberto = 2/3 * edad_juan
# edad_ana = 4/3 * edad_juan
# edad_mama = edad_juan + edad_alberto + edad_ana

# print("Las edades son:")
# print(f"Alberto: {edad_alberto}, Juan: {edad_juan}, Ana: {edad_ana}, Mamá: {edad_mama}")


# Código usando OOP:


class Familia:
    def __init__(self, edad_base):
        self.edad_juan = edad_base
    
    def calcular_edades(self):
        self.edad_alberto = self.edad_juan * 2/3
        self.edad_ana = self.edad_juan * 4/3
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_edades(self):
        print("Las edades son:")
        print(f"Alberto: {self.edad_alberto}, Juan: {self.edad_juan}, Ana: {self.edad_ana}, Mamá: {self.edad_mama}")


edad_juan = float(input("Ingrese la edad de Juan --> "))
familia = Familia(edad_juan)
familia.calcular_edades()
familia.mostrar_edades()