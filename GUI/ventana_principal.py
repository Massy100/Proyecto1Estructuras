import tkinter as tk
from tkinter import ttk

from GUI.ventana_gestion import VentanaGestion
from GUI.ventana_prestamo import VentanaPrestamo
from GUI.ventana_iniciar_sesion import VentanaIniciarSesion


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("500x300")
        self.minsize(480, 300)
        self.configure(bg="white")

        style = ttk.Style()
        style.configure("TButton", foreground="Black", background="Green", font=("Comic Sans MS", 12), padding=10)
        style.map("TButton", background=[("active", "Green")])

        contenedor = tk.Frame(self, bg="White")
        contenedor.pack(padx=20, pady=20)

        ttk.Button(contenedor, text="Gestión de Asociados", command=self.abrir_gestion, style="TButton").grid(row=0, column=0, pady=5, sticky="ew")
        ttk.Button(contenedor, text="Préstamos Bancarios", command=self.abrir_prestamo, style="TButton").grid(row=1, column=0, pady=5, sticky="ew")
        ttk.Button(contenedor, text="Iniciar Sesión", command=self.abrir_usuario, style="TButton").grid(row=2, column=0, pady=5, sticky="ew")

    def abrir_gestion(self):
        self.withdraw()
        nueva_ventana = VentanaGestion(self)
        nueva_ventana.grab_set()

    def abrir_prestamo(self):
        self.withdraw()
        nueva_ventana = VentanaPrestamo(self)
        nueva_ventana.grab_set()

    def abrir_usuario(self):
        self.withdraw()
        nueva_ventana = VentanaIniciarSesion(self)
        nueva_ventana.grab_set()


def main():
    app = VentanaPrincipal()
    app.mainloop()
