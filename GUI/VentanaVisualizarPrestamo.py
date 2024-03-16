from tkinter import ttk, Toplevel

class VentanaVisualizarPrestamos(Toplevel):
    def __init__(self, parent, lista_prestamo):
        super().__init__(parent)
        self.parent = parent
        self.lista_prestamo = lista_prestamo
        self.title("Visualizar Préstamos")
        self.geometry("600x400")

        self.mostrar_prestamos()

    def mostrar_prestamos(self):
        if self.lista_prestamo.is_empty():
            ttk.Label(self, text="No hay préstamos generados.").pack(pady=10)
        else:
            ttk.Label(self, text="Préstamos Generados:").pack(pady=10)
            prestamos_str = self.lista_prestamo.transversal()
            ttk.Label(self, text=prestamos_str).pack(pady=5)