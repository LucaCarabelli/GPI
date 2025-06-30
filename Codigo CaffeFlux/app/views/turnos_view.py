import tkinter as tk
from tkinter import ttk, messagebox
from controllers.abrir_turno import abrir_turno
from controllers.cerrar_turno import cerrar_turno

class TurnosView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Turnos")
        self.geometry("800x600")
        self.configure(bg="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self,
            text="Gestión de Turnos",
            font=("Helvetica", 20, "bold"),
            fg="#4B3621",
            bg="#ffffff"
        )
        title_label.pack(pady=20)

        frame = tk.Frame(self, bg="#ffffff")
        frame.pack(pady=20)

        ttk.Button(frame, text="Abrir Turno", command=self.abrir_turno).grid(row=0, column=0, padx=10)
        ttk.Button(frame, text="Cerrar Turno", command=self.cerrar_turno).grid(row=0, column=1, padx=10)

    def abrir_turno(self):
        hora = abrir_turno()
        if hora:
            messagebox.showinfo("Turno Abierto", f"Turno iniciado a las {hora}")
        else:
            messagebox.showwarning("Error", "Ya hay un turno abierto sin cerrar.")

    def cerrar_turno(self):
        ingresos = 50000  # En esta versión simulamos ingresos
        hora = cerrar_turno(ingresos)
        if hora:
            messagebox.showinfo("Turno Cerrado", f"Turno cerrado a las {hora}\nIngresos: ${ingresos}")
        else:
            messagebox.showwarning("Error", "No hay turno abierto para cerrar.")
