import tkinter as tk
from tkinter import Toplevel
from GUI.ventana_registrar_asociados import VentanaRegistroAsociado

class VentanaGestion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Gestión de Asociados")
        self.geometry("300x200")
        tk.Label(self, text="Esta es la ventana de Gestión").pack(pady=20)

        tk.Button(self, text="Registrar Asociados", command=self.registrar_asociados).pack(pady=5)
        tk.Button(self, text="Almacenar Archivos", command=self.almacenar_archivos).pack(pady=5)
        tk.Button(self, text="Agregar Eliminar Referencias", command=self.agregar_eliminar_referencias).pack(pady=5)
        tk.Button(self, text="Actualizar Datos", command=self.actualizar_datos).pack(pady=5)
        tk.Button(self, text="Eliminar Cuentas", command=self.eliminar_cuentas).pack(pady=5)
        
        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=10)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente
        
    def registrar_asociados(self):
        self.withdraw()
        nueva_ventana = VentanaRegistroAsociado(self)
        nueva_ventana.grab_set() 

    def almacenar_archivos(self):
        print("Almacenar archivos adjuntos")

    def agregar_eliminar_referencias(self):
        print("Agregar y eliminar referencias personales")

    def actualizar_datos(self):
        print("Actualizar datos de sus asociados")

    def eliminar_cuentas(self):
        print("Eliminar cuentas existentes")


