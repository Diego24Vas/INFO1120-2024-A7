# Crear aqui las funciones para mas adelnte
import sqlite3
import pandas as pd
#from docx import Document


# Inicia la base de datos
def Conectar_db (db_personas):
    conn = sqlite3.connect(db_personas)
    return conn

# Conecta la base de datos a la Tabla Personas
def Conectar_P(db_personas):
    conn = sqlite3.connect(db_personas)
    con = "SELECT rut, nombre_completo FROM personas"  #Define la tabla Personas como lectura (con = consulta)
    df = pd.read_sql_query(con, conn)
    conn.close()
    return df