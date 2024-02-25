class Prestamo:
    def __init__(self, codigo_prestamo, codigo_asociado, monto_solicitado, numero_cuotas, monto_aprobado, ingresos_mensuales, garantia, plan_pagos, historial_pagos, estado='creado'):
        self.codigo_prestamo = codigo_prestamo
        self.codigo_asociado = codigo_asociado
        self.estado = estado
        self.monto_solicitado = monto_solicitado
        self.numero_cuotas = numero_cuotas
        self.monto_aprobado = monto_aprobado
        self.ingresos_mensuales = ingresos_mensuales
        self.garantia = garantia
        self.plan_pagos = plan_pagos
        self.historial_pagos = historial_pagos

    def estado_activo(self):
        self.estado = 'creado'

    def estado_aprobado(self):
        self.estado = 'aprobado'
        
    def estado_encurso(self):
        self.estado = 'en curso'

    def estado_finalizado(self):
        self.estado = 'finalizado'
        
    def __str__(self):
        return (f"Código Préstamo: {self.codigo_prestamo}|Código Asociado: {self.codigo_asociado}|Estado: {self.estado}|Monto Solicitado: {self.monto_solicitado}|Número Cuotas: {self.numero_cuotas}|Monto Aprobado: {self.monto_aprobado}|Ingresos Mensuales: {self.ingresos_mensuales}|Garantía: {self.garantia}|Plan Pagos: {self.plan_pagos}|Historial Pagos: {self.historial_pagos}")
