import sqlite3
import pandas as pd
import docx
import Funciones as fn
from word_gen import example_contract



db = "db_personas.db"
start = fn.Conectar_db(db)
personas = fn.Conectar_P(db)



# Consulta al usuario
while True:
    try:
        inicio = int(input("Ingrese el primer numero de fila: "))
        final = int(input("Ingrese el ultimo numero de fila: "))
        
        if inicio > final:
            print("Error: El primer número de fila debe ser menor o igual al último.")
            continue
        break
    except ValueError:
        print("Caracter ingresado no valido")


def singular_data_to_contract(registro):
        date = registro['fecha_ingreso']
        rol = registro['Rol']
        address = registro['residencia']
        rut = registro['rut']
        full_name = registro['nombre_completo']
        nationality = registro['nacionalidad']
        birth_date = registro['fecha_de_nacimiento']
        profession = registro['profesion']
        salary = registro['Sueldo']
        #Datos egresados, solo como comprobacio  
        example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))


for i in range(inicio, final):
    registro_actual = personas.iloc[i]
    singular_data_to_contract(registro_actual)