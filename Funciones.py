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
    con = """ SELECT P.fecha_ingreso AS Fecha, S.Rol, P.residencia, P.rut,
                          P.nombre_completo, P.nacionalidad, P.fecha_de_nacimiento, p.profesion,
                          S.Sueldo FROM Salarios AS S, personas AS P """  #Define la tabla Personas como lectura (con = consulta)
    df = pd.read_sql_query(con, conn)
    conn.close()
    return df