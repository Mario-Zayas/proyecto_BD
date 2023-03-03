from OraP import *
opcion = menu()
while opcion != 7:
    if opcion == 1:
        listar_jugadores()
    elif opcion == 2:
        nombre_entrenador = input("Ingrese el nombre del entrenador: ")
        buscar_jugadores_entrenador(nombre_entrenador)
    elif opcion == 3:
        mostrar_entrenador_jugadores()
    elif opcion == 4:
        id_jugador = input("Ingrese el ID del jugador: ")
        nlicencia = input("Ingrese la licencia del entrenador: ")
        posicion_ant_camp = input("Ingrese la posición del jugador en el campeonato anterior: ")
        coef_elo = input("Ingrese el coeficiente ELO del jugador: ")
        altura = input("Ingrese la altura del jugador: ")
        insertar_jugador(id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura)
    elif opcion == 5:
        nombre_entrenador = input("Ingrese el nombre del entrenador: ")
        eliminar_jugadores_entrenador(nombre_entrenador)
    elif opcion == 6:
        id_jugador = input("Ingrese el ID del jugador: ")
        nueva_posicion = input("Ingrese la nueva posición del jugador: ")
        nueva_altura = input("Ingrese la nueva altura del jugador: ")
        actualizar_jugador(id_jugador, nueva_posicion, nueva_altura)
    elif opcion == 7:
        print("")
    else:
        print("Opción no válida, utilice una opción válida.")
    opcion = menu()