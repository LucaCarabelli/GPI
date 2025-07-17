import json
import os

DATA_PATH = "data/productos.json"

class DeleteProduct:
    @staticmethod
    def remove(index):
        if not os.path.exists(DATA_PATH):
            return

        with open(DATA_PATH, "r+") as f:
            productos = json.load(f)
            if 0 <= index < len(productos):
                productos.pop(index)
                f.seek(0)
                json.dump(productos, f, indent=4)
                f.truncate()
