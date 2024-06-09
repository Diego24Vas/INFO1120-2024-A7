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
plt.savefig('img_graficos/Grafico_sueldos.png')  # Guarda el gráfico como una imagen

