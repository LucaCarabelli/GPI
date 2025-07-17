# app/views/reportes_view.py

import tkinter as tk
from tkinter import ttk
from utils.theme import current_theme

class ReportesView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, bg=current_theme["bg"])
        self.controller = controller
        self.widgets = []
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Reportes Financieros",
            font=("Helvetica", 20, "bold"),
            fg=current_theme["accent"],
            bg=current_theme["bg"]
        )
        title_label.pack(pady=20)
        self.widgets.append(title_label)

        frame = tk.Frame(self, bg=current_theme["bg"])
        frame.pack(pady=20)
        self.widgets.append(frame)

        ttk.Button(frame, text="Ver Ventas del Día", command=self.ver_ventas_dia).pack(pady=5)
        ttk.Button(frame, text="Ver Reporte Mensual", command=self.ver_ventas_mes).pack(pady=5)

    def ver_ventas_dia(self):
        # Aquí se podría cargar un archivo JSON con las ventas del día, por ahora es demostrativo
        print("🔎 Mostrando ventas del día...")

    def ver_ventas_mes(self):
        print("📊 Mostrando ventas del mes...")
