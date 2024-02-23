import tkinter as tk
from tkinter import Toplevel

class VentanaUsuario(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Usuarios")
        self.geometry("300x200")
        tk.Label(self, text="Esta es la ventana de Usuarios").pack(pady=20)

        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=10)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente


