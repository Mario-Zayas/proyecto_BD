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
    with db.cursor() as cursor:
    
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
    with db.cursor() as cursor:
    
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
    nombre_entrenador = input("Introduce el nombre del entrenador: ")
    with db.cursor() as cursor:
     try:
        query = """
            SELECT Entrenador.nlicencia, Entrenador.nombre_entrenador, Entrenador.email,
                   Jugador.nlicencia, Jugador.id_jugador,
                   Jugador.posicion_ant_camp, Jugador.coef_elo, Jugador.altura
            FROM Entrenador 
            JOIN Jugador ON Entrenador.nlicencia = Jugador.nlicencia
            WHERE Entrenador.nombre_entrenador = %s;
            """
        cursor.execute(query, (nombre_entrenador,))
        for (nlicencia_entrenador, nombre_entrenador, email_entrenador, 
             nlicencia_jugador,
             id_jugador, posicion_ant_camp, coef_elo, altura) in cursor:
            print("Entrenador: ", nlicencia_entrenador, nombre_entrenador, email_entrenador)
            print("Jugador: ", nlicencia_jugador, 
                  id_jugador, posicion_ant_camp, coef_elo, altura)
     except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cursor.close()
        db.close()
        exit()




    

def insertar_jugador(jugadores,db):
    
    with db.cursor() as cursor:
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

def eliminar_jugadores_entrenador(nombre_entrenador, db):

    with db.cursor() as cursor:
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
    with db.cursor() as cursor:
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
    print("1. Listar jugadores")
    print("2. Buscar jugadores por entrenador")
    print("3. Mostrar entrenador y sus jugadores")
    print("4. Insertar jugador")
    print("5. Eliminar jugadores de un entrenador")
    print("6. Actualizar jugador")
    print("7. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion
