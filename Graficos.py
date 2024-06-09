import pandas as pd
import matplotlib.pyplot as plt
import Funciones as fn

start = fn.Conectar_db("db_personas.db")


# Primer grafico 

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
