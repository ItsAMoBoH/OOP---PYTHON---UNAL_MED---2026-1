# Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
# retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
# la retención en la fuente y el salario neto del trabajador.


# Algoritmo base
# num_horas_trabajo = 48
# salario_hora = 5000
# porcentaje_retefuente = 12.5
# salario_bruto = num_horas_trabajo * salario_hora
# retefuente = salario_bruto * porcentaje_retefuente/100
# salario_neto = salario_bruto - retefuente
# print(salario_neto)

# Código usando OOP

class Salario:
    def __init__(self, salario_hora, porcentaje_retefuente, num_horas_trabajo):
        self.salario_hora = salario_hora
        self.porcentaje_retefuente = porcentaje_retefuente
        self.num_horas_trabajo = num_horas_trabajo

    def calcular_datos_salario(self):
        self.salario_bruto = self.salario_hora * self.num_horas_trabajo
        self.retefuente = self.salario_bruto * self.porcentaje_retefuente / 100
        self.salario_neto = self.salario_bruto - self.retefuente

    def mostrar_datos(self):
        print(f"El salario bruto del empleado es: {self.salario_bruto}")
        print(f"La retención a la fuente del empleado es: {self.retefuente}")
        print(f"El salario neto del empleado es: {self.salario_neto}")


num_horas_trabajo = float(48)
salario_hora = float(5000)
porcentaje_retefuente = 12.5

info_salario = Salario(salario_hora, porcentaje_retefuente, num_horas_trabajo)
info_salario.calcular_datos_salario()
info_salario.mostrar_datos()