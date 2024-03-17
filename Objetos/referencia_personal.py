class ReferenciaPersonal:
    def __init__(self, nombre, telefono, relacion):
        self.nombre = nombre
        self.telefono = telefono
        self.relacion = relacion
        
    def __str__(self):
        return f"{self.nombre}|{self.telefono}|{self.relacion}"