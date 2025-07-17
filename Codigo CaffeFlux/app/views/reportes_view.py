import tkinter as tk
from tkinter import ttk

class ReportesView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reportes Financieros")
        self.geometry("800x600")
        self.configure(bg="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Reportes Financieros",
            font=("Helvetica", 20, "bold"),
            fg="#4B3621",
            bg="#ffffff"
        )
        title_label.pack(pady=20)

        frame = tk.Frame(self, bg="#ffffff")
        frame.pack(pady=20)

        ttk.Button(frame, text="Ver Ventas del Día", command=self.ver_ventas_dia).pack(pady=5)
        ttk.Button(frame, text="Ver Reporte Mensual", command=self.ver_ventas_mes).pack(pady=5)

    def ver_ventas_dia(self):
        print("Reporte diario mostrado")

    def ver_ventas_mes(self):
        print("Reporte mensual mostrado")
