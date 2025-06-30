import json
import os

DATA_PATH = "data/productos.json"

class EditProduct:
    @staticmethod
    def update(index, nombre, categoria, precio):
        if not os.path.exists(DATA_PATH):
            return

        with open(DATA_PATH, "r+") as f:
            productos = json.load(f)
            if 0 <= index < len(productos):
                productos[index] = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": precio
                }
                f.seek(0)
                json.dump(productos, f, indent=4)
                f.truncate()
