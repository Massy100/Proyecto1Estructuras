import tkinter as tk
from tkinter import ttk, messagebox
from Objetos.referencia_personal import ReferenciaPersonal

class VentanaAgregarReferencia(tk.Toplevel):
    def __init__(self, parent, codigo, lista_asociados):
        super().__init__(parent)
        self.codigo = codigo
        self.lista_asociados = lista_asociados
        self.title("Agregar Referencia")
        self.geometry("400x300")

        tk.Label(self, text="Nombre:").pack(pady=(10, 0))
        self.nombre = tk.Entry(self)
        self.nombre.pack()

        tk.Label(self, text="Teléfono:").pack(pady=(10, 0))
        self.telefono = tk.Entry(self)
        self.telefono.pack()

        tk.Label(self, text="Relación:").pack(pady=(10, 0))
        self.relacion = tk.Entry(self)
        self.relacion.pack()

        btn_agregar = tk.Button(self, text="Agregar", command=self.agregar)
        btn_agregar.pack(pady=(10, 0))
        
    def agregar(self):
        # Recolecta los datos de los widgets de entrada
        nombre = self.nombre.get()
        telefono = self.telefono.get()
        relacion = self.relacion.get()

        # Crea una nueva instancia de ReferenciaPersonal
        referencia_nueva = ReferenciaPersonal(nombre, telefono, relacion)
        
        # Encuentra el asociado específico usando el código
        try:
            asociado_especifico = self.lista_asociados.find_by_codigo(self.codigo)
            asociado_especifico.referencias.append(referencia_nueva)
            messagebox.showinfo("Éxito", "Referencia agregada correctamente.")
            self.destroy()  # Opcionalmente, cierra la ventana después de agregar la referencia
        except Exception as e:
            messagebox.showerror("Error", str(e))
