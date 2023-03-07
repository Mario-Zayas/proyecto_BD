from MBDP import *
db=Conectar_BD("localhost","raul","raul","Jota")
opcion = menu()
while opcion != 7:
    opcion = menu()
    if opcion == 1:
        listar_jugadores(db)
    elif opcion == 2:
        nombre_entrenador = input("Introduce el nombre del entrenador: ")
        buscar_jugadores_entrenador(nombre_entrenador, db)
    elif opcion == 3:
        mostrar_entrenador_jugadores(db)
    elif opcion == 4:
        jugadores = []
        num_jugadores = int(input("Introduce el número de jugadores a insertar: "))
        for i in range(num_jugadores):
            id_jugador = input("Introduce el ID del jugador: ")
            nlicencia = input("Introduce el número de licencia del entrenador: ")
            posicion_ant_camp = input("Introduce la posición anterior en el campeonato: ")
            coef_elo = input("Introduce el coeficiente Elo: ")
            altura = input("Introduce la altura: ")
            jugadores.append((id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura))
        insertar_jugador(jugadores, db)
    elif opcion == 5:
        nombre_entrenador = input("Introduce el nombre del entrenador: ")
        eliminar_jugadores_entrenador(nombre_entrenador, db)
    elif opcion == 6:
        id_jugador = input("Introduce el ID del jugador a actualizar: ")
        altura = input("Introduce la nueva altura: ")
        coef_elo = input("Introduce el nuevo coeficiente Elo: ")
        actualizar_jugador(id_jugador, altura, coef_elo, db)
    elif opcion == 7:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")

