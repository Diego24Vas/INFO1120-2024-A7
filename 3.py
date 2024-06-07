import sqlite3
import pandas as pd
import docx
import Funciones as fn
from word_gen import example_contract

dato = (input("Ingresa el rut del usuario: "))

doc =  docx.Document()
start = fn.Conectar_P("db_personas.db")

def singular_data_to_contract(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['fecha']
    rol = sub_df['rol']
    address = sub_df['residencia']
    rut = sub_df['rut']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha de nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))


def contrato_empleador(db_personas, employee_id):
    df = start
    print(df)
    try:
        index_row = df[df['rut'] == employee_id].index[0]
        print(f"Empleado encontrado: {employee_id}, en la fila: {index_row}")
    except IndexError:
        print(f"Empleado con rut {employee_id} no encontrado.")
        return
    
if __name__ == "__main__":
    db = "db_personas.db"
    employee_id = dato 
    contrato_empleador(db, employee_id)




