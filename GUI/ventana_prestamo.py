from tkinter import ttk, messagebox
from tkinter import Toplevel
from GUI.ventana_solicitar_prestamo import VentanaSolicitarPrestamo
from Listas.Double_Linked_List import DoublyLinkedList
from GUI.VentanaVisualizarPrestamo import VentanaVisualizarPrestamos
from GUI.ventanaaprobarprestamo import VentanaAprobarPrestamos


class VentanaPrestamo(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lista_prestamo = DoublyLinkedList()
        self.title("Prestamo Bancario")
        self.geometry("800x700")

        style = ttk.Style()
        style.configure("TButton", foreground="Black", background="Green", font=("Comic Sans MS", 12), padding=10)
        style.map("TButton", background=[("active", "Purple")])

        style = ttk.Style()
        style.configure("TLabelCustom.TLabel", foreground="white", background="Green", font=("Comic Sans MS", 12),
                        padding=10)
        ttk.Label(self, text="Esta es la ventana de Prestamo Bancario",style="TLabelCustom.TLabel").pack(pady=20)

        ttk.Button(self, text="Solicitar Prestamo Bancario", command=self.solicitar_prestamo).pack(pady=5)
        ttk.Button(self, text="Generar Planes de Credito", command=self.generar_plan).pack(pady=5)
        ttk.Button(self, text="Aprobar Prestamos", command=self.aprobar_prestamos).pack(pady=5)
        ttk.Button(self, text="Visualizar los Prestamos Generados", command=self.visualizar_prestamos).pack(pady=5)
        ttk.Button(self, text="Realizar Pagos", command=self.realizar_pagos).pack(pady=5)

        # Botón para regresar a la ventana principal
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=10)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente

    def solicitar_prestamo(self):
        self.withdraw()
        nueva_ventana = VentanaSolicitarPrestamo(self, self.lista_prestamo)
        nueva_ventana.grab_set()

    def generar_plan(self):
        pass

    def aprobar_prestamos(self):
        if self.lista_prestamo.is_empty():
            messagebox.showinfo("No hay préstamos", "No hay préstamos para aprobar.")
        else:
            nueva_ventana = VentanaAprobarPrestamos(self,
                                                    self.lista_prestamo.transversal())  # Pasamos la lista transversalizada
            nueva_ventana.grab_set()

    def visualizar_prestamos(self):
        if self.lista_prestamo.is_empty():
            nueva_ventana = VentanaVisualizarPrestamos(self, self.lista_prestamo)
            nueva_ventana.grab_set()

        else:
            nueva_ventana = VentanaVisualizarPrestamos(self, self.lista_prestamo)
            nueva_ventana.grab_set()

    def realizar_pagos(self):
        pass