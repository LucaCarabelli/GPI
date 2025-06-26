import tkinter as tk
from tkinter import ttk

class ProductosView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Productos")
        self.geometry("800x600")
        self.configure(bg="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Gestión de Productos",
            font=("Helvetica", 20, "bold"),
            fg="#4B3621",
            bg="#ffffff"
        )
        title_label.pack(pady=20)

        form_frame = tk.Frame(self, bg="#ffffff")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nombre:", bg="#ffffff").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.nombre_entry = tk.Entry(form_frame, width=30)
        self.nombre_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Categoría:", bg="#ffffff").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.categoria_entry = tk.Entry(form_frame, width=30)
        self.categoria_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Precio:", bg="#ffffff").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.precio_entry = tk.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, pady=5)

        btn_frame = tk.Frame(self, bg="#ffffff")
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Editar", command=self.editar_producto).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=10)

        self.tree = ttk.Treeview(self, columns=("Nombre", "Categoría", "Precio"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(pady=20, fill="both", expand=True)

    def agregar_producto(self):
        print("Producto agregado")

    def editar_producto(self):
        print("Producto editado")

    def eliminar_producto(self):
        print("Producto eliminado")
