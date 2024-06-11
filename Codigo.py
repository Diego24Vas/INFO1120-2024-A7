import sqlite3
import pandas as pd
import docx
import Funciones as fn
from Funciones import example_contract
from word_gen import example_contract

#Todas las secciones del codigo deberian funcionar por separado importando los repositorios de arriba

start = fn.Conectar_db("db_personas.db")

#               Ejercicio N°1
print("Consulta 1")
# Hace la consulta , Funciona igual que SQL
N1 = pd.read_sql_query("SELECT * FROM Salarios INNER JOIN personas ON Salarios.id_salarios = personas.id_rol", start)
print(N1)

#Consulta N°2
print("Consulta 2")
db = "db_personas.db"
do = fn.Conectar_P(db) 
print(do)

#Consulta N°3 y 4

print("Consulta 3 y 4")
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
        #Datos egresados, solo como comprobacion
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

#Consulta 5
print("consulta 5")

