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
test = pd.read_sql_query(""" SELECT P.fecha_ingreso AS Fecha, S.Rol, P.residencia, P.rut,
                          P.nombre_completo, P.nacionalidad, P.fecha_de_nacimiento, p.profesion,
                          S.Sueldo FROM Salarios AS S, personas AS P """, conn_data)


print(test)








