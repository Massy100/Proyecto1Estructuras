import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from Objetos.usuario import Usuario
from GUI.ventana_usuario import VentanaUsuario

class VentanaIniciarSesion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Iniciar Sesión")

        # Preestablecer un super usuario
        self.super_usuario = Usuario(0, "Super Usuario", "user@gmail.com", "12345", "Administrador", True)

        # Crear widgets
        tk.Label(self, text="Correo Electrónico:").grid(row=0)
        tk.Label(self, text="Contraseña:").grid(row=1)

        self.correo = tk.Entry(self)
        self.contraseña = tk.Entry(self, show="*")

        self.correo.grid(row=0, column=1)
        self.contraseña.grid(row=1, column=1)

        tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, column=1, sticky=tk.W, pady=4)

        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.grid(row=3, column=1, sticky=tk.W, pady=10)

    def iniciar_sesion(self):
        correo_ingresado = self.correo.get()
        contraseña_ingresada = self.contraseña.get()

        if correo_ingresado == self.super_usuario.correo_electronico and contraseña_ingresada == self.super_usuario.contrasena:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido {self.super_usuario.nombre_completo}")
            self.withdraw() 
            nueva_ventana = VentanaUsuario(self)
            nueva_ventana.grab_set()
        else:
            messagebox.showerror("Error", "Correo electrónico o contraseña incorrecta")
            
    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente
