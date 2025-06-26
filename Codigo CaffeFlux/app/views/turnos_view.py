import tkinter as tk
from tkinter import ttk

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
        print("Turno abierto")

    def cerrar_turno(self):
        print("Turno cerrado")
