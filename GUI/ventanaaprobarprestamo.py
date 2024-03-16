import tkinter as tk
from tkinter import ttk, MULTIPLE, END


class VentanaAprobarPrestamos(tk.Toplevel):
    def __init__(self, parent, lista_prestamo):
        super().__init__(parent)
        self.parent = parent
        self.lista_prestamo = lista_prestamo
        self.title("PRESTAMOS")
        self.geometry("600x400")

        self.mostrar_prestamos()

    def mostrar_prestamos(self):
        if self.lista_prestamo.is_empty():
            ttk.Label(self, text="No hay préstamos generados.").pack(pady=10)
        else:
            ttk.Label(self, text="Préstamos Generados:").pack(pady=10)
            self.lb_prestamos = tk.Listbox(self, selectmode=MULTIPLE, width=50, height=15)
            self.lb_prestamos.pack(pady=5)

            for prestamo in self.lista_prestamo:
                self.lb_prestamos.insert(END, self.formato_prestamo(prestamo))

            btn_aprobar = ttk.Button(self, text="Aprobar", command=self.aprobar_prestamos)
            btn_aprobar.pack(pady=10)

    def formato_prestamo(self, prestamo):
        return f"Código: {prestamo.codigo}, Estado: {prestamo.estado}, Monto: {prestamo.monto}"

    def aprobar_prestamos(self):
        seleccionados = self.lb_prestamos.curselection()
        if seleccionados:
            for idx in seleccionados:
                prestamo = self.lista_prestamo.get(idx)
                prestamo.aprobar()  # Suponiendo que hay un método para aprobar en el objeto Prestamo
                # Actualizar el estado del préstamo en la lista
                self.lista_prestamo.actualizar_prestamo(prestamo)
            ttk.Label(self, text="Préstamos aprobados correctamente.", foreground="green").pack(pady=5)
            # Actualizar la visualización de la lista de préstamos
            self.actualizar_lista_prestamos()
        else:
            ttk.Label(self, text="Por favor, seleccione al menos un préstamo para aprobar.", foreground="red").pack(
                pady=5)

    def actualizar_lista_prestamos(self):
        # Limpiar la lista actual
        self.lb_prestamos.delete(0, END)
        # Mostrar los préstamos actualizados
        for prestamo in self.lista_prestamo:
            self.lb_prestamos.insert(END, self.formato_prestamo(prestamo))