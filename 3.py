import sqlite3
import pandas as pd
import docx
import Funciones as fn
from word_gen import example_contract


while True:
    try:
        Nums = int(input("Ingresa el rut del usuario (Sin digito Verificador): "))
        strNum = str(Nums)
        Dat = input("Ingresa el digito Verificador: ")
        UDat = Dat.upper()
        print(UDat)
        SumDat = strNum + "-" + UDat
        print(SumDat)
        break

    except ValueError:
        print("Error: Ingresa un número válido para el RUT.")
    except NameError:
        print("Error: Se ha producido un error de nombre")

def singular_data_to_contract(df, employee_id):
    try:
        index_row = df[df["rut"] == employee_id].index[0]
        sub_df = df.iloc[index_row]
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
        print(f"Empleado encontrado: {employee_id}, en la fila: {index_row}")
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
        print(f"Empleado con rut {employee_id} no encontrado.")
        return    
    
db = "db_personas.db"
start = fn.Conectar_P(db) 
employee_id = SumDat #Asigna Employee_Id como confirmacion de RUT
singular_data_to_contract(start, employee_id)

