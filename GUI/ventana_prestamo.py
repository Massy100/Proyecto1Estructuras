import tkinter as tk
from tkinter import Toplevel
from GUI.ventana_solicitar_prestamo import VentanaSolicitarPrestamo
from Listas.Double_Linked_List import DoublyLinkedList

class VentanaPrestamo(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lista_prestamo = DoublyLinkedList()
        self.title("Prestamo Bancario")
        self.geometry("800x700")
        tk.Label(self, text="Esta es la ventana de Prestamo Bancario").pack(pady=20)
        
        tk.Button(self, text="Solicitar Prestamo Bancario", command=self.solicitar_prestamo).pack(pady=5)
        tk.Button(self, text="Generar Planes de Credito", command=self.generar_plan).pack(pady=5)
        tk.Button(self, text="Aprobar Prestamos", command=self.aprobar_prestamos).pack(pady=5)
        tk.Button(self, text="Visualizar los Prestamos Generados", command=self.visualizar_prestamos).pack(pady=5)
        tk.Button(self, text="Realizar Pagos", command=self.realizar_pagos).pack(pady=5)

        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
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
        pass
    
    def visualizar_prestamos(self):
        pass
    
    def realizar_pagos(self):
        pass
    
    
