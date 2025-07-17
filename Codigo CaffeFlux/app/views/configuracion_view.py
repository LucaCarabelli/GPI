# app/views/configuracion_view.py

import tkinter as tk
from tkinter import ttk
from utils.theme import current_theme, toggle_theme

class ConfiguracionView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Configuración")
        self.geometry("800x600")
        self.configure(bg=current_theme["bg"])

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self,
            text="Configuración",
            font=("Helvetica", 20, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        self.title_label.pack(pady=20)

        frame = tk.Frame(self, bg=current_theme["bg"])
        frame.pack(pady=10)

        ttk.Button(frame, text="Alternar modo oscuro", command=self.cambiar_tema).pack(pady=10)

        info_label = tk.Label(
            frame,
            text="(Próximamente: cambio de idioma, moneda, etc.)",
            font=("Helvetica", 10),
            fg=current_theme["fg"],
            bg=current_theme["bg"]
        )
        info_label.pack(pady=10)

        self.widgets = [self, frame, self.title_label, info_label]

    def cambiar_tema(self):
        toggle_theme()
        # Actualiza esta ventana
        for w in self.widgets:
            w.configure(bg=current_theme["bg"])
        self.title_label.configure(fg=current_theme["accent"])

        # Actualiza el MainWindow
        if hasattr(self.master, "actualizar_tema"):
            self.master.actualizar_tema()
