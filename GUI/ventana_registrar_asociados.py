import tkinter as tk
import uuid
from tkinter import Toplevel, filedialog, messagebox
from Objetos.asociados import Asociado
import os
import shutil
from GUI.ventana_agregar_referencia import VentanaAgregarReferencia
from Objetos.referencia_personal import ReferenciaPersonal

codigo = 1

class VentanaRegistroAsociado(tk.Toplevel):
    def __init__(self, parent, lista_asociados):
        super().__init__(parent)
        self.title("Registrar Asociados")
        self.parent = parent
        self.lista_asociados = lista_asociados
        self.geometry("400x400")  # Ajusta el tamaño de la ventana según necesites
        self.entries = {}
        
        # Campos solicitados
        campos = ["Nombre completo", "Dirección actual",
                  "Teléfono de contacto", "Número de DPI", "NIT",
                  "Referencias personales", "Archivos adjuntos",]

        for campo in campos:
            if campo == "Referencias personales":
                btn_agregar_referencia = tk.Button(self, text="Agregar Referencia", command=self.abrir_ventana_referencias)
                btn_agregar_referencia.pack(side=tk.TOP, pady=5)
            elif campo != "Archivos adjuntos":
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

    def seleccionar_archivos(self):
        # Definir la ruta de la carpeta donde se guardarán los archivos
        ruta_carpeta = os.path.join(os.getcwd(), "Archivos Asociado")
    
        # Verificar si la carpeta existe. Si no, crearla.
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
    
        # Pedir al usuario que seleccione archivos
        filenames = filedialog.askopenfilenames(title="Seleccionar archivos",
                                            filetypes=(("Todos los archivos", "*.*"),))
    
        # Copiar cada archivo seleccionado a la carpeta "archivos"
        for archivo in filenames:
            # Obtener la extensión del archivo para conservarla
            extension = os.path.splitext(archivo)[1]
        
            # Construir el nombre del archivo basado en el ID del cliente y la extensión original del archivo
            nombre_archivo = f"{codigo}{extension}"
            ruta_destino = os.path.join(ruta_carpeta, nombre_archivo)
        
            # Copiar el archivo a la carpeta "archivos" con el nuevo nombre
            shutil.copy(archivo, ruta_destino)
    
        print(f"Archivos guardados en: {ruta_carpeta}")

    
    def guardar_datos(self):
        global codigo
        # Recolecta los datos de los Entry widgets
        nombre = self.entries["Nombre completo"].get()
        direccion = self.entries["Dirección actual"].get()
        telefono = self.entries["Teléfono de contacto"].get()
        dpi = self.entries["Número de DPI"].get()
        nit = self.entries["NIT"].get()

        # Crea una nueva instancia de Asociado
        nuevo_asociado = Asociado(codigo, nombre, direccion, telefono, dpi, nit)
        self.lista_asociados.append(nuevo_asociado)  # Añade el asociado a la lista
    
        # Incrementa el código para el próximo asociado
        codigo += 1
    
        tk.messagebox.showinfo("Éxito", "Asociado registrado exitosamente.")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()
        
    def abrir_ventana_referencias(self):
        # Asume que tienes una clase VentanaAgregarReferencia diseñada para agregar referencias
        # Aquí, podrías pasar cualquier dato necesario, como el código del asociado actual
        global codigo
        ventana_referencias = VentanaAgregarReferencia(self, codigo, self.lista_asociados)
        ventana_referencias.grab_set()  # Hace la ventana modal

    
