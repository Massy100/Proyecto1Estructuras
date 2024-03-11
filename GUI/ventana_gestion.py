import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_registrar_asociados import VentanaRegistroAsociado
from tkinter import messagebox
from Listas.simple_linked_list import SimplyLinkedList
from GUI.ventana_editar_usuario import VentanaEdicionUsuario


class VentanaGestion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.lista_asociados = SimplyLinkedList()
        self.title("Gestión de Asociados")
        self.geometry("500x400")

        style = ttk.Style()
        style.configure("TButton", foreground="Black", background="green", font=("Comic Sans MS", 12), padding=10)
        style.map("TButton", background=[("active", "Green")])

        style = ttk.Style()
        style.configure("TLabelCustom.TLabel", foreground="white", background="Green", font=("Comic Sans MS", 12),
                        padding=10)
        ttk.Label(self, text="Ventana de Gestión", style="TLabelCustom.TLabel").pack(pady=5)
        ttk.Button(self, text="Registrar Asociados", command=self.registrar_asociados
                   ).pack(pady=5)
        ttk.Button(self, text="Mostrar Asociados", command=self.mostrar_lista_asociados).pack(side=tk.TOP, pady=5)
        ttk.Button(self, text="Eliminar Cuenta por Nombre", command=self.eliminar_cuentas).pack(pady=5)

        # Botón para regresar a la ventana principal
        btn_regresar = ttk.Button(self, text="Regresar", command=self.regresar_principal)
        btn_regresar.pack(pady=1)

    def regresar_principal(self):
        self.destroy()  # Cierra la ventana de gestión
        self.parent.deiconify()  # Muestra la ventana principal nuevamente

    def registrar_asociados(self):
        self.withdraw()
        nueva_ventana = VentanaRegistroAsociado(self, self.lista_asociados)
        nueva_ventana.grab_set()

    def eliminar_cuentas(self):
        def eliminar():
            nombre_asociado = entry_nombre.get()
            try:
                self.lista_asociados.remove_by_value(nombre_asociado)
                tk.messagebox.showinfo("Eliminado", f"Asociado '{nombre_asociado}' eliminado correctamente.")
            except ValueError as e:
                tk.messagebox.showerror("Error", f"No se pudo eliminar el asociado '{nombre_asociado}': {e}")

            ventana_eliminar.destroy()

        ventana_eliminar = Toplevel(self)
        ventana_eliminar.title("Eliminar Asociado")
        ventana_eliminar.geometry("300x100")

        tk.Label(ventana_eliminar, text="Ingrese el nombre del asociado a eliminar:").pack(pady=5)

        entry_nombre = tk.Entry(ventana_eliminar)
        entry_nombre.pack(pady=5)

        btn_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar)
        btn_eliminar.pack(pady=5)

    def mostrar_lista_asociados(self):
        ventana_lista = tk.Toplevel(self)
        ventana_lista.title("Lista de Asociados")
        ancho_pantalla = ventana_lista.winfo_screenwidth()
        alto_pantalla = ventana_lista.winfo_screenheight()
        ventana_lista.geometry(f"{ancho_pantalla}x{alto_pantalla}")

        tree = tk.ttk.Treeview(ventana_lista,
                               columns=("Código", "Nombre", "Dirección", "Teléfono", "DPI", "NIT", "Referencias"),
                               show="headings")
        tree.heading("Código", text="Código")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Dirección", text="Dirección")
        tree.heading("Teléfono", text="Teléfono")
        tree.heading("DPI", text="DPI")
        tree.heading("NIT", text="NIT")
        tree.heading("Referencias", text="Referencias Personales")

        # Ajustar el ancho de las columnas
        tree.column("Código", width=100)
        tree.column("Nombre", width=150)
        tree.column("Dirección", width=200)
        tree.column("Teléfono", width=150)
        tree.column("DPI", width=200)
        tree.column("NIT", width=150)
        tree.column("Referencias", width=150)

        datos_str = self.lista_asociados.show()

        # Divide los datos de usuarios en líneas individuales
        lineas_datos = self.lista_asociados.show().strip().split('\n')

        # Procesa cada línea (usuario) individualmente
        for datos_str in lineas_datos:
            # Divide la cadena de datos del usuario en partes basándonos en el separador '|'
            datos = datos_str.split('|')

            # Verifica que el número de elementos en 'datos' coincida con el número de columnas en el Treeview
            if len(datos) == len(tree["columns"]):
                # Inserta los datos del usuario actual en el Treeview
                tree.insert("", tk.END, values=tuple(datos))
            else:
                print(
                    f"Error: El número de datos ({len(datos)}) no coincide con el número de columnas ({len(tree['columns'])}).")

        btn_editar = tk.Button(ventana_lista, text="Editar", command=lambda: self.editar_asociado(tree))
        btn_editar.pack(pady=5)
        btn_eliminar = tk.Button(ventana_lista, text="Eliminar", command=lambda: self.eliminar_usuario(tree))
        btn_eliminar.pack(pady=5)

        tree.pack(expand=True, fill=tk.BOTH)

    def editar_asociado(self, tree):
        seleccionado = tree.selection()

        if seleccionado:  # Verifica que haya algo seleccionado
            item = tree.item(seleccionado)
            valores = item['values']

            etiquetas = ["Código", "Nombre", "Dirección", "Teléfono", "DPI", "NIT", "Referencias"]
            datos_usuario = dict(zip(etiquetas, valores))

            # Función que maneja el guardado de los cambios
            def guardar_cambios(datos_actualizados):
                try:
                    # Actualiza el ítem en el Treeview con los nuevos valores
                    # Unir las referencias en una cadena si 'Referencias' está presente y es una lista; de lo contrario, usar cadena vacía
                    print(datos_actualizados.get("Referencias"))
                    # Esto manejará de manera segura el caso en que "Referencias" sea None
                    referencias_str = ", ".join(datos_actualizados.get("Referencias") or [])
                    nuevos_valores = (
                    datos_actualizados["Código"], datos_actualizados["Nombre"], datos_actualizados["Dirección"],
                    datos_actualizados["Teléfono"], datos_actualizados["DPI"], datos_actualizados["NIT"],
                    referencias_str)
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
            VentanaEdicionUsuario(self, datos_usuario, guardar_cambios)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un asociado para editar.")

    def eliminar_usuario(self, tree):
        seleccionado = tree.selection()

        if seleccionado:  # Verifica que haya algo seleccionado
            # Cada usuario tiene un ID/código único.
            item = tree.item(seleccionado)
            codigo_usuario = item['values'][0]

            print('lista: ', self.lista_asociados.show())
            print('items: ', item)
            self.lista_asociados.remove_by_id(codigo_usuario)

            # Eliminar el ítem seleccionado del Treeview
            tree.delete(seleccionado)

            # Opcional: Mostrar un mensaje de confirmación
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
        else:
            # Mostrar un mensaje si no hay un ítem seleccionado
            messagebox.showwarning("Advertencia", "Por favor, seleccione un usuario para eliminar.")
