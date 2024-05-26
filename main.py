
from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi.responses import HTMLResponse


app = FastAPI()

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/francodauro/P.I.-1-Henry-DSFT-22-F.-DAuro/main/dataframe_api.csv'

# Leer el archivo CSV
try:
    df = pd.read_csv(csv_url, dtype={'genre': str, 'playtime_forever': np.int32, 'release_year': np.int32})
except Exception as e:
    print(f"No se pudo cargar los datos: {e}")


@app.get("/", response_class=HTMLResponse)
def read_root():
    # Obtener una lista de todos los géneros disponibles
    genres_available = df['genre'].unique()

    # URL base para la función PlayTimeGenre
    base_url = "http://127.0.0.1:8000/PlayTimeGenre?genre="  # Cambia esta URL por la URL de tu API en producción

    # Mensaje de bienvenida
    message = (
        "<h1>¡Bienvenido a la API de Videojuegos!</h1>"
        "<p>Esta API proporciona una función llamada 'PlayTimeGenre', "
        "la cual calcula en qué año se lanzaron los videojuegos cuyo género acumuló la mayor cantidad de horas de juego.</p>"
        "<h2>A continuación se ofrece la lista de los géneros diponibles con sus URL de consulta:</h2>"
    )

    # Agregar lista de géneros disponibles al mensaje
    for genre in genres_available:
        # Construir la URL completa para el género actual
        genre_url = base_url + genre
        # Agregar el género y la URL al mensaje
        message += f"<p>- {genre}: <a href='{genre_url}'>{genre_url}</a></p>"

    return message

@app.get("/PlayTimeGenre")
def play_time_genre(genre):
    # Filtrar el dataframe por el género especificado
    filtered_df = df[df['genre'] == genre]

    if filtered_df.empty:
        return {"error": f"No se encontraron datos para el género '{genre}'"}

    # Calcular el año con la mayor suma de horas de juego
    result = filtered_df.groupby('release_year')['playtime_forever'].sum().idxmax()

    # Obtener el año correspondiente al resultado
    release_year = int(result)

    # Construir la frase estética
    message = f"El año de lanzamiento para el género '{genre}' con más horas jugadas es {release_year}"

    return {"message": message}
