# Crear aqui las funciones para mas adelnte
import sqlite3
#from docx import Document


# Inicia la base de datos
def Conectar_db (db_personas):
    conn = sqlite3.connect(db_personas)
    return conn