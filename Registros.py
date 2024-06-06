import sqlite3
import pandas as pd
import Funciones as fn

#   CONECTA LA BASE DE DATOS
start = fn.Conectar_db("db_personas.db")

# Hace la consulta , Funciona igual que SQL
test = pd.read_sql_query(""" SELECT P.fecha_ingreso AS Fecha, S.Rol, P.residencia, P.rut,
                          P.nombre_completo, P.nacionalidad, P.fecha_de_nacimiento, p.profesion,
                          S.Sueldo FROM Salarios AS S, personas AS P """, start)


print(test)
print("HOLA")







