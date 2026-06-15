import tkinter as tk
from tkinter import messagebox

class MaxMembersExceededError(Exception):
    pass
class ExtensionError(Exception):
    pass
class TeamSizeError(Exception):
    pass


class EquipoMaratonProgramacion:
    def __init__(self, nombre = "", universidad = "", lenguaje = "", tamaño = 0):
        self._nombre = nombre
        self._universidad = universidad
        self._lenguaje = lenguaje
        self._tamaño = tamaño
        self._integrantes = []

    def verificar_completo(self):
        if len(self._integrantes) < self._tamaño:
            return False
        elif len(self._integrantes) == self._tamaño:
            return True
        else:
            raise MaxMembersExceededError("No puede haber más miembros que el tamaño definido")
        
    def añadir_miembros(self, miembro):
        if self.verificar_completo():
            raise MaxMembersExceededError("No puede haber más miebros que el tamaño definido")
        
        self._integrantes.append(miembro)

    def verificar_programadores(self, nombre, apellido):
            if not nombre.replace(" ", "").isalpha():
                raise ValueError("El nombre solo puede contener letras")

            if not apellido.replace(" ", "").isalpha():
                raise ValueError("El apellido solo puede contener letras")
            
            if len(nombre) > 20:
                raise ExtensionError("El nombre no puede llevar más de 20 caracteres")
            if len(apellido) > 20:
                raise ExtensionError("El apellido no puede llevar más de 20 caracteres")
            
class Ventana():
    def __init__(self):
        self._equipo = None
        self._ventana = tk.Tk()
        self._ventana.title("Equipo Maratón de Programación")
        self._ventana.geometry("650x150")
        self._ventana.resizable(False, False)
        

        self._label_cute = tk.Label(self._ventana, text = "Escoga una opcion")
        self._label_cute.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)

        opciones = {"Configurar Equipo": self.configurar, "Ingresar Programador": self.ingresar, "Consultar Informacion": self.consultar, "Limpiar": self.limpiar}
        for i, (opcion, funcion) in enumerate(opciones.items()):
            boton = tk.Button(self._ventana, text = opcion, command = funcion, bg = ["green", "blue", "cyan", "red"][i], fg = ["white", "white", "black", "white"][i])
            boton.grid(row = 1, column = i, padx = 10, pady = 10)
    
    def configurar(self):
        ventana = Configurar()
        self._ventana.wait_window(ventana._ventana)
        self._equipo = ventana._equipo

    def ingresar(self):
        if self._equipo is None:
            messagebox.showerror(
            "Error",
            "No se ha creado un equipo al que ingresarle programadores"
        )
            return

        Ingresar(self._equipo)

    def consultar(self):
        if self._equipo is None:
            messagebox.showerror("Error", "No se ha creado un equipo al que consultarle información")
            return
        
        integrantes = "\n".join(f"{nombre} {apellido}" for nombre, apellido in self._equipo._integrantes)
        messagebox.showinfo(
    "Datos del Equipo:",
    f"Nombre: {self._equipo._nombre}\n"
    f"Universidad: {self._equipo._universidad}\n"
    f"Lenguaje: {self._equipo._lenguaje}\n\n"
    f"Integrantes:\n{integrantes}"
)

    def limpiar(self):
        self._equipo = None

    def ejecutar(self):
        self._ventana.mainloop()

class Configurar():
    def __init__(self):    
        self._equipo = None
        self._ventana = tk.Toplevel()
        self._ventana.title("Configurar Equipo")
        self._ventana.geometry("450x450")
        self._ventana.resizable(False, False)

        self._label_cute = tk.Label(self._ventana, text = "Ingrese los datos del equipo")
        self._label_cute.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
        
        items = ["Nombre", "Universidad", "Lenguaje de Programación", "Tamaño del equipo"]
        self._campos = []
        for i, item in enumerate(items):
            label = tk.Label(self._ventana, text = item + ":")
            label.grid(row = i + 1, column = 0, padx = 10, pady = 10)

            campo = tk.Entry(self._ventana)
            campo.grid(row = i + 1, column = 1, padx = 10, pady = 10, columnspan = 2)

            self._campos.append((label, campo))

        botones = {"Ingresar": self.ingresar, "Limpiar": self.limpiar}
        for i, (texto, funcion) in enumerate(botones.items()):
            boton = tk.Button(self._ventana, text = texto, command = funcion, bg = ["green", "red"][i], fg = "white")
            boton.grid(row = 5, column = i, padx = 10, pady = 10)

    def obtener_datos(self):
        valores = []
        for i in range(4):
            try:
                if i != 3:
                    valor = self._campos[i][1].get().strip().capitalize()
                    if valor == "":
                        raise ValueError("No es posible que el nombre, lenguaje de programación o la universidad sean números o estén vacíos")
                    if valor.isdigit():
                        raise ValueError("El nombre no puede contener solo números")
                else:
                    valor = int(self._campos[i][1].get().strip())
                    if (valor < 2) or (valor > 3):
                        raise TeamSizeError("No es posible que el tamaño del equipo sea menor a 2 integrantes, o mayor que 3")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
            except TeamSizeError as e:
                messagebox.showerror("Error", str(e))
                return
            valores.append(valor)
        return tuple(valores)
            
    def ingresar(self):
        datos = self.obtener_datos()
        if datos is None:
            return
        
        self._equipo = EquipoMaratonProgramacion(datos[0], datos[1], datos [2], datos[3])
        messagebox.showinfo("Aviso", "Se han ingresado correctamente los datos")
        self._ventana.destroy()
        
    def limpiar(self):
        for i, (label, campo) in enumerate(self._campos):
            campo.delete(0, tk.END)
    
class Ingresar():
    def __init__(self, equipo):
        if equipo is None:
            return
        self._equipo = equipo
        self._ventana = tk.Toplevel()
        self._ventana.title("Ingresar Programador")
        self._ventana.geometry("350x250")
        self._ventana.resizable(False, False)

        self._label_cute = tk.Label(self._ventana, text = "Ingrese los datos del programador")
        self._label_cute.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)

        self._campos = []
        cositas = ("Nombre", "Apellido")
        for i, cosa in enumerate(cositas):
            label = tk.Label(self._ventana, text = cosa)
            label.grid(row = i + 1, column = 0, padx = 10, pady = 10)

            entry = tk.Entry(self._ventana)
            entry.grid(row = i + 1, column = 1, padx = 10, pady = 10)
            
            self._campos.append((label, entry))

        botones = {"Ingresar": self.ingresar, "Limpiar": self.limpiar}
        for i, (texto, funcion) in enumerate(botones.items()):
            boton = tk.Button(self._ventana, text = texto, command = funcion, bg = ["green", "red"][i], fg = "white")
            boton.grid(row = 3, column = 2*i, padx = 10, pady = 10)

    def limpiar(self):
        for i, (label, campo) in enumerate(self._campos):
            campo.delete(0, tk.END)

    def obtener_datos(self):
        valores = []

        for i, (label, entry) in enumerate(self._campos):

            valor = entry.get().strip().capitalize()

            valores.append(valor)
        return tuple(valores)
    def ingresar(self):
        datos = self.obtener_datos()
        if datos is None:
            return
        try:
            self._equipo.verificar_programadores(*datos)
            self._equipo.añadir_miembros(datos)
            messagebox.showinfo("Aviso", "Se han ingresado correctamente los datos")
        except TypeError as e:
            messagebox.showerror("Error", str(e))
            return
        except ExtensionError as e:
            messagebox.showerror("Error", str(e))
            return
        except MaxMembersExceededError as e:
            messagebox.showerror("Error", str(e))
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        
def main():    
    app = Ventana()
    app.ejecutar()

if __name__ == "__main__":
    main()

