# CLASE DONDE SE ALMACENARAN LOS DATOS DE LOS ASOCIADOS
class Asociado:
    def __init__(self, codigo, nombre, direccion, telefono, dpi, nit):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.dpi = dpi
        self.nit = nit


    def __str__(self):
        return f"CODIGO:{self.codigo}|NOMBRE:{self.nombre}|DIRECCION:{self.direccion}"
