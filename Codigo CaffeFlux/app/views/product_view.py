# app/views/productos_view.py

import tkinter as tk
from tkinter import ttk, messagebox
from controllers.create_product import CreateProduct
from controllers.edit_product import EditProduct
from controllers.delete_product import DeleteProduct
from utils.theme import current_theme
import json
import os

DATA_PATH = "data/productos.json"

class ProductosView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, bg=current_theme["bg"])
        self.controller = controller
        self.create_widgets()
        self.cargar_productos()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Gestión de Productos",
            font=("Helvetica", 20, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        title_label.pack(pady=20)

        form_frame = tk.Frame(self, bg=current_theme["bg"])
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nombre:", bg=current_theme["bg"], fg=current_theme["fg"]).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.nombre_entry = tk.Entry(form_frame, width=30)
        self.nombre_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Categoría:", bg=current_theme["bg"], fg=current_theme["fg"]).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.categoria_entry = tk.Entry(form_frame, width=30)
        self.categoria_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Precio:", bg=current_theme["bg"], fg=current_theme["fg"]).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.precio_entry = tk.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, pady=5)

        btn_frame = tk.Frame(self, bg=current_theme["bg"])
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Editar", command=self.editar_producto).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=10)

        self.tree = ttk.Treeview(self, columns=("Nombre", "Categoría", "Precio"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(pady=20, fill="both", expand=True)

    def cargar_productos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        if not os.path.exists(DATA_PATH):
            return

        with open(DATA_PATH, "r") as f:
            productos = json.load(f)
            for producto in productos:
                self.tree.insert("", "end", values=(producto["nombre"], producto["categoria"], producto["precio"]))

    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()

        if not nombre or not categoria or not precio:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número")
            return

        CreateProduct.add(nombre, categoria, precio)
        self.cargar_productos()
        self.limpiar_campos()

    def editar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para editar.")
            return

        index = self.tree.index(selected_item)
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()

        if not nombre or not categoria or not precio:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número")
            return

        EditProduct.update(index, nombre, categoria, precio)
        self.cargar_productos()
        self.limpiar_campos()

    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
            return

        index = self.tree.index(selected_item)
        DeleteProduct.remove(index)
        self.cargar_productos()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.categoria_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
