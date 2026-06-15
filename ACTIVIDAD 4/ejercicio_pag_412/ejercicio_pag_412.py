import numpy as np
import tkinter as tk
from tkinter import messagebox

class CalculosNumericos():
    def logaritmo(self, n):
        if n <= 0:
            raise ValueError("No es posible calcular el logaritmo de un número negativo, o cero")
        return np.log(n)
    
    def raiz(self, n):
        if n < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo en los reales")
        return(np.sqrt(n))
    
class VentanaBase(CalculosNumericos):
    def __init__(self):
        # Configuración Genérica
        self._ventana = tk.Tk()
        self._ventana.title("Operaciones Matemáticas")
        self._ventana.geometry("500x200")
        self._ventana.resizable(False, False)
        self._texto_indice = tk.Label(self._ventana, text= "Calculadora de logaritmos y raices cuadradas")
        self._texto_indice.grid(row = 0, column = 0, pady = 10)

        # Botones
        self._calcular_raiz_boton = tk.Button(self._ventana, text="Calcular raiz", command = self.calcular_raiz, bg = "green", fg = "white")
        self._calcular_raiz_boton.grid(row = 2, column=1, columnspan=1, pady=10)

        self._calcular_logaritmo_boton = tk.Button(self._ventana, text="Calcular logaritmo", command = self.calcular_logaritmo, bg = "cyan", fg = "Black")
        self._calcular_logaritmo_boton.grid(row = 2, column=0, columnspan=1, pady=10)

        self._limpiar_boton = tk.Button(self._ventana, text = "Limpiar", command = self.limpiar, bg = "red", fg = "white")
        self._limpiar_boton.grid(row = 2, column = 2, pady = 10)

        self._campos = []
        self._metricas_label = []

        label_entry = tk.Label(self._ventana, text = "Ingrese el número n:")
        label_entry.grid(row = 1, column = 0, padx = 10, pady = 10)

        numero_entry = tk.Entry(self._ventana)
        numero_entry.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        self._campos.append((label_entry, numero_entry))

        for i in range(2):
            label = tk.Label(self._ventana, text = "")
            label.grid(row = 3, column = i, padx = 10, pady = 10)
            
            self._metricas_label.append(label)

    def obtener_datos(self):
        try:
            numero = float(self._campos[0][1].get().strip())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos")
            return
        
        return numero
    
    def calcular_logaritmo(self):
        numero = self.obtener_datos()
        if numero is None:
            return
        
        try:
            logaritmo = self.logaritmo(numero)
        except ValueError as e:
            messagebox.showerror("Error", e)
            return

        self.mostrar_resultados(("Logaritmo", logaritmo))

    def calcular_raiz(self):
        numero = self.obtener_datos()
        if numero is None:
            return
        
        try:
            raiz = self.raiz(numero)
        except ValueError as e:
            messagebox.showerror("Error", e)
            return

        self.mostrar_resultados(("Raiz:", raiz))

    def mostrar_resultados(self, resultados):
        for i, label in enumerate(self._metricas_label):
            label.config(text = resultados[i])

    def limpiar(self):
        for label in self._metricas_label:
            label.config(text = "")

        for (label, entry) in self._campos:
            entry.delete(0, tk.END)

    def ejecutar(self):
        self._ventana.mainloop()

def main():
    app = VentanaBase()
    app.ejecutar()

if __name__ == "__main__":
    main()
