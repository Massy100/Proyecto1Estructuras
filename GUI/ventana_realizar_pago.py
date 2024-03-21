from Objetos.prestamo import Prestamo
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VentanaRealizarPagos(tk.Toplevel):
    def __init__(self, parent, lista_prestamo):
        super().__init__(parent)
        self.title("Realizar Pagos")
        self.geometry("400x300")
        self.lista_prestamo = lista_prestamo
        self.parent = parent

        # Inicializa prestamo_actual como None
        self.prestamo_actual = None

        ttk.Label(self, text="Seleccione el Préstamo:").pack(pady=(10, 0))
        
        self.codigos_prestamo = [prestamo.codigo_prestamo for prestamo in self.lista_prestamo]
        self.combo_prestamos = ttk.Combobox(self, values=self.codigos_prestamo, state="readonly")
        self.combo_prestamos.pack(pady=(0, 10))

        buscar_btn = ttk.Button(self, text="Buscar Préstamo", command=self.buscar_prestamo)
        buscar_btn.pack()

        self.info_label = ttk.Label(self, text="")
        self.info_label.pack(pady=10)

        ttk.Label(self, text="Monto a Pagar:").pack()
        self.monto_entry = ttk.Entry(self)
        self.monto_entry.pack(pady=(0, 10))

        pagar_btn = ttk.Button(self, text="Realizar Pago", command=self.realizar_pago)
        pagar_btn.pack()
        
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=10)

    def buscar_prestamo(self):
        codigo = self.combo_prestamos.get()
        # Asegúrate de que el código obtenido es del tipo correcto (int o str)
        # Esto depende de cómo estén almacenados tus códigos de préstamo
        try:
            codigo = int(codigo)  # Convierte a int si tus códigos de préstamo son enteros
        except ValueError:
            pass  # o maneja de alguna manera si la conversión no es posible
    
        self.prestamo_actual = None
        for prestamo in self.lista_prestamo:
            if prestamo.codigo_prestamo == codigo:
                self.prestamo_actual = prestamo
                break
    
        if self.prestamo_actual:
            self.info_label.config(text=f"Código: {self.prestamo_actual.codigo_prestamo}, Monto Aprobado: {self.prestamo_actual.monto_aprobado}")
        else:
            messagebox.showerror("Error", "Préstamo no encontrado.")
            self.info_label.config(text="")  # Limpia la etiqueta si el préstamo no se encuentra

    def realizar_pago(self):
        if self.prestamo_actual is None:
            messagebox.showerror("Error", "Primero debe buscar un préstamo válido.")
            return
        try:
            monto_a_pagar = float(self.monto_entry.get())
            # Asegúrate de que monto_aprobado es tratado como un número flotante
            monto_aprobado = float(self.prestamo_actual.monto_aprobado)
        
            if monto_a_pagar > monto_aprobado:
                messagebox.showerror("Error", "El monto a pagar no puede ser mayor al monto aprobado.")
                return
            # Asegúrate de actualizar el monto aprobado como un número flotante
            self.prestamo_actual.monto_aprobado = str(monto_aprobado - monto_a_pagar)  # Si necesitas que sea una cadena después
            self.info_label.config(text=f"Código: {self.prestamo_actual.codigo_prestamo}, Monto Restante: {self.prestamo_actual.monto_aprobado}")
            messagebox.showinfo("Pago Realizado", "El pago se ha realizado con éxito.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un monto válido.")
            
    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente
