
class Usuario:
    def __init__(self, codigo_usuario, nombre_completo, correo_electronico, contrasena, puesto, estado='activo'):
        self.codigo_usuario = codigo_usuario
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.puesto = puesto
        self.estado = estado


    def activar_usuario(self):
        self.estado = 'activo'

    def desactivar_usuario(self):
        self.estado = 'inactivo'
        
    def __str__(self):
        return (f"{self.codigo_usuario}|{self.nombre_completo}|{self.correo_electronico}|{self.contrasena}|{self.puesto}|{self.estado}")
