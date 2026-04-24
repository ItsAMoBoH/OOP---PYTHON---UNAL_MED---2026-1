class Persona:
    def __init__(self, nombre, apellido, num_doc, ano_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = num_doc
        self.ano_nacimiento = ano_nac

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Número de documento de identidad: {self.documento}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")



def pedir_datos():
    print("\nA continuación se pedirá información de una persona:")
    nombre = input("Ingrese el nombre de la persona --> ").strip().capitalize()
    apellido = input("Ingrese el apellido de la persona --> ").strip().capitalize()
    documento = input("Ingrese el número de documento de identidad de la persona --> ").strip()
    ano_nac = int(input("Ingrese el año de nacimiento de la persona --> ").strip())

    return nombre, apellido, documento, ano_nac

def main():
    nombre1, apellido1, documento1, ano_nac1 = pedir_datos()
    nombre2, apellido2, documento2, ano_nac2 = pedir_datos()

    persona1 = Persona(nombre1, apellido1, documento1, ano_nac1)
    persona2 = Persona(nombre2, apellido2, documento2, ano_nac2)
    
    print("\nA continuación se mostrarán datos de las personas registradas:")
    persona1.mostrar_datos()
    persona2.mostrar_datos()

if __name__ == "__main__":
    main()