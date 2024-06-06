import sqlite3
import pandas as pd
import Funciones as fn


start = fn.Conectar_db("db_personas.db")


#               Ejercicio N°1

# Hace la consulta , Funciona igual que SQL
test = pd.read_sql_query("SELECT * FROM Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol", start)
print(test)