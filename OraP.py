
import cx_Oracle

try:
        conn = cx_Oracle.connect(user='username', password='password', dsn='hostname:port/service_name')
except cx_Oracle.connect.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")
        exit()


cursor = conn.cursor()

def listar_jugadores():

    query = """
            SELECT nombre_entrenador, COUNT(*) AS total_jugadores
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            GROUP BY nombre_entrenador
            """

    try:
        cursor.execute(query)
        for (nombre_entrenador, total_jugadores) in cursor:
            print(nombre_entrenador, total_jugadores)
    except cx_Oracle.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()



def buscar_jugadores_entrenador(nombre_entrenador):

    query = """
            SELECT id_jugador, nombre_entrenador
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = :nombre_entrenador
            """


    try:
        cursor.execute(query, nombre_entrenador=nombre_entrenador)
        for (id_jugador, nombre_entrenador) in cursor:
            print(id_jugador, nombre_entrenador)
    except cx_Oracle.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()



def mostrar_entrenador_jugadores():

    nombre_entrenador = input("Introduce el nombre del entrenador: ")


    query = """
            SELECT *
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = :nombre_entrenador
            """


    try:
        cursor.execute(query, nombre_entrenador=nombre_entrenador)
        for (nlicencia, nombre_entrenador, email, id_jugador, posicion_ant_camp, coef_elo, altura) in cursor:
            print("Entrenador: ", nlicencia, nombre_entrenador, email)
            print("Jugador: ", id_jugador, posicion_ant_camp, coef_elo, altura)
    except cx_Oracle.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()

def insertar_jugador(jugadores):
    query = """
        INSERT INTO Jugador (id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura)
        VALUES (%s, %s, %s, %s, %s);
    """
    try:
        cursor = conn.cursor()
        for jugador in jugadores:
            cursor.execute(query, jugador)
        conn.commit()
        cursor.close()
        print(f"Se han insertado {len(jugadores)} jugadores.")
    except cx_Oracle.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()


    
    
    conn.commit()

def eliminar_jugadores_entrenador(nombre_entrenador):
    query = """
        DELETE FROM Jugador
        WHERE nlicencia IN (
            SELECT nlicencia
            FROM Entrenador
            WHERE nombre_entrenador = %s
        );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query, (nombre_entrenador,))
        num_jugadores_eliminados = cursor.rowcount
        conn.commit()
        cursor.close()
        print(f"Se han eliminado {num_jugadores_eliminados} jugadores del entrenador {nombre_entrenador}.")
    except cx_Oracle.connect.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        conn.close()
        exit()

    
    conn.commit()

def actualizar_jugador(id_jugador, altura, coef_elo):
    
    query = """
            UPDATE Jugador
            SET altura= %s, coef_elo = %s 
            WHERE id_jugador = %s;
            """
    try:
        cursor.execute(query, (altura, coef_elo, id_jugador))
    except cx_Oracle.connect.Error as err:
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
