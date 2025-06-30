import json
import os
from models.Turno import Turno

DATA_FILE = "data/turnos.json"

def abrir_turno():
    turno = Turno()
    
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    data.append(turno.to_dict())

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return turno.inicio
