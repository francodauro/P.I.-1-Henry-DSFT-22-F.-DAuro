#Importar librerías

from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi.responses import HTMLResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# URL del archivo CSV en GitHub (reemplaza con la URL correcta)
csv_url = 'df_api_playtimegenre.csv'
ml_csv_url = 'ML_df.csv'

# Leer el archivo CSV para PlayTimeGenre
try:
    df = pd.read_csv(csv_url, dtype={'genre': str, 'playtime_forever': np.int32, 'release_year': np.int32})
except Exception as e:
    print(f"No se pudo cargar los datos para la función PlayTimeGenre: {e}")

# Leer el archivo CSV para get_recommendations
try:
    df_ML = pd.read_csv(ml_csv_url, dtype={'id': str, 'app_name': str, 'tags': str, 'specs': str, 'genres': str})
   
except Exception as e:
    print(f"No se pudo cargar los datos para la función get_recommendations: {e}")

# Definir funcion bienvenida

@app.get("/", response_class=HTMLResponse)
def read_root():
    message = (
        "<h1>¡Bienvenido a la API de Videojuegos!</h1>"
        "<p>Esta API proporciona dos funciones: 1- 'PlayTimeGenre' y 2- 'get_recommendations'. </p>"
        "<p>PlayTimeGenre calcula en qué año se lanzaron los videojuegos cuyo género acumuló la mayor cantidad de horas de juego.</p>"
        "<p>get_recommendations recomienda los 5 videojuegos más similares al elegido por el usuario.</p>"
    )
    return message

# Definir funcion PlayTimeGenre

@app.get("/PlayTimeGenre")
def play_time_genre(genre: str):
    # Filtrar el dataframe por el género especificado
    filtered_df = df[df['genre'] == genre]

    if filtered_df.empty:
        return {"error": f"No se encontraron datos para el género '{genre}'"}

    # Calcular el año con la mayor suma de horas de juego
    result = filtered_df.groupby('release_year')['playtime_forever'].sum().idxmax()
    release_year = int(result)

    message = f"El año de lanzamiento para el género '{genre}' con más horas jugadas es {release_year}"
    return {"message": message}

@app.get("/get_recommendations")
def get_recommendations(game_id: str):
    # Obtener el índice del juego dado por su id
    try:
        idx = df_ML[df_ML['id'] == game_id].index[0]
    except IndexError:
        return {"error": "El id del juego no se encuentra en el dataset."}
    
    # Combinar todas las características en un solo texto
    df_ML['combined_features'] = df_ML['tags'] + ' ' + df_ML['specs'] + ' ' + df_ML['genres']

    # Vectorización
    vectorizer = CountVectorizer().fit_transform(df_ML['combined_features'])
    vectors = vectorizer.toarray()

    # Calcular la Similitud del Coseno:
    cosine_sim = cosine_similarity(vectors)

    # Obtener las puntuaciones de similitud del juego dado con todos los otros juegos
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Ordenar los juegos por puntuación de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Obtener los índices de los 5 juegos más similares
    sim_scores = sim_scores[1:6]
    game_indices = [i[0] for i in sim_scores]
    
    # Devolver los nombres de los 5 juegos más similares
    recommendations = df_ML[['id', 'app_name']].iloc[game_indices].to_dict(orient='records')
    return {"recommendations": recommendations}