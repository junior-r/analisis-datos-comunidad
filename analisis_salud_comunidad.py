# Proyecto: Analizando Datos de Salud de una Comunidad
# Autor: Wilfred Junior Ruiz Navas
# Descripción: Este script realiza un análisis básico de datos de salud de una comunidad.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV utilizando pandas
df = pd.read_csv("datos_salud_comunidad.csv")

# 2. Mostrar las primeras 5 filas del conjunto de datos
print("Primeras 5 filas del dataset:")
print(df.head())

# 3. Describir estadísticamente la columna de edad
print("\nEstadísticas de la columna 'edad':")
print(df['edad'].describe())

# 4. Identificar si hay valores nulos y eliminarlos si existen
print("\nValores nulos en cada columna:")
print(df.isnull().sum())

df = df.dropna()  # Elimina filas con cualquier valor nulo

# 5. Calcular la edad promedio por género
print("\nEdad promedio por género:")
print(df.groupby('género')['edad'].mean())

# 6. Contar cuántas personas fuman y cuántas no
print("\nConteo de personas fumadoras y no fumadoras:")
print(df['fumador'].value_counts())

# 7. Graficar un histograma de las edades
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=15, color='skyblue', edgecolor='black')
plt.title('Histograma de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout()
plt.savefig("histograma_edades.png")
plt.show()

# 8. Graficar un gráfico de barras de fumadores por género
plt.figure(figsize=(8, 5))
fumadores_por_genero = df[df['fumador'] == 'Sí']['género'].value_counts()
fumadores_por_genero.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Cantidad de Fumadores por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Fumadores')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("fumadores_por_genero.png")
plt.show()

# 9. Observaciones importantes
print("\nObservaciones:")
print("1. La mayoría de las personas en el conjunto de datos tienen entre 20 y 60 años.")
print("2. Hay una mayor proporción de no fumadores, y los fumadores se distribuyen de forma relativamente equitativa entre géneros.")
