import tkinter as tk
from tkinter import simpledialog, messagebox

class VentanaEdicion:
    def __init__(self, master, datos_usuario, on_guardar):
        self.master = master
        self.datos_usuario = datos_usuario
        self.on_guardar = on_guardar

        self.ventana = tk.Toplevel(master)
        self.ventana.title("Actualizar Usuario")
        self.ventana.geometry("800x700") 

        # Crear campos de entrada basados en los datos del usuario
        self.campos = {}
        row = 0
        for etiqueta, valor in datos_usuario.items():
            tk.Label(self.ventana, text=etiqueta).grid(row=row, column=0, sticky="w")
            entrada = tk.Entry(self.ventana)
            entrada.insert(0, valor)
            # Bloquear el campo de "Código" para que sea de solo lectura
            if etiqueta == "Código":
                entrada.config(state=tk.DISABLED)
            entrada.grid(row=row, column=1)
            self.campos[etiqueta] = entrada
            row += 1

        # Botón para guardar los cambios
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar).grid(row=row, column=0, columnspan=2, pady=10)

        # Botón para cancelar y cerrar la ventana
        tk.Button(self.ventana, text="Cancelar", command=self.ventana.destroy).grid(row=row+1, column=0, columnspan=2, pady=10)

    def guardar(self):
        datos_actualizados = {etiqueta: entrada.get() for etiqueta, entrada in self.campos.items()}
        try:
            # Intenta guardar los cambios y actúa según el resultado
            resultado = self.on_guardar(datos_actualizados)
            if resultado:
                messagebox.showinfo("Éxito", "Datos del usuario actualizados correctamente")
                self.ventana.destroy()
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar los datos del usuario.")
        except Exception as e:
            # Maneja cualquier excepción que pueda ocurrir en on_guardar
            messagebox.showerror("Error", f"Excepción al actualizar los datos: {e}")
            