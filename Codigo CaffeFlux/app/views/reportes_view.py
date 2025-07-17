import tkinter as tk
from tkinter import ttk, messagebox
from utils.theme import current_theme
import json
import os
from datetime import datetime

TURNOS_PATH = "data/turnos.json"

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

    def cargar_turnos(self):
        if not os.path.exists(TURNOS_PATH):
            return []

        with open(TURNOS_PATH, "r") as f:
            return json.load(f)

    def ver_ventas_dia(self):
        hoy = datetime.now().strftime("%Y-%m-%d")
        turnos = self.cargar_turnos()

        turnos_hoy = [t for t in turnos if t["inicio"].startswith(hoy)]
        total = sum(t["ingresos"] for t in turnos_hoy)

        if turnos_hoy:
            mensaje = f"🗓️ Ventas del día ({hoy}):\n"
            for t in turnos_hoy:
                mensaje += f" - {t['inicio']} a {t['fin']}: ${t['ingresos']}\n"
            mensaje += f"\n💰 Total: ${total}"
        else:
            mensaje = "No hay turnos registrados hoy."

        messagebox.showinfo("Ventas del Día", mensaje)

    def ver_ventas_mes(self):
        ahora = datetime.now()
        mes_actual = ahora.strftime("%Y-%m")
        turnos = self.cargar_turnos()

        turnos_mes = [t for t in turnos if t["inicio"].startswith(mes_actual)]
        total = sum(t["ingresos"] for t in turnos_mes)

        if turnos_mes:
            mensaje = f"📆 Ventas del mes ({mes_actual}):\n"
            dias = {}
            for t in turnos_mes:
                fecha = t["inicio"][:10]
                dias.setdefault(fecha, []).append(t["ingresos"])
            for fecha, ingresos in dias.items():
                mensaje += f" - {fecha}: ${sum(ingresos)}\n"
            mensaje += f"\n💰 Total del mes: ${total}"
        else:
            mensaje = "No hay turnos registrados este mes."

        messagebox.showinfo("Reporte Mensual", mensaje)
