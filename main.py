# Librerias 
from fastapi import FastAPI
import numpy as np
import pandas as pd

# intanciacion de la API
app = FastAPI()
app.title = "Salvo ver películas API"

'''
Esto es un MVP
Modificaciones pendientes:
- Version 1: que el mes y el dia puedan ingresarse en mayuscula o minuscula. Convertir a minuscula y buscarlo asi
Para eso tengo que actualizar columnas y guardar los datos en minuscula
- Version 2: ingresar mes o dia de la semana en letras, convertirlo a numero y buscar como numero. ¿sera mas rapido?
Guardar el valor ingresado para que en el mensaje de return aparezca exactamente igual a cómo lo ingresó el usuario
- Tener en cuenta que pueden escribir setiembre o septiembre, miercoles o miércoles y sabado o sábado
'''


# Lectura de datasets para cada funcion
df_mes = pd.read_csv('datos/movies_ds_mes.csv')
df_dia = pd.read_csv('datos/movies_ds_dia.csv')


# Endpoints

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str): 
 # arg: mes en idioma Español (string)
 # Devuelve: cantidad de películas que se estranron en el mes consultado en la totalidad del dataset 

 qtt_movies_month = df_mes.loc[df_mes['release_month_spa'] == mes, 'id'].count()

 return {
      "mensaje": f"En el mes de {mes} se estrenaron {qtt_movies_month} películas."  
 }

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str): 
 # arg: día en idioma Español (string)
 # Devuelve: la cantidad de películas que se estrenaron en la totalidad del dataset el dia de la semana consultado  

 qtt_movies_day = (df_dia['day_week_spa'].values == dia).sum()

 return {
      "mensaje": f"En día {dia} se estrenaron {qtt_movies_day} películas."  
 }
