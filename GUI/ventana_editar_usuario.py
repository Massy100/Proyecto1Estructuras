import tkinter as tk
from tkinter import simpledialog, messagebox

class VentanaEdicionUsuario:
    def __init__(self, master, datos_usuario, on_guardar):
        self.master = master
        self.datos_usuario = datos_usuario
        self.on_guardar = on_guardar

        self.ventana = tk.Toplevel(master)
        self.ventana.title("Editar Asociado")
        self.ventana.geometry("800x700") 

        # Crear campos de entrada basados en los datos del usuario
        self.campos = {}
        row = 0
        valor = datos_usuario.get("Referencias", "")
        for etiqueta, valor in datos_usuario.items():
            if etiqueta != "Referencias":
                tk.Label(self.ventana, text=etiqueta).grid(row=row, column=0, sticky="w")
                entrada = tk.Entry(self.ventana)
                entrada.insert(0, valor)
                entrada.grid(row=row, column=1)
                self.campos[etiqueta] = entrada
                
                # Bloquear el campo de "Código" para que sea de solo lectura
                if etiqueta == "Código":
                    entrada.config(state=tk.DISABLED)
                
                row += 1
            else:
                # Crear un Listbox para las referencias
                tk.Label(self.ventana, text=etiqueta).grid(row=row, column=0, sticky="w")
                self.lista_referencias = tk.Listbox(self.ventana)
                self.lista_referencias.grid(row=row, column=1, sticky="ew")
                
                # Añadir la referencia al Listbox
                self.lista_referencias.insert(tk.END, valor)
                
                # Inicializa una lista vacía para recolectar las referencias
                referencias = []

                # Obtiene el número total de elementos en el Listbox
                num_referencias = self.lista_referencias.size()

                # Itera sobre los elementos del Listbox y los añade a la lista
                for i in range(num_referencias):
                    referencia = self.lista_referencias.get(i)
                    referencias.append(referencia)

                # Concatena los elementos de la lista en una sola cadena, separados por el separador que elijas
                cadena_referencias = '; '.join(referencias)
                print('lista referencias: ', cadena_referencias)
                
                # Botones para agregar y eliminar referencias
                tk.Button(self.ventana, text="Agregar Referencia", command=self.agregar_referencia).grid(row=row+1, column=1, sticky="ew")
                tk.Button(self.ventana, text="Eliminar Referencia", command=self.eliminar_referencia).grid(row=row+2, column=1, sticky="ew")
                row += 3

        # Botón para guardar los cambios
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar).grid(row=row, column=0, columnspan=2, pady=10)

        # Botón para cancelar y cerrar la ventana
        tk.Button(self.ventana, text="Cancelar", command=self.ventana.destroy).grid(row=row+1, column=0, columnspan=2, pady=10)

    def guardar(self):
        datos_actualizados = {etiqueta: entrada.get() for etiqueta, entrada in self.campos.items()}
        try:
            # Intenta guardar los cambios y actúa según el resultado
            resultado = self.on_guardar(datos_actualizados)
            if resultado:
                messagebox.showinfo("Éxito", "Datos del usuario actualizados correctamente")
                self.ventana.destroy()
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar los datos del usuario.")
        except Exception as e:
            # Maneja cualquier excepción que pueda ocurrir en on_guardar
            messagebox.showerror("Error", f"Excepción al actualizar los datos: {e}")
            
    def agregar_referencia(self):
        # Solicitar al usuario que ingrese una nueva referencia
        nueva_referencia = simpledialog.askstring("Nueva Referencia", "Ingrese la nueva referencia:")
        if nueva_referencia:
            self.lista_referencias.insert(tk.END, nueva_referencia)
            print('nueva referencia: ', nueva_referencia)
            print('como va la lista: ', self.lista_referencias)

    def eliminar_referencia(self):
        # Eliminar la referencia seleccionada
        try:
            indice_seleccionado = self.lista_referencias.curselection()
            self.lista_referencias.delete(indice_seleccionado)
        except:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una referencia para eliminar.")
