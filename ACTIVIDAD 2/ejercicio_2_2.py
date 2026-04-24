from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre = None, satelites = 0, masa = float(0), volumen = float(0), diametro = float(0), distancia_sol = float(0), tipo = None, observable = False):
        
        self.nombre = nombre
        self.satelites = satelites
        self.masa =  masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable

    def calcular_densidad(self):
        return self.masa / self.volumen

    def planeta_exterior(self):
        UA = 149.59787
        return (self.distancia_sol / UA) > 3.4
    
    def mostrar_informacion(self):
        print("\nA continuación se dará información acerca del planeta: ")
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Número de satélites: {self.satelites}")
        print(f"Masa del planeta: {self.masa}")
        print(f"Volumen del planeta: {self.volumen}")
        print(f"Diámetro del planeta: {self.diametro}")
        print(f"Tipo del planeta: {self.tipo.name.capitalize()}")
        if self.observable:
            print("El planeta es observable a simple vista")
        else:
            print("El planeta no es observable a simple vista")

def pedir_datos():
    print("\nA continuación se pedirá información de un planeta:")
    nombre = input("Ingrese el nombre del planeta --> ").strip().capitalize()
    satelites = int(input("Ingrese el número de satélites con los que cuenta el planeta --> "))
    masa = float(input("Ingrese la masa del planeta --> "))
    volumen = float(input("Ingrese volumen del planeta --> "))
    diametro = float(input("Ingrese la medida del diámetro del planeta --> "))
    distancia_sol = float(input("Ingrese la distancia desde el planeta al sol --> "))
    while True:
        tipo_input = input(
        "Ingrese el tipo de planeta (GASEOSO, ENANO, TERRESTRE) --> " ).strip().upper()
    
        try:
            tipo = TipoPlaneta[tipo_input]
            break
        except KeyError:
            print("Tipo incorrecto, intente nuevamente.")
    while True:
        observable = input("¿El planeta es observable a simple vista? Ingrese \"s\" si lo es, y \"n\" si no es el caso, a continuación --> ").strip().lower()
        if observable != "s" and observable != "n":
            print("No ha ingresado un dato correcto, intente de nuevo")
        else:
            if observable == "s":
                observable = True
            else: 
                observable = False
            break
    return nombre, satelites, masa, volumen, diametro, distancia_sol, tipo, observable

def main():
    nombre1, satelites1, masa1, volumen1, diametro1, distancia_sol1, tipo1, observable1 = pedir_datos()
    nombre2, satelites2, masa2, volumen2, diametro2, distancia_sol2, tipo2, observable2 = pedir_datos()

    planeta1 = Planeta(nombre1, satelites1, masa1, volumen1, diametro1, distancia_sol1, tipo1, observable1)
    planeta2 = Planeta(nombre2, satelites2, masa2, volumen2, diametro2, distancia_sol2, tipo2, observable2)

    planeta1.mostrar_informacion()
    planeta2.mostrar_informacion()

    print(f"La densidad de {planeta1.nombre} es: {planeta1.calcular_densidad()}")
    if planeta1.planeta_exterior():
        print(f"{planeta1.nombre} es un planeta exterior al sistema solar")
    else:
        print(f"{planeta1.nombre} no es un planeta exterior al sistema solar")

    print(f"La densidad de {planeta2.nombre} es: {planeta2.calcular_densidad()}")
    if planeta2.planeta_exterior():
        print(f"{planeta2.nombre} es un planeta exterior al sistema solar")
    else:
        print(f"{planeta2.nombre} no es un planeta exterior al sistema solar")


if __name__ == "__main__":
    main()