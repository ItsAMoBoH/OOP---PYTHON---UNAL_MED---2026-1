from enum import Enum

class Color(Enum):
    blanco = 1
    negro = 2
    rojo = 3
    naranja = 4
    amarillo = 5
    verde = 6
    azul = 7
    violeta = 8

class TipoCombustible(Enum):
    gasolina = 1
    bioetanol = 2
    diesel = 3
    biodiesel = 4
    gas_natural = 5

class TipoAutomovil(Enum):
    carro_ciudad = 1
    subcompacto = 2
    compacto = 3
    familiar = 4
    ejecutivo = 5
    suv = 6


class Automovil:
    def __init__(self, marca = None, modelo=None, motor=None, tipoCombustible = None , tipoAutomovil = None, numeroPuertas=0, cantidadAsientos=0, velocidadMaxima=0.0, color = None, velocidadActual=0.0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMaxima = velocidadMaxima
        self.color = color
        self.velocidadActual = velocidadActual

    def acelerar(self, velocidadAcelerar):
        if self.velocidadActual + velocidadAcelerar > self.velocidadMaxima:
            raise ValueError("No se puede acelerar más que la velocidad máxima del automóvil")
        self.velocidadActual += velocidadAcelerar
        print(f"La velocidad actual del automóvil es: {self.velocidadActual}")

    def desacelerar(self, velocidadDesacelerar):
        if self.velocidadActual - velocidadDesacelerar < 0:
            raise ValueError("No se puede desacelerar menos que 0 km/h")
        self.velocidadActual -= velocidadDesacelerar
        print(f"La velocidad actual del automóvil es: {self.velocidadActual}")

    def frenar(self):
        self.velocidadActual = 0
        print(f"La velocidad actual del automóvil es: {self.velocidadActual}")

    def tiempoEstimado(self, distancia):
        return distancia / self.velocidadActual
    
    def mostrarAtributos(self):
        print("\nA continuación se mostrarán los datos asociados al vehículo:")
        print(f"Marca del automóvil: {self.marca}")
        print(f"Modelo del automóvil: {self.modelo}")
        print(f"Motor del automóvil: {self.motor}")
        print(f"Tipo de combustible del automóvil: {self.tipoCombustible.name}")
        print(f"Tipo del automóvil: {self.tipoAutomovil.name}")
        print(f"Número de puertas del automóvil: {self.numeroPuertas}")
        print(f"Cantidad de asientos del automóvil: {self.cantidadAsientos}")
        print(f"Velocidad máxima del automóvil: {self.velocidadMaxima}")
        print(f"Color del automóvil: {self.color.name}")
        print(f"Velocidad actual del automóvil {self.velocidadActual}")


def pedirDatos():
    print("\nA continuación se pedirá información acerca de un automóvil:")
    marca = input("Ingrese la marca del automóvil --> ").strip()
    modelo = input("Ingrese el modelo del automóvil --> ").strip()
    motor = input("Ingrese el motor del automóvil --> ").strip()
    while True:
        tipo_input = input(
        "Ingrese el tipo de combustible (gasolina, bioetanol, diesel, biodiesel, gas_natural) --> " ).strip().lower()
    
        try:
            tipoCombustible = TipoCombustible[tipo_input]
            break
        except KeyError:
            print("Tipo incorrecto, intente nuevamente.")
    while True:
        tipo_input = input(
        "Ingrese el tipo de automóvil (carro_ciudad, subcompacto, compacto, familiar, ejecutivo, suv) --> " ).strip().lower()
    
        try:
            tipoAutomovil = TipoAutomovil[tipo_input]
            break
        except KeyError:
            print("Tipo incorrecto, intente nuevamente.")

    numeroPuertas = int(input("Ingrese el número de puertas del automóvil --> "))
    cantidadAsientos = int(input("Ingrese la cantidad de asientos del automóvil --> "))
    velocidadMaxima = float(input("Ingrese la velocidad máxima del automóvil --> "))
    
    while True:
        tipo_input = input("Ingrese el color del automóvil (blanco, negro, rojo, naranja, amarillo, verde, azul, violeta) --> " ).strip().lower()
    
        try:
            color = Color[tipo_input]
            break
        except KeyError:
            print("Color incorrecto, intente nuevamente.")

    velocidadActual = float(input("Ingrese la velocidad actual del automóvil --> "))
    return marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMaxima, color, velocidadActual

def main():
    marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMaxima, color, velocidadActual = pedirDatos()
    automovil = Automovil(marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMaxima, color, velocidadActual)

    automovil.mostrarAtributos()

    # Variaciones de velocidad
    automovil.velocidadActual = 100
    automovil.acelerar(20)
    automovil.desacelerar(50)
    automovil.frenar()

if __name__ == "__main__":
    main()
