import sqlite3


#   CONECTA LA BASE DE DATOS
try: 
    conn_data = sqlite3.connect("db_personas.db") 
    cursor = conn_data.cursor()

    # Hace la consulta
    # Funciona igual que SQL
    cursor.execute("SELECT * FROM personas")
    resultado = cursor.fetchall()

    for fila in resultado:
        print(fila)

except sqlite3.Error as error:
    print("Error al conectar BBDD")


