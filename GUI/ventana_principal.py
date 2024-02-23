import tkinter as tk
from GUI.ventana_gestion import VentanaGestion
from GUI.ventana_prestamo import VentanaPrestamo
from GUI.ventana_usuario import VentanaUsuario


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("300x150")

        tk.Button(self, text="Gestión de Asociados", command=self.abrir_gestion).pack(pady=5)
        tk.Button(self, text="Préstamos Bancarios", command=self.abrir_prestamo).pack(pady=5)
        tk.Button(self, text="Usuario", command=self.abrir_usuario).pack(pady=5)

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
        nueva_ventana = VentanaUsuario(self)
        nueva_ventana.grab_set()  

def main():
    app = VentanaPrincipal()
    app.mainloop()


   