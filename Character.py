# -------------------------------------------------------------------------
# Clase para los personajes (jugador o enemigo)
# -------------------------------------------------------------------------

class Character:
    def __init__(self, level, ps, atk, defense):
        self.level = level
        self.ps = ps
        self.initial_ps = ps  # Guardamos los PS iniciales para reiniciar
        self.atk = atk
        self.defense = defense
        self.action = 0       # 0: ninguna, 1: ataque normal, 2: esquivar, 3: crítico, 4: esquivar fallido
    
    def reset_health(self):
        self.ps = self.initial_ps
    
    def is_alive(self):
        return self.ps > 0