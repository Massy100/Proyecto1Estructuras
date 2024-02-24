import tkinter as tk
import uuid
from tkinter import Toplevel, filedialog, messagebox
from Objetos.asociados import Asociado


class VentanaRegistroAsociado(tk.Toplevel):
    def __init__(self, parent, lista_asociado):
        super().__init__(parent)
        self.title("Registrar Asociados")
        self.parent = parent
        self.lista_asociados = lista_asociado
        self.geometry("400x400")  # Ajusta el tamaño de la ventana según necesites
        self.entries = {}
        # Campos solicitados
        campos = ["Nombre completo", "Dirección actual",
                  "Teléfono de contacto", "Número de DPI", "NIT", "Archivos adjuntos",
                  "Referencias personales"]

        for campo in campos:
            if campo != "Archivos adjuntos":
                row = tk.Frame(self)
                label = tk.Label(row, width=22, text=campo + ":", anchor='w')
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
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        btn_regresar.pack(side=tk.TOP, pady=1)
        btn_mostrar_asociados = tk.Button(self, text="Mostrar Asociados", command=self.mostrar_lista_asociados)
        btn_mostrar_asociados.pack(side=tk.TOP, pady=5)

    def seleccionar_archivos(self):
        filenames = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                filetypes=(("Todos los archivos", "*.*"),))
        print(filenames)  # Aquí puedes hacer algo con los nombres de los archivos seleccionados

    def guardar_datos(self):
        codigo_aleatorio = str(uuid.uuid4())
        codigo = codigo_aleatorio
        nombre = self.entries["Nombre completo"].get()
        direccion = self.entries["Dirección actual"].get()
        telefono = self.entries["Teléfono de contacto"].get()
        dpi = self.entries["Número de DPI"].get()
        nit = self.entries["NIT"].get()

        asociado = Asociado(codigo, nombre, direccion, telefono, dpi, nit)

        self.lista_asociados.append(asociado)

        todos_los_campos_llenos = True
        for label, entry in self.entries.items():
            if not entry.get().strip():  # .strip() elimina espacios en blanco al principio y al final
                messagebox.showwarning("Campo vacío", f"Por favor, complete el campo '{label}'.")
                todos_los_campos_llenos = False
                break  # Sale del ciclo si encuentra un campo vacío

        if not todos_los_campos_llenos:
            return  # Detiene la función si algún campo está vacío

        # No olvides incluir la lógica para los archivos adjuntos

        messagebox.showinfo("Registro exitoso", "Asociado registrado exitosamente")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()

    def mostrar_lista_asociados(self):
        ventana_lista = tk.Toplevel(self)
        ventana_lista.title("Lista de Asociados")

        texto_lista = tk.Text(ventana_lista)
        texto_lista.pack()

        texto_lista.insert(tk.END, self.lista_asociados.show())
