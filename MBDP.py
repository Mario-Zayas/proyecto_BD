import mysql.connector


def Conectar_BD(host, usuario, password, database):
    try:
        db = mysql.connector.connect(
            host=host,
            user=usuario,
            password=password,
            database=database
        )

        return db
    except mysql.connector.Error as e:
        print("No puedo conectar a la base de datos:", e)
        return None




def listar_jugadores(db):
    cursor = db.cursor()
    
    try:
        query = """
            SELECT nombre_entrenador, COUNT(*) AS total_jugadores
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            GROUP BY nombre_entrenador;
            """
        cursor.execute(query)
        for (nombre_entrenador, total_jugadores) in cursor:
            print(nombre_entrenador, total_jugadores)
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        exit()


def buscar_jugadores_entrenador(nombre_entrenador, db):
    cursor = db.cursor()
    
    try:
        query = """
            SELECT id_jugador, nombre_entrenador
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = %s;
            """
        cursor.execute(query, (nombre_entrenador,))
        for (id_jugador, nombre_entrenador) in cursor:
            print(id_jugador, nombre_entrenador)
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()
    

def mostrar_entrenador_jugadores(db):
    cursor = db.cursor()
    nombre_entrenador = input("Introduce el nombre del entrenador: ")
    
    try:
        query = """
            SELECT *
            FROM Entrenador JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE nombre_entrenador = %s;
            """
        cursor.execute(query, (nombre_entrenador,))
        for (nlicencia, nombre_entrenador, email, id_jugador, posicion_ant_camp, coef_elo, altura) in cursor:
            print("Entrenador: ", nlicencia, nombre_entrenador, email)
            print("Jugador: ", id_jugador, posicion_ant_camp, coef_elo, altura)
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()

    

def insertar_jugador(jugadores,db):
    
    cursor = db.cursor()
    try:
        query = """
        INSERT INTO Jugador (id_jugador, nlicencia, posicion_ant_camp, coef_elo, altura)
        VALUES (%s, %s, %s, %s, %s);
    """
        cursor = db.cursor()
        for jugador in jugadores:
            cursor.execute(query, jugador)
        db.commit()
        cursor.close()
        print(f"Se han insertado {len(jugadores)} jugadores.")
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()


    
    
    db.commit()

def eliminar_jugadores_entrenador(nombre_entrenador,db):
    cursor=db.cursor()
    try:
        query = """
        DELETE FROM Jugador
        WHERE nlicencia IN (
            SELECT nlicencia
            FROM Entrenador
            WHERE nombre_entrenador = %s
        );
            """
        cursor = db.cursor()
        cursor.execute(query, (nombre_entrenador,))
        num_jugadores_eliminados = cursor.rowcount
        db.commit()
        cursor.close()
        print(f"Se han eliminado {num_jugadores_eliminados} jugadores del entrenador {nombre_entrenador}.")
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()

    
    db.commit()

def actualizar_jugador(id_jugador, altura, coef_elo,db):
    cursor = db.cursor()
    try:
        query = """
            UPDATE Jugador
            SET altura= %s, coef_elo = %s 
            WHERE id_jugador = %s;
            """
        cursor.execute(query, (altura, coef_elo, id_jugador))
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()
    
    db.commit()

    cursor.close()
    db.close()
    
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
