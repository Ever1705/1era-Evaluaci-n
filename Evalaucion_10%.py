import random,os,time

# Animaciones de las acciones en el juego

playerEnemy = """
      __________                       __________
      |        |                       | \\   /  |
      |  ^   ^ |                       | ~   ~  |
      |   \\_/  |                       |  ===   |
      ----------                       ----------
"""

enemyDead = """
      __________                       __________
      |        |                       |        |
      |  ·   · |                       | +   +  |
      |    _   |                       |  ___   |
      ----------                       ----------
"""

playerDead = """
      __________                       __________
      |        |                       | \\   /  |
      |  +   + |                       | ~   ~  |
      |   ___  |                       |  \\_/   |
      ----------                       ----------
"""

playerDodge = """
      __________     )))               __________
      |        |     )))               | \\   /  |
      |  ^   ^ |     )))               | ~   ~  |
      |   \\_/  |     )))               |  ===   |
      ----------     )))               ----------
"""

enemyDodge = """
      __________                    (((   __________
      |        |                    (((   | \\   /  |
      |  ^   ^ |                    (((   | ~   ~  |
      |   \\_/  |                    (((   |  ===   |
      ----------                    (((   ----------
"""

playerEnemyDodge = """
      __________    )))            (((   __________
      |        |    )))            (((   | \\   /  |
      |  ^   ^ |    )))            (((   | ~   ~  |
      |   \\_/  |    )))            (((   |  ===   |
      ----------    )))            (((   ----------
"""

multipleAtack = """
           !                               !
      __________                       __________
      |        |                       |        |
      |  *   * |                       | #   #  |
      |    #   |                       |  ===   |
      ----------                       ----------
"""

atackEnemy = """
                                           !
      __________                       __________
      |        |                       |         |
      |  ^   ^ |                       | #   #   |
      |   \\_/  |                       |  ===    |
      ----------                       ----------
"""

atackPlayer = """
           !                                
      __________                       __________
      |        |                       | \\   /  |
      |  *   * |                       | ~   ~  |
      |    #   |                       |  ===   |
      ----------                       ----------
"""

playerEnemyConfuse = """
          ?                                ?
      __________                       __________
      |        |                       | \\   /  |
      |  ^   ^ |                       | ~   ~  |
      |   \\_/  |                       |  ===   |
      ----------                       ----------
"""

# Variables que se usaran para la aleatoriedad de cada uno
playerProb = 0
enemyProb = 0

# Jugador
playerStats = {
    'level':5,
    'ps':19,
    'atk':52,
    'def':43,
    'attack':False,
    'dodge':False,
    'des': 0
}
# Enemigo
enemyStats = {
    'level':5,
    'ps':24,
    'atk':48,
    'def':65,
    'attack':False,
    'dodge':False,
    'des': 0
}

# Formulas para el calculo del daño se realizan cada uno en funcion de atributos de ambos
damagePla = round((0.01 * 0.5 * 85 * (((0.2 * playerStats['level'] + 1) *playerStats['atk'] * 40) / (25 * enemyStats['def']) + 2)),2)
damageEne = round((0.01 * 0.5 * 85 * (((0.2 * enemyStats['level'] + 1) * enemyStats['atk'] * 40) / (25 * playerStats['def']) + 2)),2)

# Formulas para el critico del jugador y el enemigo
critickPla = round(1.5 * damagePla , 2)
critickEne = round(1.5 * damageEne, 2)

# Variables para la ejecucion del bucle principal y bucle del gameplay
run = True
runGame = False

# Bucle principal
while(run):

    playerPs = playerStats['ps']
    enemyPs = enemyStats['ps']
    
    os.system('cls' if os.name == 'nt' else 'clear') #Esto limpia la terminal

    # Menu de inicio
    print(F"""
              -----------------------------------------------------------
              |                 Bienvenido a Battle Demo                |
              |                                                         |
              |   1 ===> Jugar                                          |
              |   2 ===> Reglas                                         |
              |   3 ===> Salir                                          |
              |                                                         |
              -----------------------------------------------------------""")
    # Bloque para pedir un numero segun la opcion existente
    try:
        choice = int(input("              Eleccion: "))
        
        # Para cuando se ingresa un numero mayor o menor de los existentes
        if choice < 1 or choice > 3:
            print('\n              Escriba una opcion existente')
            time.sleep(1)

        # Para la opcion 2
        elif choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(F"""
              -----------------------------------------------------------
              |                      Reglas:                            |
              |                                                         |
              |   El jugador y el enemigo solo atacan y esquivan        |
              |   pero existe la posibilidad que al atacar se produsca  |
              |   un ataque critico y al esquivar no se pueda esquivar. |
              |                                                         |
              |   El juego termina cuando uno de los caiga en combate.  |
              |                                                         |
              |                     Disfruta :>                         |
              -----------------------------------------------------------""")
            input("\n              Presiona una tecla para continuar...")

        # Para la opcion 3
        elif choice == 3:
            # Simulacion de espera
            print("              Cerrando.", end='\r')  
            time.sleep(0.25)
            print("              Cerrando..", end='\r')
            time.sleep(0.25)
            print("              Cerrando...", end='\r')
            time.sleep(0.25)

            # Termina la ejecucion del programa
            run = False
            
            os.system('cls' if os.name == 'nt' else 'clear')


        # Para la opcion 1 la cual inicia el gameplay
        elif choice == 1:
            # Simulacion de carga de inicio
            print("Cargando.", end='\r')  
            time.sleep(0.25)
            print("Cargando..", end='\r')
            time.sleep(0.25)
            print("Cargando...", end='\r')
            time.sleep(0.25)

            # Inicia el juego
            runGame = True
            while runGame:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n')
                

                # Impresion de la vida y dibujo de los personajes en la terminal

                print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                print(playerEnemy)

                # Eleccion del jugador
                try:
                    playerStats['des'] = int(input(f"""         1: Atacar              2:Esquivar
                    Elije: """))

                    # Si es diferente se salta la iteracion
                    if(playerStats['des'] < 1 or playerStats['des'] > 2):
                        print("Elije una opcion real")
                        time.sleep(0.5)
                        playerStats['des'] = 0;
                        continue

                # Si no es un numero se salta la iteracion
                except:
                    print("Elije un numero")
                    time.sleep(0.5)
                    playerStats['des'] = 0;
                    continue


                # Acciones del enemigo segun los numeros aleario que se obtengan
                # Numero aleatorio del jugador del 1 al 10 para el critico o para fallar la defensa
                enemyProb = random.randint(1,10)

                # Accion aleatoria de ataque o defensa
                enemyStats['des'] = random.randint(1,2)
                
                # Verificacion del resultado para el Ataque
                if enemyStats['des'] == 1:
                    if (enemyProb >=1 and enemyProb <=2):
                        enemyStats['des'] = 3
                # Verificacion del resultado para la Defensa
                elif enemyStats['des'] == 2:
                    if (enemyProb >=3 and enemyProb <=7):
                        enemyStats['des'] = 4  

                # Acciones del personaje segun el numero aleario que se obtuvo  y la accion elegida

                # Numero aleatorio del jugador del 1 al 10
                playerProb = random.randint(1,10)

                # Ataque del personaje
                if playerStats['des'] == 1:
                    # Numeros correspondientes al valor aleatorio obtenido anteriormente
                    if playerProb >= 1 and playerProb <= 2:
                        #  Si era alguno de los anteriores es un ataque critico
                         playerStats['des'] = 3

                # Defensa del personaje
                if playerStats['des'] == 2:
                    # Numeros correspondientes al valor aleatorio obtenido anteriormente                    
                    if (playerProb >= 3 and playerProb <= 7):
                        #  Si era alguno de los anteriores es un la defensa falla
                        playerStats['des'] = 4

                
                # Acciones en la batalla segun los resultados obtenidos de ambos personajes
                os.system('cls' if os.name == 'nt' else 'clear')


                # En ataques multiples normales o criticos
                if (playerStats['des'] == 1 or playerStats['des'] == 3) and (enemyStats['des'] == 1 or enemyStats['des'] == 3):
      
                    # Se verifica que tipo de daño realizo el jugador
                    if playerStats['des'] == 3:
                        enemyStats['ps']-= (damagePla + (damagePla * critickPla))
                    elif playerStats['des'] == 1:
                        enemyStats['ps']-=damagePla

                    # Se verifica que tipo de daño realizo el enemigo
                    if enemyStats['des'] == 3:
                        playerStats['ps']-=(damageEne + (damageEne * critickEne))
                    elif enemyStats['des'] == 1:
                        playerStats['ps'] -= damageEne

                    # Se imprime despues
                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    # Dependiendo que tipo de daño reciben se refleja abajo si fue normal o critico
                    print(f'      {"¡CRITICO!" if enemyStats['des'] == 3 else "Normal"}                                { "¡CRITICO!" if playerStats['des'] == 3 else "Normal"}')
                    print(multipleAtack)
                    print("Ataque multiple")
                    time.sleep(1.5)
                
                # Cuando el jugador ataca y el enemigo no se puede defender 
                elif ((playerStats['des']== 1 or playerStats['des']== 3) and enemyStats['des'] == 4):

                    # cuando es Critico
                    if playerStats['des'] == 3:
                        enemyStats['ps']-= (damagePla + (damagePla * critickPla))
                    # cuando es Normal
                    else:
                        enemyStats['ps']-=damagePla


                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(atackEnemy)
                    print("Ataque directo")
                    time.sleep(1.5)


                # Cuando el jugador no se puede defender y el enemigo ataca 
                elif (playerStats['des']== 4 and (enemyStats['des'] == 1 or enemyStats['des'] == 3)):

                    # cuando es Critico
                    if enemyStats['des'] == 3:
                        playerStats['ps']-= (damageEne + (damageEne * critickEne))
                    # cuando es Normal
                    else:
                        playerStats['ps']-= damageEne

                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(atackPlayer)
                    print("Daño directo")
                    time.sleep(1.5)

                # Cuando el jugador se defiende y el enemigo ataca
                elif (playerStats['des']== 2 and (enemyStats['des'] == 1 or enemyStats['des'] == 3)):
                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(playerDodge)
                    print("Esquivaste el ataque")
                    time.sleep(1.5)
                

                # Cuando el jugador ataqua y el enemigo se bloquea
                elif ((playerStats['des']== 1 or playerStats['des']== 3) and enemyStats['des'] == 2):
                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(enemyDodge)
                    print("Fallaste el ataque")
                    time.sleep(1.5)

                # Cuando los dos se defienden
                elif (playerStats['des']== 2 and enemyStats['des'] == 2):
                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(playerEnemyDodge)
                    print("Ambos se defienden")
                    time.sleep(1.5)

                # Para cuando ambos jugadores fallan el bloqueo
                elif ((playerStats['des']== 4 or playerStats['des']== 2) and (enemyStats['des'] == 4 or enemyStats['des'] == 2)):
                    print(f"\n\n   · Jugador: {round(playerStats['ps'],2)} ♥                  · Enemigo: {round(enemyStats['ps'],2)} ♥")
                    print(playerEnemyConfuse)
                    print("Ambos no puenden defenderse")
                    time.sleep(1.5)


                # Cuando alguno de los dos cae en batalla
                os.system('cls' if os.name == 'nt' else 'clear')

                if(playerStats['ps'] <=0 or enemyStats['ps'] <=0):
                    # Si fue el jugador
                    if(playerStats['ps'] <=0):
                        print(playerDead)
                        print("El enemigo gana")
                        input("Preciona una tecla para continuar...")

                    # Si fue el enemigo
                    elif(enemyStats['ps'] <=0):
                        print(enemyDead)
                        print("Tu ganas")
                        input("Preciona una tecla para continuar...")
                    
                    # Se reestablecen los puntos de salud para otra batalla
                    playerStats['ps'] = playerPs
                    enemyStats['ps']=enemyPs
                    runGame = False

    # Si la eleccion de juego no es un numero
    except:
        print("\n              Escriba un numero real")
        time.sleep(1)

        
