import json
from datetime import datetime

class Turno:
    def __init__(self, inicio=None, fin=None, ingresos=0):
        self.inicio = inicio or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fin = fin
        self.ingresos = ingresos

    def cerrar(self):
        self.fin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "inicio": self.inicio,
            "fin": self.fin,
            "ingresos": self.ingresos
        }
