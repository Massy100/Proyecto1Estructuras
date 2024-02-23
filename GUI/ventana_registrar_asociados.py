import tkinter as tk
from tkinter import filedialog

class VentanaRegistroAsociado(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrar Asociados")
        self.geometry("400x400")  # Ajusta el tamaño de la ventana según necesites
        
        # Campos solicitados
        campos = ["Código del asociado", "Nombre completo", "Dirección actual",
                  "Teléfonos de contacto", "Número de DPI", "NIT", "Archivos adjuntos",
                  "Referencias personales"]
        
        self.entries = {}
        
        for campo in campos:
            if campo != "Archivos adjuntos":
                row = tk.Frame(self)
                label = tk.Label(row, width=22, text=campo+":", anchor='w')
                entry = tk.Entry(row)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                label.pack(side=tk.LEFT)
                entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
                self.entries[campo] = entry
            else:
                row = tk.Frame(self)
                btn_archivos = tk.Button(row, text="Seleccionar Archivos", command=self.seleccionar_archivos)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                btn_archivos.pack(side=tk.RIGHT, expand=tk.YES)
                
        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        btn_guardar.pack(side=tk.TOP, pady=5)

    def seleccionar_archivos(self):
        filenames = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                filetypes=(("Todos los archivos", "*.*"), ))
        print(filenames)  # Aquí puedes hacer algo con los nombres de los archivos seleccionados

    def guardar_datos(self):
        # Aquí puedes implementar la lógica para guardar los datos ingresados
        # Por ejemplo, imprimir los valores de los campos en la consola
        for campo, entry in self.entries.items():
            print(f"{campo}: {entry.get()}")
        # No olvides incluir la lógica para los archivos adjuntos

# Para probar la ventana, puedes crear una instancia de tk.Tk() y luego instanciar VentanaRegistro
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Opcional: Oculta la ventana principal de Tk
    app = VentanaRegistroAsociado(root)
    app.mainloop()
