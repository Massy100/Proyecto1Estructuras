from Objetos.plan_credito import PlanCredito
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

codigo_plan = 0

class VentanaGenerarPlan(tk.Toplevel):
    def __init__(self, parent, lista_prestamo, lista_planes):
        super().__init__(parent)
        self.parent = parent  
        self.title("Generar Plan de Credito")
        self.geometry("1200x900")
        self.lista_prestamo = lista_prestamo
        self.lista_planes = lista_planes

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

        self.entries = {}
        
        # Campos solicitados
        campos = ["Tasa de interés", "Plazo del préstamo",
                  "Cargos y penalizaciones", "Condiciones de Uso",]

        for campo in campos:
            row = tk.Frame(self)
            label = tk.Label(row, width=22, text=campo + ":", anchor='w')
            entry = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            label.pack(side=tk.LEFT)
            entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.entries[campo] = entry

        pagar_btn = ttk.Button(self, text="Generar", command=self.generar_plan)
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

    def generar_plan(self):
        if self.prestamo_actual is None:
            messagebox.showerror("Error", "Primero debe buscar un préstamo válido.")
            return
        try:
            global codigo_plan
            codigo_plan += 1  # Incrementa el ID para asegurar que sea único
            tasa_interes = self.entries["Tasa de interés"].get()
            plazo = self.entries["Plazo del préstamo"].get()
            cargos = self.entries["Cargos y penalizaciones"].get()
            condiciones = self.entries["Condiciones de Uso"].get()

            todos_los_campos_llenos = True
            for label, entry in self.entries.items():
                if not entry.get().strip():  # .strip() elimina espacios en blanco al principio y al final
                    messagebox.showwarning("Campo vacío", f"Por favor, complete el campo '{label}'.")
                    todos_los_campos_llenos = False
                    break  # Sale del ciclo si encuentra un campo vacío

            if not todos_los_campos_llenos:
                return  # Detiene la función si algún campo está vacío

            plan = PlanCredito(codigo_plan, tasa_interes, plazo, cargos, condiciones)

            self.lista_planes.append(plan)

            messagebox.showinfo("Registro exitoso", "Plan de prestamo generado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
    
    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente
