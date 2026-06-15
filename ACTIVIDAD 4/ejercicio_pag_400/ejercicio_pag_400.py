import tkinter as tk
from tkinter import messagebox

class PruebaExcepciones():
    def __init__(self):
        self._ventana = tk.Tk()
        self._ventana.title("Prueba Manejo Excepciones")
        self._ventana.geometry("500x300")

        self._texto_bonis = tk.Label(self._ventana, text = "Ingrese los valores necesarios para realizar una división")
        self._texto_bonis.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)

        self._campos = []
        self._labels = []

        for i in range(2):
            if i == 0:
                label = tk.Label(self._ventana, text = "Dividendo")
            else:
                label = tk.Label(self._ventana, text = "Divisor")

            label.grid(row = 1 + i, column = 0, padx = 10, pady = 10, columnspan = 2)

            campo = tk.Entry(self._ventana)
            campo.grid(row = 1 + i, column = 2, padx = 10, pady = 10, columnspan = 2)

            self._campos.append(campo)

        for i in range(2):
            if i == 0:
                label = tk.Label(self._ventana, text = "Cociente")
            else:
                label = tk.Label(self._ventana, text = "")
            label.grid(row = 3, column = 2*i, padx = 10, pady = 10, columnspan = 2)

            self._labels.append(label)

        self._botones = []

        funciones = {"Calcular": self.calcular, "Limpiar": self.limpiar, "Romper": self.romper}

        for i, (clave, valor) in enumerate(funciones.items()):
            boton = tk.Button(self._ventana, text = clave, command = valor, bg = ["green", "red", "blue"][i], fg = "white")
            boton.grid(row = 4, column = i, padx = 10, pady = 10)

            self._botones.append(boton)

    def obtener_datos(self):
        try:
            valores = []
            for campo in self._campos:
                valor = float(campo.get().strip())
                valores.append(valor)
            if valores[1] == 0:
                raise ValueError("No es posible dividir entre cero")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        messagebox.showinfo("Info", "Datos obtenidos correctamente")
        return valores
    
    def mostrar_datos(self, datos):
        label = self._labels[1]
        label.config(text = datos)
    
    def calcular(self):
        valores = self.obtener_datos()

        if valores is None:
            return
        cociente = valores[0] / valores [1]

        self.mostrar_datos(cociente)

    def limpiar(self):
        for i in self._campos:
            i.delete(0, tk.END)
        self._labels[1].config(text = "")

    def romper(self):
        nada = None
        try:
            nada.get()

        except AttributeError:
            messagebox.showerror("Error", "No puedes usar una función de algo que no está creado\n¡Felicidades!")
        finally:
            messagebox.showinfo("Aviso", "La ejecución de \"Romper\" ha terminado")
    
    def ejecutar(self):
        self._ventana.mainloop()

def main():
    app = PruebaExcepciones()
    app.ejecutar()

if __name__ == "__main__":
    main()


    