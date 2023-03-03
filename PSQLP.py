
import psycopg2

# Establecemos la conexión a la base de datos
try:
    conn = psycopg2.connect(user='mario', password='mario', host='localhost', database='database_name')
except psycopg2.connect.Error as err:
    print(f"Error al conectarse a la base de datos: {err}")
    exit()

# Creamos un cursor para ejecutar las consultas SQL
cursor = conn.cursor()

def listar_jugadores():
    # Consulta para obtener la lista de jugadores y el total de jugadores
    query = """
            SELECT nombre_entrenador, COUNT(*) AS total_jugadores
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            GROUP BY nombre_entrenador;
            """

    # Ejecutamos la consulta
    try:
        cursor.execute(query)
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()

    # Recuperamos los resultados
    for (nombre_entrenador, total_jugadores) in cursor:
        print(nombre_entrenador, total_jugadores)

def buscar_jugadores_entrenador(nombre_entrenador):
    # Consulta para buscar jugadores cuyo entrenador tenga por nombre "Manolo"
    query = """
            SELECT id_jugador, nombre_entrenador
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = %s;
            """

    # Ejecutamos la consulta con el nombre de entrenador proporcionado
    try:
        cursor.execute(query, (nombre_entrenador))
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()

    # Recuperamos los resultados
    for (id_jugador, nombre_entrenador) in cursor:
        print(id_jugador, nombre_entrenador)

def mostrar_entrenador_jugadores():
    # Pedimos el nombre del entrenador
    nombre_entrenador = input("Introduce el nombre del entrenador: ")

    # Consulta para obtener los datos del entrenador y los jugadores que entrena
    query = """
            SELECT *
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = %s;
            """

    # Ejecutamos la consulta con el nombre de entrenador proporcionado
    try:
        cursor.execute(query, (nombre_entrenador))
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()

    # Recuperamos los resultados
    for (nlicencia, nombre_entrenador, email, id_jugador, posicion_ant_camp, coef_elo, altura) in cursor:
        print("Entrenador: ", nlicencia, nombre_entrenador, email)
        print("Jugador: ", id_jugador, posicion_ant_camp, coef_elo, altura)

def insertar_jugador(id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura):
    # Consulta para insertar un nuevo jugador en la tabla Jugador
    query = """
            INSERT INTO Jugador (id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura)
            VALUES (%s, %s, %s, %s, %s);
            """

    # Ejecutamos la consulta con los datos del nuevo jugador
    try:
        cursor.execute(query, (id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura))
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()
    # Hacemos commit para guardar los cambios en la base de datos
    conn.commit()

def eliminar_jugadores_entrenador(nombre_entrenador):
    # Consulta para eliminar jugadores cuyo entrenador tenga por nombre el proporcionado
    query = """
        DELETE FROM Jugador
        WHERE nlicencia IN (
        SELECT nlicencia FROM Entrenador WHERE nombre_entrenador = %s);
        """
    try:
        cursor.execute(query, (nombre_entrenador))
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()
    # Hacemos commit para guardar los cambios en la base de datos
    conn.commit()
    # Mostramos el número de filas eliminadas
    print(cursor.rowcount, "jugadores eliminados")
    
def actualizar_jugador(id_jugador, altura, coef_elo):
    # Consulta para actualizar la altura y el coeficiente elo de un jugador existente en la tabla Jugador
    query = """
            UPDATE Jugador
            SET altura= %s, coef_elo = %s 
            WHERE id_jugador = %s;
            """
    try:
        cursor.execute(query, (altura, coef_elo, id_jugador))
    except psycopg2.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()
    conn.commit()
    cursor.close()
    conn.close()


def menu():
    print("-------------------------------------------")
    print("Proyecto de BBDD")
    print("\n")
    print("1. Mostrar la cantidad de jugadores que hay en la lista participantes y lista los jugadores")
    print("2. Buscar jugadores cuyo entrenador tenga por nombre Manolo")
    print("3. Pide por teclado un entrenador y muestra sus datos y los jugadores a los que entrena")
    print("4. Inserta en la tabla Jugador un nuevo jugador")
    print("5. Elimina a los jugadores cuyo entrenador tenga por nombre Agosto")
    print("6. Actualizar la altura y coeficiente elo de un jugador que ya ha sido registrado")
    print("7. Salir")
    print("\n")
    print("-------------------------------------------")
    opcion=int(input("Seleccione una de las opciones: "))
    return opcion