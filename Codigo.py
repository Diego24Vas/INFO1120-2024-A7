import sqlite3
import pandas as pd
import docx
import Funciones as fn
from Funciones import example_contract
import matplotlib.pyplot as plt

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

db = "db_personas.db"
start = fn.Conectar_db(db)
personas = fn.Conectar_P(db)

# Consulta cantidad de filas
con_cant = start.execute("SELECT COUNT(*) as cantidad FROM personas")
con_cant = con_cant.fetchone()
con_cant = con_cant[0]

# Consulta al usuario
while True:
    try:
        inicio = int(input("Ingrese el primer numero de fila: "))
        final = int(input("Ingrese el ultimo numero de fila: "))
        
        if inicio > final:  
            print("El primer número debe ser menor o igual al último.")
            continue
        elif inicio > con_cant:
            print("El primer rango esta fuera de limite")
            continue
        elif final > con_cant:
            print("El segundo rango esta fuera de limite")
            continue
        break
    except (ValueError, IndexError, TypeError):
        print("Caracter ingresado no valido")


def multiple_data_to_contract(registro):
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
    multiple_data_to_contract(registro_actual)

#Graficos
print("Graficos")

print("Consulta 1")
# Hace la consulta, Funciona igual que SQL
con_rol = pd.read_sql_query("SELECT Rol FROM Salarios", start)
con_sld = pd.read_sql_query("SELECT Sueldo FROM Salarios", start)

# Combina datos
data = pd.DataFrame({
    "Rol"   : con_rol["Rol"],
    "Sueldo": con_sld["Sueldo"]
})

# Calcular el sueldo promedio por rol
prom_sld = data.groupby("Rol")["Sueldo"].mean().reset_index()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(prom_sld["Rol"], prom_sld["Sueldo"], color="skyblue", edgecolor="black")

# Añadir títulos y etiquetas
plt.title("Sueldo Promedio ", fontsize=16)
plt.xlabel("Profesion", fontsize=14)
plt.ylabel("Sueldo Promedio", fontsize=14)


# Mostrar el gráfico
plt.tight_layout()
plt.savefig("img_graficos/Grafico_sueldos.png")  # Guarda el gráfico como una imagen


#...................................................................................................


# Segundo Grafico 
dtb_prf = pd.read_sql_query("SELECT profesion FROM personas", start)

cont_prf = dtb_prf["profesion"].value_counts().reset_index()
cont_prf.columns = ['profesion', 'cantidad']

# Crear el gráfico de tarta
plt.figure(figsize=(8, 8))
plt.pie(cont_prf["cantidad"], labels=cont_prf["profesion"], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

# Añadir título
plt.title("Distribución de Profesiones", fontsize=16)

# Mostrar el gráfico
plt.tight_layout()
plt.savefig("img_graficos/distribucion_grafico_tarta.png")
plt.show()


#.....................................................................................................

# Tercer grafico

ncd = pd.read_sql_query("SELECT nacionalidad FROM personas", start)

# Contar la cantidad de ocurrencias de cada nacionalidad
conteo_nacionalidades = ncd['nacionalidad'].value_counts().reset_index()
conteo_nacionalidades.columns = ['nacionalidad', 'cantidad']

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(conteo_nacionalidades['nacionalidad'], conteo_nacionalidades['cantidad'], color='skyblue', edgecolor='black')

# Añadir títulos y etiquetas
plt.title("Cantidad de Personas por Nacionalidad", fontsize=16)
plt.xlabel("Nacionalidad", fontsize=14)
plt.ylabel("Cantidad de Personas", fontsize=14)

# Rotar las etiquetas del eje X
plt.xticks(rotation=45, ha="right", fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.savefig("img_graficos/grafico_nacionalidad.png")
plt.show()