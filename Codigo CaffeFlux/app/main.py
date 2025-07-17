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

        self.current_view = None
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = tk.Label(
            self,
            text="CafféFlux",
            font=("Helvetica", 32, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        self.title_label.pack(pady=10)

        # Botonera lateral
        self.sidebar = tk.Frame(self, bg=current_theme["bg"])
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.buttons = {
            "Gestión de Productos": ProductosView,
            "Gestión de Turno": TurnosView,
            "Reportes": ReportesView,
            "Configuración": ConfiguracionView,
            "Ayuda": AyudaView
        }

        for text, view_class in self.buttons.items():
            btn = ttk.Button(
                self.sidebar,
                text=text,
                width=25,
                command=lambda v=view_class: self.cambiar_vista(v)
            )
            btn.pack(pady=5)

        # Área central de contenido
        self.content_frame = tk.Frame(self, bg=current_theme["bg"])
        self.content_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    def cambiar_vista(self, vista_clase):
        # Elimina vista actual
        if self.current_view is not None:
            self.current_view.destroy()

        # Crea nueva vista en el content_frame
        self.current_view = vista_clase(master=self.content_frame, controller=self)
        self.current_view.pack(expand=True, fill="both")

    def actualizar_tema(self):
        self.configure(bg=current_theme["bg"])
        self.title_label.configure(bg=current_theme["bg"], fg=current_theme["accent"])
        self.sidebar.configure(bg=current_theme["bg"])
        self.content_frame.configure(bg=current_theme["bg"])
        if self.current_view:
            self.current_view.configure(bg=current_theme["bg"])

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
