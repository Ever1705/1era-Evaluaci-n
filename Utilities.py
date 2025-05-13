import os
# -------------------------------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------------------------------

def clear_screen():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')