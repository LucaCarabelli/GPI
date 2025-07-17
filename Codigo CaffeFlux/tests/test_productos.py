import unittest
from controllers.create_product import crear_producto

class TestCrearProducto(unittest.TestCase):
    def test_creacion_producto_valido(self):
        producto = crear_producto("Latte", "Bebidas", 2500)
        self.assertEqual(producto["nombre"], "Latte")
        self.assertEqual(producto["categoria"], "Bebidas")
        self.assertEqual(producto["precio"], 2500)

if __name__ == "__main__":
    unittest.main()
