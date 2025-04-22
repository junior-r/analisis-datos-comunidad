# 📊 Analizando Datos de Salud de una Comunidad

Este proyecto de análisis de datos fue desarrollado como parte de la tenología en Ciencia de Datos. Tiene como objetivo explorar y visualizar información básica de salud recolectada de una comunidad ficticia utilizando Python.

## 🗂️ Descripción del Dataset

El conjunto de datos contiene las siguientes columnas:

- `id`: Identificador único de la persona.
- `edad`: Edad de la persona en años.
- `género`: Género (Masculino o Femenino).
- `fumador`: Indica si la persona es fumadora (Sí o No).

## 🧪 Análisis Realizado

El script realiza los siguientes pasos:

1. Carga de datos desde un archivo CSV.
2. Visualización de las primeras filas.
3. Estadísticas descriptivas de la edad.
4. Identificación y limpieza de valores nulos.
5. Cálculo de edad promedio por género.
6. Conteo de fumadores vs. no fumadores.
7. Visualización de:
   - Histograma de edades.
   - Gráfico de barras de fumadores por género.
8. Conclusiones con observaciones clave.

## 🛠️ Requisitos

Para ejecutar este código, necesitas tener Python 3.12 y las siguientes dependencias. Estas se pueden instalar mediante el archivo `requirements.txt`.

### Crear un entorno virtual

1. **Instalar `virtualenv` (si no lo tienes instalado)**:

   ```bash
   pip install virtualenv
   ```

2. **Crear un entorno virtual con Python 3.12**:

   ```bash
   virtualenv venv --python=3.12
   ```

3. **Activar el entorno virtual**:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

### Instalar las dependencias

Con el entorno virtual activado, instala las dependencias necesarias utilizando `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar el código

Una vez que las dependencias estén instaladas y el entorno virtual esté activado, puedes ejecutar el código directamente desde un script Python o desde un archivo Jupyter Notebook.

1. **Ejecutar desde un archivo Python**:

   El código está guardado en un archivo llamado `analisis_salud_comunidad.py`, simplemente ejecuta:

   - En Windows:

     ```bash
     python analisis_salud_comunidad.py
     ```

   - En macOS/Linux:

     ```bash
     python3 analisis_salud_comunidad.py
     ```

2. **Ejecutar desde un Jupyter Notebook**:

   Si prefieres trabajar en un entorno interactivo, puedes convertir el código a un archivo de Jupyter Notebook (`.ipynb`) y ejecutarlo paso a paso.
