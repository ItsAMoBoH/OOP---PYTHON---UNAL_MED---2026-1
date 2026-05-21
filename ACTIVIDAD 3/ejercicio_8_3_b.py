import numpy as mt
import tkinter as tk
from tkinter import messagebox

class CuerpoGeometrico:
    def calcular_volumen(self):
        raise NotImplementedError
    
    def calcular_area_superficial(self):
        raise NotImplementedError


class Cilindro(CuerpoGeometrico):
    def __init__(self, radio, altura):
        self._radio = radio
        self._altura = altura

    def calcular_volumen(self):
        return mt.pi * self._radio**2 * self._altura
    
    def calcular_area_superficial(self):
        return mt.pi * 2 * self._radio * self._altura + 2 * mt.pi * self._radio **2
    
class Esfera(CuerpoGeometrico):
    def __init__(self, radio):
        self._radio = radio

    def calcular_volumen(self):
        return 4/3 * self._radio**3 * mt.pi
    
    def calcular_area_superficial(self):
        return 4 * mt.pi * self._radio**2

class Piramide(CuerpoGeometrico):
    def __init__(self, lado_base, altura, apotema):
        self._lado_base = lado_base
        self._altura = altura
        self._apotema = apotema

    def calcular_volumen(self):
        return 1/3 * self._lado_base**2 * self._altura
    
    def calcular_area_superficial(self):
        return 2 * self._apotema * self._lado_base + self._lado_base**2
    
class VentanaPrincipal:
    def __init__(self):
        # Configuración Genérica
        self._ventana = tk.Tk()
        self._ventana.title("Constructor de Sólidos Geométricos")
        self._ventana.geometry("350x150")
        self._ventana.resizable(False, False)
        self._texto_indice = tk.Label(self._ventana, text= "Escoja una figura para modelar")
        self._texto_indice.grid(row = 0, column = 0, pady = 10, columnspan = 3)

        # Botones
        i = 0
        self._cilindro_boton = tk.Button(self._ventana, text = "Cilindro", command = self.abrir_cilindro)
        self._cilindro_boton.grid(row = 1, column=i, columnspan=1, pady=10, padx = 10)
        self._esfera_boton = tk.Button(self._ventana, text = "Esfera", command = self.abrir_esfera)
        self._esfera_boton.grid(row = 1, column=i+1, columnspan=1, pady=10, padx = 10)
        self._piramide_boton = tk.Button(self._ventana, text = "Pirámide", command = self.abrir_piramide)
        self._piramide_boton.grid(row = 1, column=i+2, columnspan=1, pady=10, padx = 10)


    def abrir_cilindro(self):
        VentanaCilindro()

    def abrir_esfera(self):
        VentanaEsfera()

    def abrir_piramide(self):
        VentanaPiramide()

    def ejecutar(self):
        self._ventana.mainloop()

class VentanaBase:
    def __init__(self, titulo):
        # Configuración Genérica
        self._ventana = tk.Toplevel()
        self._ventana.title(titulo)
        self._ventana.geometry("500x350")
        self._ventana.resizable(False, False)
        self._texto_indice = tk.Label(self._ventana, text= "Constructor de Sólidos Geométricos")
        self._texto_indice.grid(row = 0, column = 0, pady = 10)

        # Botones
        self._calcular_boton = tk.Button(self._ventana, text="Calcular", command = self.calcular)
        self._calcular_boton.grid(row = 5, column=0, columnspan=1, pady=10)

        self._limpiar_boton = tk.Button(self._ventana, text = "Limpiar", command = self.limpiar)
        self._limpiar_boton.grid(row = 5, column = 1, pady = 10)

        self._campos = []
        self._metricas_label = []

        for i in range(2):
            etiqueta = tk.Label(self._ventana, text = "")
            etiqueta.grid(column = 0, row = 6 + i, pady = 10)

            valor = tk.Label(self._ventana, text = "")
            valor.grid(column = 1, row = 6 + i, pady = 10)

            self._metricas_label.append((etiqueta, valor))
            

    def calcular(self):
        datos = self.obtener_datos()
        if datos is None:
            return
        figura = self.crear_figura(datos)
        volumen = figura.calcular_volumen()
        area = figura.calcular_area_superficial()
        self.mostrar_resultados(volumen, area)

    def mostrar_resultados(self, volumen, area):
        labels = ["Volumen", "Área Superficial"]
        valores = [volumen, area]

        for i, (label, campo) in enumerate(self._metricas_label):
            label.config(text = labels[i])
            campo.config(text = f"{valores[i]:.2f} cm^{3 - i}")

    def limpiar(self):
        for i, (label, campo) in enumerate(self._metricas_label):
            label.config(text = "")
            campo.config(text = "")
        for campo in self._campos:
            campo.delete(0, tk.END)
    
    def obtener_datos(self):
        raise NotImplementedError
    
    def crear_figura(self, datos):
        raise NotImplementedError
    

    

class VentanaEsfera(VentanaBase):
    def __init__(self):
        super().__init__("Esfera")
        self._texto_especifico = tk.Label(self._ventana, text = "Ingrese los siguientes datos para construir una esfera")
        self._texto_especifico.grid(column = 0, row = 1, pady = 10)

        _radio_label= tk.Label(self._ventana, text = "Ingrese el radio:")
        _radio_label.grid(column = 0, row = 2, pady = 10)

        self._radio_entry = tk.Entry(self._ventana)
        self._radio_entry.grid(column = 1, row = 2)

        self._campos.append(self._radio_entry)

    def obtener_datos(self):
        try:
            radio = float(self._campos[0].get().strip())
            if radio <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa solo números positivos")
            return
        return radio
    
    def crear_figura(self, datos):
        return Esfera(datos)

class VentanaCilindro(VentanaBase):
    def __init__(self):
        super().__init__("Cilindro")
        self._texto_especifico = tk.Label(self._ventana, text = "Ingrese los siguientes datos para construir un cilindro")
        self._texto_especifico.grid(column = 0, row = 1, pady = 10)

        metricas = ["el radio", "la altura"]
        for i in range (2):
            etiqueta = tk.Label(self._ventana, text = f"Ingrese {metricas[i]}:")
            etiqueta.grid(column = 0, row = 2 + i, pady = 10)

            campo = tk.Entry(self._ventana)
            campo.grid(column = 1, row = 2 + i)
 
            self._campos.append(campo)

    def obtener_datos(self):
        try:
            radio = float(self._campos[0].get().strip())
            altura = float(self._campos[1].get().strip())
            if radio <= 0 or  altura <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa solo números positivos")
            return
        return radio, altura
    
    def crear_figura(self, datos):
        return Cilindro(*datos)

class VentanaPiramide(VentanaBase):
    def __init__(self):
        super().__init__("Pirámide")
        self._texto_especifico = tk.Label(self._ventana, text = "Ingrese los siguientes datos para construir una pirámide")
        self._texto_especifico.grid(column = 0, row = 1, pady = 10)

        metricas = ["el lado de la base", "la altura", "el apotema"]

        for i in range (3):
            etiqueta = tk.Label(self._ventana, text = f"Ingrese la medida de {metricas[i]}:")
            etiqueta.grid(column = 0, row = 2 + i, pady = 10)

            campo = tk.Entry(self._ventana)
            campo.grid(column = 1, row = 2 + i)
 
            self._campos.append(campo)

    def obtener_datos(self):
        try:
            lado_base = float(self._campos[0].get().strip())
            altura = float(self._campos[1].get().strip())
            apotema = float(self._campos[2].get().strip())
            if lado_base <= 0 or  altura <= 0 or apotema <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa solo números positivos")
            return 
        return lado_base, altura, apotema
        
    def crear_figura(self, datos):
        return Piramide(*datos)
        

def main():
    app = VentanaPrincipal()
    app.ejecutar()

if __name__ == "__main__":
    main()


