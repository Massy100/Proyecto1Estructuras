import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import shutil
from Objetos.prestamo import Prestamo

codigo_prestamo = 0

class VentanaSolicitarPrestamo(tk.Toplevel):
    def __init__(self, parent, lista_prestamo):
        super().__init__(parent)
        self.title("Solicitar Prestamo")
        self.lista_prestamo = lista_prestamo
        self.parent = parent
        self.geometry("800x800")  # Ajusta el tamaño de la ventana según necesites

        # Campos solicitados
        campos = ['Código del asociado', 'Estado del préstamo',
                  'Monto solicitado', 'Número de cuotas', 'Monto aprobado', 'Ingresos mensuales del asociado',
                  'Garantía que deja el asociado', 'Plan de pagos',
                  'Historial de pagos', 'Archivos adjuntos']

        self.entries = {}

        for campo in campos:
            if campo != 'Código del préstamo':  # Excluir el campo del código del préstamo
                if campo != "Archivos adjuntos":
                    row = tk.Frame(self)
                    label = tk.Label(row, width=22, text=campo + ":", anchor='w')
                    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                    label.pack(side=tk.LEFT)
                    if campo == 'Estado del préstamo':
                        estado_values = ["Creado", "Aprobado", "En curso", "Finalizado"]
                        estado_combobox = ttk.Combobox(row, values=estado_values)
                        estado_combobox.pack(side=tk.RIGHT)
                        self.entries[campo] = estado_combobox
                    elif campo == "Plan de pagos":
                        # Aquí se agrega el ComboBox para el plan de pagos
                        plan_pagos_values = ["Mensual", "Bimensual", "Trimestral"]
                        plan_pagos_combobox = ttk.Combobox(row, values=plan_pagos_values)
                        plan_pagos_combobox.pack(side=tk.RIGHT)
                        self.entries[campo] = plan_pagos_combobox
                    else:
                        entry = tk.Entry(row)
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
        btn_regresar.pack(side=tk.TOP, pady=5)




    def seleccionar_archivos(self):
        # Definir la ruta de la carpeta donde se guardarán los archivos
        ruta_carpeta = os.path.join(os.getcwd(), "Archivos Prestamo")

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
            nombre_archivo = f"{codigo_prestamo}{extension}"
            ruta_destino = os.path.join(ruta_carpeta, nombre_archivo)

            # Copiar el archivo a la carpeta "archivos" con el nuevo nombre
            shutil.copy(archivo, ruta_destino)

        print(f"Archivos guardados en: {ruta_carpeta}")

    def guardar_datos(self):
        global codigo_prestamo
        codigo_prestamo += 1  # Incrementa el ID para asegurar que sea único
        codigo_asociado = 1
        estado = self.entries["Estado del préstamo"].get()
        monto_solicitado = self.entries["Monto solicitado"].get()
        numero_cuotas = self.entries["Número de cuotas"].get()
        monto_aprobado = self.entries["Monto aprobado"].get()
        ingresos_mensuales = self.entries["Ingresos mensuales del asociado"].get()
        garantia = self.entries["Garantía que deja el asociado"].get()
        plan_pagos = self.entries["Plan de pagos"].get()
        historial_pagos = self.entries["Historial de pagos"].get()

        todos_los_campos_llenos = True
        for label, entry in self.entries.items():
            if not entry.get().strip():  # .strip() elimina espacios en blanco al principio y al final
                messagebox.showwarning("Campo vacío", f"Por favor, complete el campo '{label}'.")
                todos_los_campos_llenos = False
                break  # Sale del ciclo si encuentra un campo vacío

        if not todos_los_campos_llenos:
            return  # Detiene la función si algún campo está vacío

        # No olvides incluir la lógica para los archivos adjuntos
        prestamo = Prestamo(codigo_prestamo, codigo_asociado, monto_solicitado, numero_cuotas, monto_aprobado,
                            ingresos_mensuales, garantia, plan_pagos, historial_pagos)

        self.lista_prestamo.append(prestamo)

        messagebox.showinfo("Registro exitoso", "Prestamo creado exitosamente")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()