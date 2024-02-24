import tkinter as tk
from tkinter import Toplevel, filedialog, messagebox

class VentanaSolicitarPrestamo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Solicitar Prestamo")
        self.parent = parent
        self.geometry("400x400")  # Ajusta el tamaño de la ventana según necesites
        
        # Campos solicitados
        campos = ['Código del préstamo', 'Código del asociado', 'Estado del préstamo',
            'Monto solicitado', 'Número de cuotas', 'Monto aprobado', 'Ingresos mensuales del asociado',
            'Garantía que deja el asociado', 'Archivos adjuntos', 'Plan de pagos',
            'Historial de pagos']
        
        self.entries = {}
        
        for campo in campos:
            if campo != "Archivos adjuntos":
                row = tk.Frame(self)
                label = tk.Label(row, width=22, text=campo+":", anchor='w')
                entry = tk.Entry(row)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                label.pack(side=tk.LEFT)
                entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
                self.entries[campo] = entry
            else:
                row = tk.Frame(self)
                btn_archivos = tk.Button(row, text="Seleccionar Archivos", command=self.seleccionar_archivos)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                btn_archivos.pack(side=tk.RIGHT, expand=tk.YES)
                
        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        btn_guardar.pack(side=tk.TOP, pady=5)
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        btn_regresar.pack(side=tk.TOP, pady=5)

    def seleccionar_archivos(self):
        filenames = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                filetypes=(("Todos los archivos", "*.*"), ))
        print(filenames)  # Aquí puedes hacer algo con los nombres de los archivos seleccionados

    def guardar_datos(self):
        # Aquí puedes implementar la lógica para guardar los datos ingresados
            
        todos_los_campos_llenos = True
        for label, entry in self.entries.items():
            if not entry.get().strip():  # .strip() elimina espacios en blanco al principio y al final
                messagebox.showwarning("Campo vacío", f"Por favor, complete el campo '{label}'.")
                todos_los_campos_llenos = False
                break  # Sale del ciclo si encuentra un campo vacío
    
        if not todos_los_campos_llenos:
            return  # Detiene la función si algún campo está vacío
        
        # No olvides incluir la lógica para los archivos adjuntos
        
        messagebox.showinfo("Registro exitoso", "Prestamo solicitado exitosamente")
        
    def regresar(self):
        self.destroy()  
        self.parent.deiconify()