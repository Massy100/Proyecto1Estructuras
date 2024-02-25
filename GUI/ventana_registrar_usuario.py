import tkinter as tk
from tkinter import ttk
import uuid
from tkinter import Toplevel, filedialog, messagebox
from Objetos.usuario import Usuario
import os
import shutil

codigo_usuario = 0

class VentanaRegistroUsuario(tk.Toplevel):
    def __init__(self, parent, lista_usuarios):
        super().__init__(parent)
        self.title("Registrar Asociados")
        self.parent = parent
        self.lista_usuarios = lista_usuarios
        self.geometry("400x400")  # Ajusta el tamaño de la ventana según necesites
        self.entries = {}
        # Campos solicitados
        campos = ["Nombre completo", "Correo Electronico",
                  "Contraseña", "Puesto", "Estado"]

        for campo in campos:
            row = tk.Frame(self)
            label = tk.Label(row, width=22, text=campo + ":", anchor='w')

            if campo == "Correo Electrónico":
                entry = tk.Entry(row)
                entry.insert(0, "@gmail.com")  # Agregar @gmail.com por defecto
            elif campo == "Contraseña":
                entry = tk.Entry(row, show="*")  # Mostrar la contraseña en caracteres especiales
            elif campo == "Puesto":
                entry = ttk.Combobox(row, values=["Administrador", "Empleado", "Vendedor"])
            elif campo == "Estado":
                entry = tk.Entry(row)
                entry.insert(0, "activo")  # Estado activo por defecto
                entry.config(state="disabled")  # Bloquear el campo de estado
            else:
                entry = tk.Entry(row)

            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            label.pack(side=tk.LEFT)
            if campo == "Puesto":
                entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=5)
            else:
                entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.entries[campo] = entry

        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        btn_guardar.pack(side=tk.TOP, pady=5)
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        btn_regresar.pack(side=tk.TOP, pady=1)

    def guardar_datos(self):
        global codigo_usuario
        codigo_usuario += 1  # Incrementa el ID para asegurar que sea único
        nombre = self.entries["Nombre completo"].get()
        correo = self.entries["Correo Electronico"].get()
        contrasena = self.entries["Contraseña"].get()
        puesto = self.entries["Puesto"].get()
        estado = self.entries["Estado"].get()

        todos_los_campos_llenos = True
        for label, entry in self.entries.items():
            if not entry.get().strip():  # .strip() elimina espacios en blanco al principio y al final
                messagebox.showwarning("Campo vacío", f"Por favor, complete el campo '{label}'.")
                todos_los_campos_llenos = False
                break  # Sale del ciclo si encuentra un campo vacío

        if not todos_los_campos_llenos:
            return  # Detiene la función si algún campo está vacío

        # No olvides incluir la lógica para los archivos adjuntos
        usuario = Usuario(codigo_usuario, nombre, correo, contrasena, puesto, estado)

        self.lista_usuarios.append(usuario)
        
        messagebox.showinfo("Registro exitoso", "Usuario registrado exitosamente")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()