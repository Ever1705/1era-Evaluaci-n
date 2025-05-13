import random
import Utilities
from Animations import Animations
# -------------------------------------------------------------------------
# Clase para el sistema de combate
# -------------------------------------------------------------------------
class BattleSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.animations = Animations()
        
        # Cálculo del daño base para ambos personajes
        self.damage_player = self._calculate_damage(player, enemy)
        self.damage_enemy = self._calculate_damage(enemy, player)
        
        # Cálculo del daño crítico (50% más)
        self.critical_player = round(1.5 * self.damage_player, 2)
        self.critical_enemy = round(1.5 * self.damage_enemy, 2)
    
    def _calculate_damage(self, attacker, defender):
        """Calcula el daño base según la fórmula del juego"""
        damage = 0.01 * 0.5 * 85 * (
            ((0.2 * attacker.level + 1) * attacker.atk * 40) / 
            (25 * defender.defense) + 2
        )
        return round(damage, 2)
    
    def determine_player_action(self, choice):
        """Determina la acción final del jugador basada en su elección y probabilidad"""
        self.player.action = choice
        
        # Número aleatorio para determinar crítico o fallo
        player_prob = random.randint(1, 10)
        
        # Si ataca, tiene 20% de probabilidad de crítico
        if self.player.action == 1 and player_prob <= 2:
            self.player.action = 3  # Crítico
        
        # Si esquiva, tiene 50% de probabilidad de fallar
        elif self.player.action == 2 and 3 <= player_prob <= 7:
            self.player.action = 4  # Defensa fallida
    
    def determine_enemy_action(self):
        """Determina la acción del enemigo de forma aleatoria"""
        # Probabilidad para crítico o fallo
        enemy_prob = random.randint(1, 10)
        
        # Acción aleatoria: 1 = atacar, 2 = esquivar
        self.enemy.action = random.randint(1, 2)
        
        # 20% de probabilidad de ataque crítico
        if self.enemy.action == 1 and enemy_prob <= 2:
            self.enemy.action = 3
        
        # 50% de probabilidad de fallo en esquivar
        elif self.enemy.action == 2 and 3 <= enemy_prob <= 7:
            self.enemy.action = 4
    
    def process_battle_round(self):
        """Procesa una ronda completa de batalla y devuelve la animación y mensaje"""
        Utilities.clear_screen()
        
        # Ambos atacan (normal o crítico)
        if (self.player.action in [1, 3]) and (self.enemy.action in [1, 3]):
            # Procesar daño del jugador
            if self.player.action == 3:  # Crítico
                self.enemy.ps -= self.damage_player + self.critical_player
            else:  # Normal
                self.enemy.ps -= self.damage_player
            
            # Procesar daño del enemigo
            if self.enemy.action == 3:  # Crítico
                self.player.ps -= self.damage_enemy + self.critical_enemy
            else:  # Normal
                self.player.ps -= self.damage_enemy
            
            return {
                'animation': self.animations.multiple_attack,
                'message': "Ataque múltiple",
                'player_hit_type': "¡CRÍTICO!" if self.player.action == 3 else "Normal",
                'enemy_hit_type': "¡CRÍTICO!" if self.enemy.action == 3 else "Normal"
            }
        
        # Jugador ataca y enemigo no puede defenderse
        elif (self.player.action in [1, 3]) and self.enemy.action == 4:
            if self.player.action == 3:  # Crítico
                self.enemy.ps -= self.damage_player + self.critical_player
            else:  # Normal
                self.enemy.ps -= self.damage_player
            
            return {
                'animation': self.animations.attack_enemy,
                'message': "Ataque directo",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Jugador no puede defenderse y enemigo ataca
        elif self.player.action == 4 and (self.enemy.action in [1, 3]):
            if self.enemy.action == 3:  # Crítico
                self.player.ps -= self.damage_enemy + self.critical_enemy
            else:  # Normal
                self.player.ps -= self.damage_enemy
            
            return {
                'animation': self.animations.attack_player,
                'message': "Daño directo",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Jugador se defiende con éxito y enemigo ataca
        elif self.player.action == 2 and (self.enemy.action in [1, 3]):
            return {
                'animation': self.animations.player_dodge,
                'message': "Esquivaste el ataque",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Jugador ataca y enemigo se defiende con éxito
        elif (self.player.action in [1, 3]) and self.enemy.action == 2:
            return {
                'animation': self.animations.enemy_dodge,
                'message': "Fallaste el ataque",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Ambos se defienden
        elif self.player.action == 2 and self.enemy.action == 2:
            return {
                'animation': self.animations.player_enemy_dodge,
                'message': "Ambos se defienden",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Ambos fallan al defenderse
        elif (self.player.action in [2, 4]) and (self.enemy.action in [2, 4]):
            return {
                'animation': self.animations.player_enemy_confuse,
                'message': "Ambos no pueden defenderse",
                'player_hit_type': None,
                'enemy_hit_type': None
            }
        
        # Caso por defecto (no debería ocurrir)
        return {
            'animation': self.animations.player_enemy,
            'message': "...",
            'player_hit_type': None,
            'enemy_hit_type': None
        }
    
    def check_battle_end(self):
        """Verifica si la batalla ha terminado y devuelve el resultado"""
        if not self.player.is_alive() or not self.enemy.is_alive():
            if not self.player.is_alive():
                return {
                    'animation': self.animations.player_dead,
                    'message': "El enemigo gana"
                }
            else:
                return {
                    'animation': self.animations.enemy_dead,
                    'message': "Tú ganas"
                }
        return None
