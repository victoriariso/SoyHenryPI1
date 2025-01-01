# Librerias 
from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# intanciacion de la API
app = FastAPI()
app.title = "Salvo ver películas API"

'''
Esto es un MVP
Modificaciones pendientes:
- Por ahora, si hay mas de una pelicula con el mismo nombre (como Sabrina), devuelve solo los datos de la primera que encuentra 
- Que devuelva un error y no se cuelgue si el titulo de la pelicula, el nombre del actor o del director no estan en el dataset
'''


# Lectura de datasets para cada funcion
df_mes = pd.read_csv('datos/movies_ds_mes.csv')
df_dia = pd.read_csv('datos/movies_ds_dia.csv')
df_score = pd.read_csv('datos/movies_ds_score.csv')
df_votos = pd.read_csv('datos/movies_ds_votos.csv')
df_actors = pd.read_csv('datos/movies_ds_actors ver1.csv')
df_directors = pd.read_csv('datos/movies_ds_directors ver1.csv')
df_movies = pd.read_csv('datos/movies_ds_titles.csv')


# Endpoints

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str): 
 # arg: mes en idioma Español (string)
 # Devuelve: un mensaje indicando la cantidad de películas que se estrenaron en el mes consultado en la totalidad del dataset 

 # El dataset usado tiene las columnas:
 # - id de la película (no necesito el título)
 # - mes de estreno en español (preparado en la notebook transformaciones a partir de la fecha de estreno)
 # Incluye todas las peliculas del dataset movies luego de eliminar los duplicados

 # por si ingresa setiembre sin p lo convierte a septiembre
 if (mes.lower() == 'setiembre'):
    mes = 'septiembre'
 
 # cuenta la cantidad de películas que se estrenaron en el mes consultado. El mes se convierte a minusculas
 qtt_movies_month = df_mes.loc[df_mes['release_month_spa'] == mes.lower(), 'id'].count()

 return {
      "mensaje": f"En el mes de {mes} se estrenaron {qtt_movies_month} películas."  
 }


@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str): 
 # arg: día en idioma Español (string)
 # Devuelve: un mensaje indicando la cantidad de películas que se estrenaron en la totalidad del dataset el dia de la semana consultado  

 # El dataset usado tiene las columnas:
 # - id de la película (no necesito el título)
 # - día de la semana (en idioma español) en que se estrenó la película (preparado en la notebook transformaciones a partir de la fecha de estreno)
 # Incluye todas las peliculas del dataset movies luego de eliminar los duplicados

 # en el dataset los nombres de los días de la semana tienen acento. Por si lo ingresaron sin acento
 if dia.lower() == 'sabado':
    dia = 'sábado'
 elif dia.lower() == 'miercoles':
    dia = 'miércoles'

 # cuenta la cantidad de películas que se estrenaron el dia de la semana consultado 
 qtt_movies_day = df_dia.loc[df_dia['day_week_spa'] == dia.lower(), 'id'].count() 
 
 return {
      "mensaje": f"En día {dia} se estrenaron {qtt_movies_day} películas."  
 }


@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str): 
 # arg: titulo_de_la_filmación (string)
 # Devuelve: un mensaje indicando el título, el año de estreno y el score/popularidad
 
 # Como es un MVP, si hay mas de una pelicula con el mismo nombre (como Sabrina), por ahora devuelve solo los datos de la primera que encuentra 
 # QUEDA PENDIENTE: Ver cómo avisar si la pelicula no esta en el df

 # El dataset usado tiene las columnas:
 # id de la película 
 # title
 # release_year
 # popularity (piden score/popularidad. Es esa columna)

 # Incluye todas las peliculas del dataset movies luego de eliminar los duplicados

 # busca en el dataset la pelicula cuyo titulo se ingresó
 titulo_datos = df_score.loc[df_score['title'].str.lower() == titulo.lower(), ['release_year', 'popularity']]

 # guarda el año y la popularidad de la pelicula elegida para mostrarlo en el mensaje
 # si pongo directamente el valor de la columna titulo_datos['release_year'].values[0], por ejemplo, no funciona
 tit_year = titulo_datos['release_year'].values[0]
 tit_pop = titulo_datos['popularity'].values[0]

 
 return {
      "mensaje": f"La película {titulo} se estrenó en el año {tit_year} con un score/popularidad de {tit_pop}." 
  }


@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str): 
 # arg: titulo_de_la_filmación (string)
 # Devuelve: un mensaje indicando el título, el año de estreno, la cantidad de votos y el valor promedio de las votaciones
 # el año de estreno no esta pedido explicitamente pero esta en el mensaje de ejemplo (lo agrego por las dudas)
 # La cantidad de votos debe ser igual o mayor a 2000 valoraciones. Si no informa que no cumple esta condición y no se devuelve ningun valor.
 
 # Como es un MVP, si hay mas de una pelicula con el mismo nombre (como Sabrina), por ahora devuelve solo los datos de la primera que encuentra 
 # Ver cómo avisar si la pelicula no esta en el df

 # El dataset usado tiene las columnas:
 # -id de la película 
 # -title
 # -release_year,
 # -vote_average,
 # -vote_count

 # Incluye todas las peliculas del dataset movies luego de eliminar los duplicados

 # busca en el dataset la pelicula cuyo titulo se ingresó
  titulo_datos = df_votos.loc[df_votos['title'].str.lower() == titulo.lower(), ['release_year', 'vote_average', 'vote_count']]
  
  # guarda el año de estreno, la cant de votos y el promedio de votos de la pelicula elegida para mostrarlo en el mensaje
  # si pongo directamente el valor de la columna titulo_datos['release_year'].values[0], por ejemplo, no funciona
  tit_year = titulo_datos['release_year'].values[0]
  tit_vote_count = titulo_datos['vote_count'].values[0]
  tit_vote_avg = titulo_datos['vote_average'].values[0]

  msg = {
      "mensaje": f"La película {titulo} se estrenó en el año {tit_year}. La misma cuenta con un total de {tit_vote_count} valoraciones, con un promedio de {tit_vote_avg}." 
  }

  # Si la cantidad de votos es menor a 2000 valoraciones informa que no cumple esta condición y no se devuelve ningun valor
  if tit_vote_count < 2000:
    msg = {
      "mensaje": f"La película {titulo} tiene menos de 2000 valoraciones. No se devuelve ningun valor." 
  }
  
  return msg


@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor: str): 
 # arg: nombre_actor (string)
 # Devuelve: un mensaje indicando la cantidad y la suma del retorno de todas las películas en las que participó y 
 # el promedio de retorno por película. 
 # Si un actor fue también director en alguna película el mensaje solo indica eso y no da mas datos

 # El dataset usado tiene las columnas:
 # - id de la película 
 # - id del actor (campos id de la columna cast de la tabla credits) 
 # - nombre del actor (campos name de la columna cast de la tabla credits)
 # - título de cada pelicula en la que participó
 # - return de cada pelicula en la que participó
 #  - es_director (columna bool (True/False) indicando los actores que tambien son directores porque hay que informar eso y no mostrar sus datos)

 # como hay una fila por pelicula y actor para que el dataset no fuera tan grande 
 # elegi un dataset reducido de 20 actores conocidos de los cuales 9 son tambien directores
 # Si eso funciona bien, mas adelante agregare mas actores
 # actors_selected = ['Brad Pitt', 'Clint Eastwood', 'Denzel Washington', 'Emma Stone', 'Emma Thompson', 'Emma Watson', 'Harrison Ford', 'Jessica Lange', 
 #                  'Jodie Foster', 'Johnny Depp', 'Keanu Reeves', 'Leonardo DiCaprio', 'Meryl Streep', 'Robert Redford', 'Sally Field', 'Sandra Bullock', 
 #                   'Tom Cruise', 'Tom Hanks', 'Will Smith', 'Woody Allen']
 
 # guardo en minusculas el nombre del actor ingresado por si ingresa mezcla de mayusculas y minusculas
  actor_low = nombre_actor.lower()

 # consulto si el actor es tambien director en alguna pelicula 
 # df_actors.loc['is_director'].values[0] sera True
  actor_director  = df_actors.loc[df_actors['actor_name'].str.lower() == actor_low, 'is_director'].values[0]

  # si fue director en alguna pelicula aviso y no muestra los datos
  if actor_director:
    msg = {
      "mensaje": f"El actor {nombre_actor} fue también director de alguna película - No se muestran datos." 
  }
    
  else:
    
    # arma un dataset reducido solo con las peliculas en la que participo el actor elegido
    movies_ds_one_actor = df_actors.loc[df_actors['actor_name'].str.lower() == actor_low]

    # sumo el retorno de las peliculas en las que actuó, cuento la cantidad de peliculas en las que actuó y calculo el promedio del retorno
    ret_sum =  movies_ds_one_actor['return'].sum() 
    ret_count = movies_ds_one_actor['return'].count() 
    ret_avg = ret_sum / ret_count

    msg = {
       "mensaje": f"El actor {nombre_actor} ha participado de {ret_count} películas, consiguió un retorno de {ret_sum} con un promedio de {ret_avg} por película." 
    }
    
  return msg


@app.get('/get_director/{nombre_director}')
def get_director( nombre_director: str): 
 # arg: nombre_director (string)
 # Devuelve: un mensaje indicando la suma del retorno de todas las películas en las que participó y 
 # el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma (si logro hacerlo)

 # El dataset usado tiene las columnas:
 # - id de la película 
 # - id del director (id de la columna crew de la tabla credits donde 'job': 'Director')
 # - nombre del director (name de la columna crew de la tabla credits donde 'job': 'Director') 
 # - title
 # - release_date
 # - budget
 # - revenue
 # - return
 
 # como hay una fila por pelicula y director para que el dataset no fuera tan grande 
 # elegi un dataset reducido de directores conocidos (al menos por mi)
 # directors_selected = ['Francis Ford Coppola', 'James Cameron', 'Joel Coen', 'Martin Scorsese', 'Quentin Tarantino', 'Stanley Kubrick', 
 #                     'Steven Spielberg', 'Wes Anderson', 'Woody Allen', 'Clint Eastwood', 'Sofia Coppola', 'Natalie Portman', 
 #                     'Jodie Foster', 'Martin Scorsese', 'Alfred Hitchcock', 'Greta Gerwig', 'Niki Caro']

 # busca las peliculas de ese director solo una vez y arma un nuevo dataset con eso 
 df_one_dir = df_directors.loc[df_directors['director_name'].str.lower() == nombre_director.lower()]

 # selecciono las columnas que hay que mostrar
 movies_ds = df_one_dir[['title', 'release_date', 'budget', 'revenue', 'return']].copy()

 # suma el retorno de las peliculas que dirigio el director seleccionado
 ret_sum = df_one_dir['return'].sum() 

 msg = {'El director': nombre_director,
       'consiguió un retorno de': ret_sum,
       'Participó en las películas': movies_ds.to_dict(orient="records")
 }

 return msg


@app.get('/recomendacion/{titulo}')
def recomendacion( titulo: str): 
 
 # arg: titulo de una pelicula conocida o inventada (string)
 # Devuelve: una lista de las 5 peliculas mas parecida de acuerdo al nombre del titulo ingresado

 # El dataset usado tiene la columna:
 # - title
 
 # selecciono las peliculas de idioma original ingles, de 1980 a 1985. solo el titulo
 # Son 1486 peliculas. 
 # Si esto funciona bien (alcanza la memoria y no es muy lento) ofrecerá tambien peliculas de otros años o en otros idiomas
 # siempre con el titulo en ingles

  # con mucha ayuda de google y chapGPT
 # Inicializo TfidfVectorizer
 vectorizer = TfidfVectorizer()

 # Fit y transformación de los titulos de las peliculas
 tfidf_matrix = vectorizer.fit_transform(df_movies['title'])

 # convierte en una lista el titulo ingresado 
 s_tit = [titulo]

 # vectoriza s_tit
 s_tit_tfidf = vectorizer.transform(s_tit)

 # Calcula la similitud del coseno entre el titulo de que ingreso y los titulos de las peliculas del dataset 
 cosine_sim = cosine_similarity(s_tit_tfidf, tfidf_matrix)

 # une los títulos de las películas con sus valores de similitud de coseno correspondientes
 # (con mucha ayuda de google y chatGPT)
 result = []

 for i in range(len(df_movies)):  # itera por todas las filas de la serie de titulos de peliculas
        similarity_value = cosine_sim[0][i]
        result.append({
           # accede a cada elemento de la serie y de la matriz
            'Title': df_movies['title'].iloc[i],
            'Cos_Sim': similarity_value
        })

 # Convierte el resultado en un df
 result_df = pd.DataFrame(result)

 # ordena los valores de similitud en orden ascendente
 final_df = result_df.sort_values(by=['Cos_Sim'], ascending=False)

 # selecciona los 5 valores mas similares y los convierte para poder mostrar (correccion sugerida por chatGPT)
 # lista = final_df.head(5).values.tolist()
 lista = final_df.head(5).to_dict(orient='records') 
 
 msg = {'Las 5 peliculas cuyo titulo es mas similar a': titulo,
       'son': lista
 }

 return msg