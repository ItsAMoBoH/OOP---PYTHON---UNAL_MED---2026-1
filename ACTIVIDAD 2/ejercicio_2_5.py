from enum import Enum

class TipoCuenta(Enum):
    Ahorros = 1
    Corriente = 2

class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_de_cuenta, tipo_cuenta, saldo = 0):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_de_cuenta = numero_de_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def mostrar_datos(self):
        print("\nA continuación se mostrará la información de la cuenta")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de cuenta: {self.numero_de_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.name}")
        print(f"Saldo actual: {self.saldo}")

    def consultar_saldo(self):
        print(f"\nEl saldo actual de la cuenta de {self.nombres} es: {self.saldo}")

    def consignar(self, valor):
        self.saldo += valor
        self.consultar_saldo()
    
    def retirar(self, valor):
        if self.saldo - valor < 0:
            print(f"No es posible retirar más dinero del que se tiene actualmente")
        else:
            self.saldo -= valor

        self.consultar_saldo()


def pedir_datos():
    print("\nA continuación se pedirán datos de una cuenta bancaria:")
    nombres = input("Ingrese sus nombres a continuación --> ")
    apellidos = input("Ingrese sus apellidos a continuación --> ")
    while True:
        try:
            numero_cuenta = int(input("Ingrese el número de cuenta a continuación --> "))
            if numero_cuenta <= 0:
                raise ValueError("No puede tener un número de cuenta que sea un número negativo o cero")
            break
        except ValueError:
            print("Ha ingresado un número de cuenta inválido, intente nuevamente")
            print()
    while True:
        tipo_cuenta = input("Ingrese su tipo de cuenta a continuación (ahorros o corriente) --> ").strip().capitalize()
        if tipo_cuenta not in ("Ahorros", "Corriente"):
            print("\nHa ingresado un tipo de cuenta incorrecto, intente nuevamente")
            print()
            continue
        tipo_cuenta = TipoCuenta[tipo_cuenta]
        break

    while True:
        try:
            saldo = float(input("Ingrese su saldo actual en la cuenta --> "))
            if saldo < 0:
                raise ValueError()
            break
        except ValueError:
            print("\nHa ingresado un saldo incorrecto, intente nuevamente")
            print()

    return nombres, apellidos, numero_cuenta, tipo_cuenta, saldo

def main():
    nombres, apellidos, numero_cuenta, tipo_cuenta, saldo = pedir_datos()

    cuentaA = CuentaBancaria(nombres, apellidos, numero_cuenta, tipo_cuenta, saldo)

    cuentaA.mostrar_datos()

    cuentaA.consignar(200000)
    cuentaA.retirar(10e150)
    cuentaA.retirar(0.5)


if __name__ == "__main__":
    main()