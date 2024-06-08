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


def contrato_empleador(df, employee_id):
    try:
        index_row = df[df['rut'] == employee_id].index[0]
        print(f"Empleado encontrado: {employee_id}, en la fila: {index_row}")
    except IndexError:
        print(f"Empleado con rut {employee_id} no encontrado.")
        return
    
if __name__ == "__main__":
    db = "db_personas.db"
    start = fn.Conectar_P(db) 
    employee_id = SumDat 
    contrato_empleador(start, employee_id)

  git config --global user.email "dvasquez2024@alu.uct.cl"
  git config --global user.name "Diego24Vas"



