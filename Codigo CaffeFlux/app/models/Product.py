import json
import os

DATA_FILE = "data/productos.json"

class Product:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def load_all():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save_all(productos):
        with open(DATA_FILE, "w") as f:
            json.dump(productos, f, indent=4)
