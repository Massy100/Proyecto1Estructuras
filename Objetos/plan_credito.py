class PlanCredito:
    def __init__(self, codigo_plan, tasa_interes, plazo_prestamo, cargos_penalizaciones, condiciones):
        self.codigo_plan = codigo_plan
        self.tasa_interes = tasa_interes
        self.plazo_prestamo = plazo_prestamo
        self.cargos_penalizaciones = cargos_penalizaciones
        self.condiciones = condiciones

    def __str__(self):
        return (f"{self.codigo_plan}|{self.tasa_interes}|{self.plazo_prestamo}|{self.cargos_penalizaciones}|{self.condiciones}")