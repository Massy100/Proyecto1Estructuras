from tkinter import ttk, Toplevel

class VentanaVisualizarPrestamos(Toplevel):
    def __init__(self, parent, lista_prestamo):
        super().__init__(parent)
        self.parent = parent
        self.lista_prestamo = lista_prestamo
        self.title("Visualizar Préstamos")
        self.attributes('-fullscreen', True)
        self.mostrar_prestamos()

    def mostrar_prestamos(self):
        if self.lista_prestamo.is_empty():
            ttk.Label(self, text="No hay préstamos generados.").pack(pady=10)
        else:
            ttk.Label(self, text="Préstamos Generados:").pack(pady=10)
            for i, prestamo in enumerate(self.lista_prestamo, start=1):
                row_frame = ttk.Frame(self)
                row_frame.pack(pady=2, fill='x')

                # Modificación para mostrar todos los atributos del préstamo
                prestamo_info = (
                    f"Código Préstamo: {prestamo.codigo_prestamo}, "
                    f"Código Asociado: {prestamo.codigo_asociado}, "
                    f"Estado: {prestamo.estado}, "
                    f"Monto Solicitado: {prestamo.monto_solicitado}, "
                    f"Número Cuotas: {prestamo.numero_cuotas}, "
                    f"Monto Aprobado: {prestamo.monto_aprobado}, "
                    f"Ingresos Mensuales: {prestamo.ingresos_mensuales}, "
                    f"Garantía: {prestamo.garantia}, "
                    f"Plan de Pagos: {prestamo.plan_pagos}, "
                    f"Historial de Pagos: {prestamo.historial_pagos}"
                )
                ttk.Label(row_frame, text=prestamo_info).pack(side='left', padx=10)
                approve_button = ttk.Button(row_frame, text="Aprobar")
                approve_button.config(command=lambda b=approve_button, p=prestamo: self.aprobar_prestamo(p, b))
                approve_button.pack(side='right')
                
        regresar_btn = ttk.Button(self, text="Regresar", command=self.regresar_principal)
        regresar_btn.pack()
    
    def aprobar_prestamo(self, prestamo, button):
        prestamo.estado = "aprobado"
        button.config(state='disabled')  # Deshabilita el botón después de cambiar el estado del préstamo
        # Actualiza la interfaz de usuario para reflejar el cambio de estado
        self.actualizar_interfaz() 

    def actualizar_interfaz(self):
        # Limpiar la interfaz actual y volver a mostrar los préstamos
        for widget in self.winfo_children():
            widget.destroy()
        self.mostrar_prestamos()
        
    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente