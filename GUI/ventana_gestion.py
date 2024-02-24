import tkinter as tk
from tkinter import Toplevel
from GUI.ventana_registrar_asociados import VentanaRegistroAsociado
from tkinter import messagebox
from Listas.simple_linked_list import SimplyLinkedList


class VentanaGestion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lista_asociados = SimplyLinkedList()
        self.title("Gestión de Asociados")
        self.geometry("300x200")
        tk.Label(self, text="Esta es la ventana de Gestión").pack(pady=5)

        tk.Button(self, text="Registrar Asociados", command=self.registrar_asociados
                  ).pack(pady=5)
        tk.Button(self, text="Agregar Eliminar Referencias", command=self.agregar_eliminar_referencias).pack(pady=5)
        tk.Button(self, text="Actualizar Datos", command=self.actualizar_datos).pack(pady=5)
        tk.Button(self, text="Eliminar Cuentas", command=self.eliminar_cuentas).pack(pady=5)

        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=1)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente

    def registrar_asociados(self):
        self.withdraw()
        nueva_ventana = VentanaRegistroAsociado(self, self.lista_asociados)
        nueva_ventana.grab_set()

    def almacenar_archivos(self):
        print("Almacenar archivos adjuntos")

    def agregar_eliminar_referencias(self):
        print("Agregar y eliminar referencias personales")

    def actualizar_datos(self):
        print("Actualizar datos de sus asociados")

    def eliminar_cuentas(self):
        def eliminar():
            nombre_asociado = entry_nombre.get()
            try:
                self.lista_asociados.remove_by_value(nombre_asociado)
                tk.messagebox.showinfo("Eliminado", f"Asociado '{nombre_asociado}' eliminado correctamente.")
            except ValueError as e:
                tk.messagebox.showerror("Error", f"No se pudo eliminar el asociado '{nombre_asociado}': {e}")

            ventana_eliminar.destroy()

        ventana_eliminar = Toplevel(self)
        ventana_eliminar.title("Eliminar Asociado")
        ventana_eliminar.geometry("300x100")

        tk.Label(ventana_eliminar, text="Ingrese el nombre del asociado a eliminar:").pack(pady=5)

        entry_nombre = tk.Entry(ventana_eliminar)
        entry_nombre.pack(pady=5)

        btn_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar)
        btn_eliminar.pack(pady=5)
