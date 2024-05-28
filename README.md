# P.I.-1-Henry-DSFT-22-F.-DAuro
### Proyecto Individual 1. Henry Data Science Full Time 22. Franco D'Auro. Repositorio API

En el presente repositorio se presentan los archivos de un MVP (Minimum Viable Product). Este MVP consiste en la construcción de una API (Application Programming Interface) capaz de consultar y procesar información sobre videojuegos.
La API tiene dos funciones que se detallarán debajo:
- PlayTimeGenre: Retorna el año de lanzamiento de los videojuegos de un género elegido por el usuario que mayor cantidad de horas de juego han acumulado. Su argumento o endpoint es el género del juego escrito como String. Funciona con los datos disponibles en el archivo df_api_playtimegenre.csv.
- get_recommendations: Devuelve una lista de 5 videojuegos recomendados para un juego elegido por el usuario. Su endpoint es la ID (Número entero) del juego elegido. Funciona con los datos disponibles en el archivo ML_df.csv.
La API fue construida con el framework FastAPI y desplegada de manera online utilizando el servicio de la plataforma Render. Utilizando el siguiente link se puede desplejar la api:

https://p-i-1-henry-dsft-22-f-dauro-12.onrender.com/

Los archivos ML_df.csv y df_api_playtime.csv fueron obtenidos mediante procesamiento local de los datasets originales.

A continuación se presentan los archivos originales y los scripts desarrollados de manera local con su nombre y su función:
- australian_user_reviews.json: Archivo original con revisiones sobre videojuegos. 
- australian_user_items.json: Archivo original con características de videojuegos adquiridos por distintos usuarios. Cada item es un videojuego.
- output_steam_games.json: Archivo original con características de los videojuegos y sus fabricantes.
- ETL.ipynb: Notebook de Python en el que se cargó, reparó y transformó cada uno de los archivos JSON originales descriptos previamente. Además se realizó un análisis de sentimientos en el archivo de reviews para identificar la valoración subjetiva de cada revisión. Este notebook crea 3 archivos JSON (Games_corregido.json, Items_corregido.json y Reviews_corregido.json) y otros 4 CSV (Games_corregidos.csv, Items_corregidos.csv, Reviews_corregido.csv y Reviews_corregidas_con_sentimiento.csv) formateados correctamente.
- df_api_PlayTimeGenre.ipynb: Notebook de Python en el que se cargó y optimizó la información disponible en los archivos Games_corregidos.csv e Items_corregidos.csv. Este notebook crea un archivo llamado df_api_playtimegenre.csv que contiene sólo un 10% de la información disponible originalmente por motivo de peso del archivo. Este archivo CSV es la base de datos que usa la funcion de la api llamada PlayTimeGenre.
- EDA_y_ML.ipynb: Notebook de Python en el que se cargó y procesó la información disponible en los archivos Games_corregidos.csv, Items_corregidos.csv y Reviews_corregidas_con_sentimiento para organizarla en un único dataframe al que se le realizó un EDA (Exploratory Data Analysis). Este dataframe fue optimizado y guardado con el nombre ML_df.csv para luego realizar para realizar un sistema de recomendación item-item. El modelo de recomendación se realizó utilizando Similitud del Coseno. El archivo ML_df.csv se usó como base de datos de la funcion de la api llamada get_recommendations.

A continuación se encuentra el link a un carpeta pública de Google Drive en el que se encuentran los archivos necesarios para realizar los procedimientos de manera local:

https://drive.google.com/drive/folders/1Nad8TmHsK9HcfGWZtHhq8gkXpJ_DFZe0?usp=sharing

    

