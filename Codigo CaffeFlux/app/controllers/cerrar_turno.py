import json
from models.Turno import Turno

DATA_FILE = "data/turnos.json"

def cerrar_turno(ingresos):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if not data or data[-1]["fin"]:  # No hay turno abierto
        return None

    turno_abierto = Turno(**data[-1])
    turno_abierto.cerrar()
    turno_abierto.ingresos = ingresos
    data[-1] = turno_abierto.to_dict()

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return turno_abierto.fin
