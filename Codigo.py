import sqlite3
import pandas as pd
import Funciones as fn


#   CONECTA LA BASE DE DATOS
try: 
    conn_data = sqlite3.connect("db_personas.db")
    cursor = conn_data.cursor()
    print("BBDD Cargada con exito")

except sqlite3.Error as error:
    print("Error al conectar BBDD")


# Hace la consulta , Funciona igual que SQL
test = pd.read_sql_query("SELECT * FROM Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol", conn_data)
print(test)
resultado = cursor.fetchall()

for fila in resultado:
    print(fila)


