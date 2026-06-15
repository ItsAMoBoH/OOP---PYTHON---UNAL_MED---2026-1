import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

class Ventana:
    def __init__(self):
        self._ruta = None
        self._ventana = tk.Tk()
        self._ventana.title("Lector de Archivos de Texto")
        self._ventana.geometry("650x150")
        self._ventana.resizable(False, False)
        self._ventana_texto = None
        self._label_bonis = tk.Label(self._ventana, text = "Escoja la ruta del archivo de texto")
        self._label_bonis.grid(row = 0, column = 0, padx = 10, pady = 10)

        opciones = {"Escoger Ruta": self.escoger, "Abrir Archivo": self.abrir, "Limpiar": self.limpiar}
        for i, (texto, funcion) in enumerate(opciones.items()):
            boton = tk.Button(self._ventana, text = texto, command = funcion, bg = ["blue", "green", "red"][i], fg = "white")
            boton.grid(row = 2, column = i, padx = 10, pady = 10)

        self._labels_ruta = []
        for i in range(2):
            label = tk.Label(self._ventana, text = ["Ruta:", ""][i])
            label.grid(row = 1, column = i, padx = 10, pady = 10)
            self._labels_ruta.append(label)
        self._labels_ruta = tuple(self._labels_ruta)

    def abrir_archivo(self, ruta):
        if not ruta:
            messagebox.showerror("Error", "No ha escogido una ruta")
            return
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                mensaje = archivo.read()
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo")
            return
        except PermissionError:
            messagebox.showerror("Error", "No se tienen los permisos suficientes para abrir el archivo")
            return
        except Exception:
            messagebox.showerror("Error", "Se ha presentado un error desconocido")
            return
        return mensaje

    def escoger(self):  
        self._ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        self._labels_ruta[1].config(text = self._ruta)
    
    def abrir(self):
        mensaje = self.abrir_archivo(self._ruta)
        if mensaje is None:
            return
        if self._ventana_texto is not None:
            self.cerrar_ventana_texto()
        self._ventana_texto = tk.Toplevel(self._ventana)
        self._ventana_texto.title("Texto del archivo")
        self._ventana_texto.geometry("400x400")
        self._ventana_texto.focus()
        texto = ScrolledText(self._ventana_texto, width = 70, height = 20)
        texto.pack(fill="both", expand=True)
        texto.insert("end", mensaje)
        texto.config(state="disabled")

        self._ventana_texto.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_texto)


    def cerrar_ventana_texto(self):
        if self._ventana_texto is not None:
            self._ventana_texto.destroy()
            self._ventana_texto = None

    def limpiar(self):
        self._labels_ruta[1].config(text = "")
        if self._ventana_texto is not None:
            self.cerrar_ventana_texto()
        self._ruta = None

    def ejecutar(self):
        self._ventana.mainloop()


def main():
    app = Ventana()
    app.ejecutar()

if __name__ == "__main__":
    main()