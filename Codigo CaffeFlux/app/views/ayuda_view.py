import tkinter as tk

class AyudaView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, bg="#ffffff")
        self.controller = controller  # Por si en el futuro necesitas volver al menú principal
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Centro de Ayuda", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#4B3621").pack(pady=20)
        mensaje = (
            "Bienvenido a CafféFlux.\n\n"
            "Desde aquí puedes gestionar tus productos, turnos, reportes\n"
            "y mucho más. Para asistencia técnica, contacta con el equipo de soporte.\n\n"
            "Gracias por utilizar CafféFlux."
        )
        tk.Label(self, text=mensaje, font=("Helvetica", 12), bg="#ffffff", justify="center").pack(pady=10)
