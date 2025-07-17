# app/main.py

import tkinter as tk
from tkinter import ttk
from views.product_view import ProductosView
from views.ayuda_view import AyudaView
from views.configuracion_view import ConfiguracionView
from views.reportes_view import ReportesView
from views.turnos_view import TurnosView
from utils.theme import current_theme

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CafféFlux")
        self.geometry("900x600")
        self.configure(bg=current_theme["bg"])

        self.create_widgets()

    def create_widgets(self):
        # Título estilizado
        self.title_label = tk.Label(
            self,
            text="CafféFlux",
            font=("Helvetica", 32, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        self.title_label.pack(pady=40)

        # Frame para los botones
        self.button_frame = tk.Frame(self, bg=current_theme["bg"])
        self.button_frame.pack()

        self.buttons = [
            ("Gestión de Productos", ProductosView),
            ("Gestión de Turno", TurnosView),
            ("Reportes", ReportesView),
            ("Configuración", lambda root=self: ConfiguracionView(root)),
            ("Ayuda", AyudaView)
        ]

        for text, view in self.buttons:
            btn = ttk.Button(
                self.button_frame,
                text=text,
                command=lambda v=view: v(self),
                width=30
            )
            btn.pack(pady=10)

    def actualizar_tema(self):
        """Llama esto después de cambiar el tema para actualizar colores"""
        self.configure(bg=current_theme["bg"])
        self.title_label.configure(bg=current_theme["bg"], fg=current_theme["accent"])
        self.button_frame.configure(bg=current_theme["bg"])
        
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
