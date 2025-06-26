# app/utils/theme.py

current_theme = {
    "bg": "#ffffff",       # Fondo claro inicial
    "fg": "#000000",       # Texto oscuro
    "accent": "#4B3621"    # Marrón para títulos
}

def toggle_theme():
    """Alterna entre claro y oscuro suave."""
    if current_theme["bg"] == "#ffffff":
        current_theme["bg"] = "#1e1e1e"        # Gris oscuro (no negro)
        current_theme["fg"] = "#f5f5f5"
        current_theme["accent"] = "#f5c46b"    # Dorado suave para contraste
    else:
        current_theme["bg"] = "#ffffff"
        current_theme["fg"] = "#000000"
        current_theme["accent"] = "#4B3621"
