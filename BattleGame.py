import time
import Utilities
from Character import Character
from BattleSystem import BattleSystem

# -------------------------------------------------------------------------
# Clase para el manejo del juego completo
# -------------------------------------------------------------------------
class BattleGame:
    def __init__(self):
        # Crear los personajes
        self.player = Character(level=5, ps=19, atk=52, defense=43)
        self.enemy = Character(level=5, ps=24, atk=48, defense=65)
        
        # Inicializar el sistema de batalla
        self.battle_system = BattleSystem(self.player, self.enemy)
        
        # Estado del juego
        self.running = True
        self.in_battle = False
    
    def display_main_menu(self):
        """Muestra el menú principal del juego"""
        Utilities.clear_screen()
        print("""
              -----------------------------------------------------------
              |                 Bienvenido a Battle Demo                |
              |                                                         |
              |   1 ===> Jugar                                          |
              |   2 ===> Reglas                                         |
              |   3 ===> Salir                                          |
              |                                                         |
              -----------------------------------------------------------""")
    
    def show_rules(self):
        """Muestra las reglas del juego"""
        Utilities.clear_screen()
        print("""
              -----------------------------------------------------------
              |                      Reglas:                            |
              |                                                         |
              |   El jugador y el enemigo solo atacan y esquivan        |
              |   pero existe la posibilidad que al atacar se produzca  |
              |   un ataque crítico y al esquivar no se pueda esquivar. |
              |                                                         |
              |   El juego termina cuando uno de los caiga en combate.  |
              |                                                         |
              |                     Disfruta :>                         |
              -----------------------------------------------------------""")
        input("\n              Presiona una tecla para continuar...")
    
    def close_game(self):
        """Cierra el juego con una animación"""
        print("              Cerrando.", end='\r')  
        time.sleep(0.25)
        print("              Cerrando..", end='\r')
        time.sleep(0.25)
        print("              Cerrando...", end='\r')
        time.sleep(0.25)
        
        self.running = False
        Utilities.clear_screen()
    
    def start_battle(self):
        """Inicia la secuencia de batalla"""
        print("Cargando.", end='\r')  
        time.sleep(0.25)
        print("Cargando..", end='\r')
        time.sleep(0.25)
        print("Cargando...", end='\r')
        time.sleep(0.25)
        
        self.in_battle = True
        self.run_battle_loop()
    
    def display_battle_status(self):
        """Muestra el estado actual de la batalla"""
        Utilities.clear_screen()
        print('\n')
        print(f"\n\n   · Jugador: {round(self.player.ps, 2)} ♥                  · Enemigo: {round(self.enemy.ps, 2)} ♥")
        print(self.battle_system.animations.player_enemy)
    
    def get_player_action(self):
        """Obtiene la acción elegida por el jugador"""
        try:
            choice = int(input("""         1: Atacar              2:Esquivar
                    Elije: """))
            
            if choice < 1 or choice > 2:
                print("Elije una opción real")
                time.sleep(0.5)
                return 0
            return choice
        except:
            print("Elije un número")
            time.sleep(0.5)
            return 0
    
    def show_battle_result(self, result):
        """Muestra el resultado de una acción de batalla"""
        Utilities.clear_screen()
        print(f"\n\n   · Jugador: {round(self.player.ps, 2)} ♥                  · Enemigo: {round(self.enemy.ps, 2)} ♥")
        
        # Si hay tipos de golpe, mostrarlos
        if result['player_hit_type'] is not None and result['enemy_hit_type'] is not None:
            print(f"      {result['enemy_hit_type']}                                {result['player_hit_type']}")
        
        print(result['animation'])
        print(result['message'])
        time.sleep(1.5)
    
    def check_and_show_battle_end(self):
        """Verifica si la batalla ha terminado y muestra el resultado"""
        result = self.battle_system.check_battle_end()
        if result:
            Utilities.clear_screen()
            print(result['animation'])
            print(result['message'])
            input("Presiona una tecla para continuar...")
            
            # Reiniciar la salud de los personajes
            self.player.reset_health()
            self.enemy.reset_health()
            self.in_battle = False
            return True
        
        return False
    
    def run_battle_loop(self):
        """Ejecuta el bucle principal de la batalla"""
        while self.in_battle:
            # Mostrar el estado de la batalla
            self.display_battle_status()
            
            # Obtener la acción del jugador
            player_choice = self.get_player_action()
            if player_choice == 0:
                continue  # Si la entrada fue inválida, solicitar de nuevo
            
            # Determinar la acción final del jugador y del enemigo
            self.battle_system.determine_player_action(player_choice)
            self.battle_system.determine_enemy_action()
            
            # Procesar la ronda de batalla
            result = self.battle_system.process_battle_round()
            self.show_battle_result(result)
            
            # Verificar si la batalla ha terminado
            if self.check_and_show_battle_end():
                break
    
    def run(self):
        """Ejecuta el bucle principal del juego"""
        while self.running:
            self.display_main_menu()
            
            try:
                choice = int(input("              Elección: "))
                
                if choice < 1 or choice > 3:
                    print('\n              Escriba una opción existente')
                    time.sleep(1)
                
                elif choice == 1:  # Jugar
                    self.start_battle()
                
                elif choice == 2:  # Reglas
                    self.show_rules()
                
                elif choice == 3:  # Salir
                    self.close_game()
                
            except ValueError:
                print("\n              Escriba un número real")
                time.sleep(1)