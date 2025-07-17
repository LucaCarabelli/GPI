import json
import os

DATA_PATH = "data/productos.json"

class CreateProduct:
    @staticmethod
    def add(nombre, categoria, precio):
        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }

        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, "w") as f:
                json.dump([], f)

        with open(DATA_PATH, "r+") as f:
            productos = json.load(f)
            productos.append(producto)
            f.seek(0)
            json.dump(productos, f, indent=4)
