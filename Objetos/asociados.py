# CLASE DONDE SE ALMACENARAN LOS DATOS DE LOS ASOCIADOS
class Asociado:
    def __init__(self, codigo, nombre, direccion, telefono, dpi, nit, referencias):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.dpi = dpi
        self.nit = nit
        self.referencias = referencias


    def __str__(self):
        return f"{self.codigo}|{self.nombre}|{self.direccion}|{self.telefono}|{self.dpi}|{self.nit}|{self.referencias}"

