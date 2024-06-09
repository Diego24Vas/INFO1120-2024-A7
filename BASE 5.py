import sqlite3
import pandas as pd
import docx
import Funciones as fn
from word_gen import example_contract



def singular_data_to_contract(sub_df):
    try:
        index_row = sub_df.name
        print("Ya se creo el archivo")
        date = sub_df['fecha_ingreso']
        rol = sub_df['Rol']
        address = sub_df['residencia']
        rut = sub_df['rut']
        full_name = sub_df['nombre_completo']
        nationality = sub_df['nacionalidad']
        birth_date = sub_df['fecha_de_nacimiento']
        profession = sub_df['profesion']
        salary = sub_df['Sueldo']
        #Datos egresados, solo como comprobacion
        print(f"Empleado encontrado: {rut}, en la fila: {index_row}")
        print("Datos del empleado:")
        print(f"Fecha: {sub_df['fecha_ingreso']}")
        print(f"Rol: {sub_df['Rol']}")
        print(f"Residencia: {sub_df['residencia']}")
        print(f"RUT: {sub_df['rut']}")
        print(f"Nombre Completo: {sub_df['nombre_completo']}")
        print(f"Nacionalidad: {sub_df['nacionalidad']}")
        print(f"Fecha de Nacimiento: {sub_df['fecha_de_nacimiento']}")
        print(f"Profesión: {sub_df['profesion']}")
        print(f"Sueldo: {sub_df['Sueldo']}")    
        example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
    except IndexError:
        print(f"Empleado con rut {rut} no encontrado.")
        return    
    


# Funcion que llama los datos
def range_usu(ini_rut, fin_rut):
    try: 
        conn = fn.Conectar_db("db_personas.db")
        cons = f""" SELECT * FROM personas 
                    NATURAL JOIN Salarios 
                    WHERE rut BETWEEN {ini_rut} AND {fin_rut}"""
        df = pd.read_sql_query(cons, conn)

        # Comprueba si df esta vacio, si no genera los contratos
        if df.empty:   
            print("No se encontraron empleados en el rango especificado.")
        else:
            for index, row in df.iterrows():
                singular_data_to_contract(row)
        return df
        
    except Exception as e:
        print(f"Error al conectar a la base de datos o al procesar datos: {e}")

# Consulta al usuario
while True:
    try:
        ini_rut = int(input("Ingresa el RUT inicial del rango (sin dígito verificador): "))
        fin_rut = int(input("Ingresa el RUT final del rango (sin dígito verificador): "))
        break
    except ValueError:
        print("Error: Ingresa un número válido para el RUT.")
    
range_usu(ini_rut, fin_rut)
