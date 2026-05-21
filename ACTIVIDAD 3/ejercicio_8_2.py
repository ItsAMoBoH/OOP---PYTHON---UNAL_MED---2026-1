import tkinter as tk
from tkinter import messagebox
import math as mt

class VentanaNotas:
    def __init__(self, titulo):
        self._ventana = tk.Tk()
        self._ventana.title(titulo)
        self._ventana.geometry("350x400")
        self._texto_indice = tk.Label(self._ventana, text= "Ingrese el valor de las 5 notas")
        self._texto_indice.grid(row = 0, column = 0)
        self._campos = []
        for i in range(5):
            etiqueta = tk.Label(self._ventana, text=f"Nota {i+1}:")
            etiqueta.grid(row = i + 1, column = 0, pady = 5, padx = 10)
            
            campo = tk.Entry(self._ventana)
            campo.grid(row= i + 1, column = 1 , pady = 5, padx = 10)
            
            self._campos.append(campo)

        self._calcular_boton = tk.Button(self._ventana, text="Calcular", command = self.calcular)
        self._calcular_boton.grid(row = 6, column=0, columnspan=1, pady=10)

        self._limpiar_boton = tk.Button(self._ventana, text = "Limpiar", command = self.limpiar)
        self._limpiar_boton.grid(row = 6, column = 1, pady = 10)

        self._metricas_label = []
        for i in range(4):
            metrica = tk.Label(self._ventana, text="")
            metrica.grid(row = 7 + i, column = 0, pady = 5, padx = 10)

            valor = tk.Label(self._ventana, text="")
            valor.grid(row = 7 + i, column = 1, pady = 5, padx = 10)
            self._metricas_label.append((metrica, valor))
            
    
    def calcular(self):
        notas = []
        for campo in self._campos:
            try:
                valor = float(campo.get())
                if valor < 0:
                    raise ValueError
                elif valor > 5:
                    raise ValueError
                notas.append(valor)
            except ValueError:
                messagebox.showerror("Error", "Ingresa solo números positivos menores que 5")
                return
            
        promedio = sum(notas) / len(notas)
        desviacion = mt.sqrt(sum((x-promedio)**2 for x in notas) / len(notas))
        maxima = max(notas)
        minima = min(notas)
        valores = (promedio, desviacion, maxima, minima)
        metricas = ("Promedio", "Desviación Estándar", "Nota Máxima", "Nota Mínima")
        for i, (metrica_label, valor_label) in enumerate(self._metricas_label):
            metrica_label.config(text = metricas[i])
            valor_label.config(text = f"{valores[i]:.2f}")

    def ejecutar(self):
        self._ventana.mainloop()

    def limpiar(self):
        for i, (metrica_label, valor_label) in enumerate(self._metricas_label):
            metrica_label.config(text = "")
            valor_label.config(text = "")
        for campo in self._campos:
            campo.delete(0, tk.END)


def main():
    ventana = VentanaNotas("Calculador de Métricas de Notas")
    ventana.ejecutar()

if __name__ == "__main__":
    main()