import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from Listas.circular_list import CircularList
from GUI.ventana_registrar_usuario import VentanaRegistroUsuario
from GUI.ventana_edicion import VentanaEdicion

class VentanaUsuario(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lista_usuarios = CircularList()
        self.title("Usuarios")
        self.geometry("300x200")

        tk.Button(self, text="Registrar Nuevos Usuarios", command=self.registar_usuarios
                  ).pack(pady=5)
        tk.Button(self, text="Visualizar Usuarios Existentes", command=self.mostrar_usuarios).pack(side=tk.TOP, pady=5)
        # Botón para regresar a la ventana principal
        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=10)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente
        
    def registar_usuarios(self):
        self.withdraw()
        nueva_ventana = VentanaRegistroUsuario(self, self.lista_usuarios)
        nueva_ventana.grab_set()
    
    def mostrar_usuarios(self):
        ventana_lista = tk.Toplevel(self)
        ventana_lista.title("Lista Usuarios Existentes")
        ancho_pantalla = ventana_lista.winfo_screenwidth()
        alto_pantalla = ventana_lista.winfo_screenheight()
        ventana_lista.geometry(f"{ancho_pantalla}x{alto_pantalla}")


        tree = tk.ttk.Treeview(ventana_lista, columns=("Código", "Nombre", "Correo", "Contrasena", "Puesto", "Estado"), show="headings")
        tree.heading("Código", text="Código")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Correo", text="Correo")
        tree.heading("Contrasena", text="Contraseña")
        tree.heading("Puesto", text="Puesto")
        tree.heading("Estado", text="Estado")

        # Ajustar el ancho de las columnas
        tree.column("Código", width=100)
        tree.column("Nombre", width=150)
        tree.column("Correo", width=200)
        tree.column("Contrasena", width=150)
        tree.column("Puesto", width=200)
        tree.column("Estado", width=150)
        
        datos_str = self.lista_usuarios.show()
        
        # Divide los datos de usuarios en líneas individuales
        lineas_datos = self.lista_usuarios.show().strip().split('\n')

        # Procesa cada línea (usuario) individualmente
        for datos_str in lineas_datos:
            # Divide la cadena de datos del usuario en partes basándonos en el separador '|'
            datos = datos_str.split('|')

            # Verifica que el número de elementos en 'datos' coincida con el número de columnas en el Treeview
            if len(datos) == len(tree["columns"]):
                # Inserta los datos del usuario actual en el Treeview
                tree.insert("", tk.END, values=tuple(datos))
            else:
                print(f"Error: El número de datos ({len(datos)}) no coincide con el número de columnas ({len(tree['columns'])}).")

        btn_editar = tk.Button(ventana_lista, text="Actualizar Datos", command=lambda: self.editar_usuario(tree))
        btn_editar.pack(pady=5)
        btn_eliminar = tk.Button(ventana_lista, text="Deshabilitar", command=lambda: self.eliminar_usuario(tree))
        btn_eliminar.pack(pady=5)

        tree.pack(expand=True, fill=tk.BOTH)
        
    def editar_usuario(self, tree):
        seleccionado = tree.selection()

        if seleccionado:  # Verifica que haya algo seleccionado
            item = tree.item(seleccionado)
            valores = item['values']
        
            etiquetas = ["Código", "Nombre", "Correo", "Contrasena", "Puesto", "Estado"]
            datos_usuario = dict(zip(etiquetas, valores))
        
            # Función que maneja el guardado de los cambios
            def guardar_cambios(datos_actualizados):
                try:
                    # Actualiza el ítem en el Treeview con los nuevos valores
                    nuevos_valores = (datos_actualizados["Código"], datos_actualizados["Nombre"], datos_actualizados["Correo"], datos_actualizados["Contrasena"], datos_actualizados["Puesto"], datos_actualizados["Estado"])
                    tree.item(seleccionado, values=nuevos_valores)
                    print("Datos actualizados:", datos_actualizados)
                    print('Nuevos valores: ', nuevos_valores)
                    # Si todo fue exitoso, devuelve True
                    return True
                except Exception as e:
                    print("Error al guardar los cambios:", e)
                    # Si hubo un error, devuelve False
                    return False
        
            # Instanciar VentanaEdicionUsuario pasando 'self' como 'master'
            VentanaEdicion(self, datos_usuario, guardar_cambios)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un asociado para editar.")

    def eliminar_usuario(self, tree):
        seleccionado = tree.selection()
    
        if seleccionado:  # Verifica que haya algo seleccionado
            # Cada usuario tiene un ID/código único.
            item = tree.item(seleccionado)
            codigo_usuario = item['values'][0]
        
            print('lista: ', self.lista_usuarios.show())
            print('items: ', item)
            self.lista_usuarios.remove_by_id(codigo_usuario)
        
            # Eliminar el ítem seleccionado del Treeview
            tree.delete(seleccionado)
        
            # Opcional: Mostrar un mensaje de confirmación
            messagebox.showinfo("Éxito", "Usuario deshabilitado correctamente")
        else:
            # Mostrar un mensaje si no hay un ítem seleccionado
            messagebox.showwarning("Advertencia", "Por favor, seleccione un usuario para deshabilitar.")


