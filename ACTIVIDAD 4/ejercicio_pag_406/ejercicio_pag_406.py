import tkinter as tk
from tkinter import messagebox

class Vendedor():
    def __init__(self, nombre = "Jhon", apellidos = "Doe", edad = 0):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad

    def verificar_edad(self, edad):
        if edad is None:
            return
        
        if edad <0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        elif edad < 18:
            raise ValueError("El vendedor debe ser mayor de edad")
        
    def imprimir(self):
        return (self._nombre, self._apellidos, self._edad)
    
class VentanaVendedor():
    def __init__(self):
        self._ventana = tk.Tk()
        self._ventana.title("Configuración de vendedores")
        self._ventana.geometry("400x300")

        self._texto_bonis = tk.Label(self._ventana, text = "Ingrese los datos del vendedor")
        self._texto_bonis.grid(row = 0, column = 0, padx = 10, pady = 10)

        datos = ["Nombre:", "Apellidos:", "Edad:"]

        self._campos = []

        for i in range(len(datos)):
            label = tk.Label(self._ventana, text = datos[i])
            label.grid(row = 1 + i, column = 0, padx = 10, pady = 10)

            campo = tk.Entry(self._ventana)
            campo.grid(row = 1 + i, column = 1, columnspan = 2, padx = 10, pady = 10)

            self._campos.append((label, campo))
            
        botones = {"Verificar": self.verificar, "Imprimir": self.imprimir, "Limpiar": self.limpiar}

        for i, (clave, valor) in enumerate(botones.items()):
            boton = tk.Button(self._ventana, text = clave, command = valor, bg = ["green", "blue", "red"][i], fg = "white")
            boton.grid(row = 4, column = i, padx = 10, pady = 10)

        
        self._vendedor = None

    def obtener_datos(self):
        try:
            valores = []
            for (label, campo) in self._campos:
                if label.cget("text") in ("Nombre:", "Apellidos:"):
                    valor = campo.get().strip().capitalize()
                else:
                    valor = int(campo.get().strip())
                valores.append(valor)
        except ValueError:
                messagebox.showerror("Error", "Ha ingresado datos inválidos")
                return
        
        return valores

    def limpiar(self):
        for (label, campo) in self._campos:
            campo.delete(0, tk.END)
        self._vendedor = None
        messagebox.showinfo("Aviso", "Ha liberado exitosamente 2TB de información\n¡Que alivio!")
    
    def verificar(self):
        valores = self.obtener_datos()
        if valores is None:
            return
        
        self._vendedor = Vendedor(*valores)

        try:
            self._vendedor.verificar_edad(valores[2])
            messagebox.showinfo("Aviso", "Ha creado exitosamente un vendedor\nPobre esclavo del capitalismo")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
    
    def imprimir(self):
        if self._vendedor is None:
            messagebox.showerror("Error", "Primero cree un vendedor")
            return
        datos = self._vendedor.imprimir()
        messagebox.showinfo("Datos del vendedor", f"Nombre: {datos[0]}\nApellidos: {datos[1]}\nEdad: {datos[2]}")

    def ejecutar(self):
        self._ventana.mainloop()

def main():
    app = VentanaVendedor()
    app.ejecutar()

if __name__ == "__main__":
    main()


        
        