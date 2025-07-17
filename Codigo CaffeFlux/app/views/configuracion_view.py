# app/views/configuracion_view.py

import tkinter as tk
from tkinter import ttk
from utils.theme import current_theme, toggle_theme

class ConfiguracionView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, bg=current_theme["bg"])
        self.controller = controller  # Para comunicación con MainWindow
        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Configuración",
            font=("Helvetica", 20, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        title_label.pack(pady=20)
        self.widgets.append(title_label)

        frame = tk.Frame(self, bg=current_theme["bg"])
        frame.pack(pady=10)
        self.widgets.append(frame)

        ttk.Button(frame, text="Alternar modo oscuro", command=self.cambiar_tema).pack(pady=10)

        info_label = tk.Label(
            frame,
            text="(Próximamente: cambio de idioma, moneda, etc.)",
            font=("Helvetica", 10),
            fg=current_theme["fg"],
            bg=current_theme["bg"]
        )
        info_label.pack(pady=10)
        self.widgets.append(info_label)

    def cambiar_tema(self):
        toggle_theme()
        # Actualizar todos los widgets con el nuevo tema
        for widget in self.widgets:
            widget.configure(bg=current_theme["bg"])
            if isinstance(widget, tk.Label):
                widget.configure(fg=current_theme["accent"] if "Configuración" in widget.cget("text") else current_theme["fg"])

        # Notificar al controlador (MainWindow) para que actualice su color también
        if self.controller and hasattr(self.controller, "actualizar_tema"):
            self.controller.actualizar_tema()
