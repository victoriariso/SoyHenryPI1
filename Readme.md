# <h1 align=center> **Victoria RISO** </h1>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Read.Me`**</h1>

# <h1 align=center>**`Solo ver películas API`**</h1>

<hr>  

## **Descripción**

Este proyecto desarrolla una API que provee un sistema para recomendar películas por similitud con el título ingresado y otros endpoints que ofrecen datos acerca de las películas, los actores y los directores de los datasets provistos.

## **Instalación y Requisitos**

## Requisitos:
•	Python 3.7 o superior</br>
•	pandas</br>
•	numpy</br>
•	fastapi (FastAPI)</br>
•	scikit-learn (TfidfVectorizer y cosine_similarity)</br>
•	uvicorn</br>

## Instalación y ejecución de la API de manera local:
1.	Clonar el repositorio:</br> git clone https://github.com/victoriariso/SoyHenryPI1.git
2.	Crear un entorno virtual:</br> python -m venv venv
3.	Activar el entorno virtual:</br>
	Windows: venv\Scripts\activate
4.	Instalar las dependencias:</br> pip install -r requirements.txt
</br>
    El archivo de requirements.txt usado debe contener las siguientes líneas:
     </br>pandas
     </br>numpy
     </br>fastapi
     </br>scikit-learn
     </br>uvicorn
5.  Iniciar el servidor FastAPI:</br>
    uvicorn main:app --reload
6.  Acceder a la API local en el link:</br>
    http://127.0.0.1:8000/docs

## Ejecución de la API en Render:
https://soyhenrypi1-k3io.onrender.com/docs

## **Estructura del Proyecto**
•	data/: Contiene los archivos de datos usados en cada uno de los endpoints.</br>
•	notebooks/: Contiene tres Jupyter notebooks:</br> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Desarrollo de funciones (las que aparecen en cada uno de los endpoints).</br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EDA (con el Análisis exploratorio de los datos).</br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transformaciones (las realizadas para obtener los datos que consultan los endpoints).</br>
•	README.md: Documentación. (el archivo que estás leyendo ahora)</br>
•	main.py (archivo en Python con la últimq versión de la API)</br>
•	main sin exception.py (archivo en Python con una versión anterior de la API )</br>
•	requirements.txt (archivo con las librerías necesarias para correr la API, mencionado en los Pasos de instalación)</br>


## **Uso de la API / endpoints**
  
+  **cantidad_filmaciones_mes( *`Mes`* )**:
    Se ingresa un mes en idioma español. Devuelve la cantidad de películas que fueron estrenadas en ese mes. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo:  Ingreso: `junio` - Mensaje de salida: En el mes de `junio` se estrenaron `3151` películas. </br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función consulta todas las películas del dataset provisto. El nombre de los meses puede ingresarse en mayúscula o minúscula. Septiembre puede ingresarse también escrito 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;como setiembre (sin p).  
         

+  **cantidad_filmaciones_dia( *`Dia`* )**:
    Se ingresa un día de la semana en idioma español. Devuelve la cantidad de películas que fueron estrenadas ese día.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo:  Ingreso: `domingo` - Mensaje de salida: En día `domingo` se estrenaron `3608` películas </br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función consulta todas las películas del dataset provisto. El nombre de los días puede ingresarse en mayúscula o minúscula. Los días miércoles y sábado pueden ingresarse con 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o sin acento.  

+  **score_titulo( *`titulo_película`* )**:
    Se ingresa el título de una película. Devuelve el mismo título, el año de estreno y el score/popularidad.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo Ingreso: `Sense and Sensibility` - Mensaje de salida: La película `Sense and Sensibility` se estrenó en el año `1995` con un score/popularidad de `18.376137`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función consulta todas las películas del dataset provisto. Si hay más de una película con el mismo nombre (como Sabrina), por ahora devuelve solo los datos de la primera que &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encuentra. Si se ingresa el título de una película que no está incluída aparece un mensaje informando que "La película no está en
el dataset provisto".
 
+  **votos_titulo( *`titulo_película`* )**:
    Se ingresa el título de una película. Devuelve el mismo título, el año de estreno, la cantidad de votos y el valor promedio de las votaciones. Si la cantidad de votos de esa película es menor a 2000, se informa esa situación y no se devuelven sus datos.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo Ingreso: `Blade Runner` - Mensaje de salida: La película `Blade Runner` se estrenó en el año `1982`. La misma cuenta con un total de `3833.0` valoraciones, con &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;un promedio de `7.9`." 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esta función consulta todas las películas del dataset provisto. si hay más de una pelicula con el mismo nombre (como Sabrina), por ahora devuelve solo los datos de la primera que &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encuentra. Si se ingresa el título de una película que no está incluída aparece un mensaje informando que "La película no está en
el dataset provisto".

+  **get_actor( *`nombre_actor`* )**:
    Se ingresa el nombre de un actor. Devuelve el éxito del mismo medido a través de la suma del retorno de las películas en las que participó, la cantidad de películas en las que participó y el promedio de retorno por película. Si un actor fue también director en alguna película el mensaje solo indica eso y no da mas datos
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo Ingreso: `Meryl Streep` - Mensaje de salida: El actor `Meryl Streep` ha participado de `66` películas, consiguió un retorno de `108.24862345926158` con un promedio de &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`1.6401306584736604` por película.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como hay una fila por película y actor Esta función consulta un dataset reducido de  20 actores famosos de los cuales 9 son también directores. Si se ingresa un actor o una actriz que no &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;está en ese grupo se informa cuales son los actores o actrices que pueden elegirse en esta versión. Y cuáles de ellos son también directores. Las películas de los actores/directores &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;también están guardadas en el dataset pero no se consultan.

+ **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director. Devuelve la suma del retorno de todas las películas en las que participó y una lista con el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de las mismas.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo Ingreso: `Sofia Coppola` - Mensaje de salida: El director `Sofia Coppola` consiguió un retorno de `36.87723784761904` Participó en las películas [{ title: The Virgin &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suicides, release_date: 1999-04-21, budget: 6000000.0, revenue: 10409377.0, return: 1.734896166666667} ... 
{title: The Beguiled, release_date: 2017-06-23, budget: 10500000.0, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revenue: 25442939.0, return: 2.4231370476190475} ]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como hay una fila por película y actor esta función consulta un dataset reducido de  17 directores conocidos (al menos por mí). Si se ingresa un director o una directora que no está &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;en ese grupo se informa cuáles son los directores o directoras que pueden elegirse en esta versión. 

+ **recomendacion( *`titulo_película`* )**:
    Se ingresa el título de una película (real o inventado) y recomienda las 5 películas cuyo título es más similar al ingresado.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo Ingreso: `Love actually` - Mensaje de salida: Las 5 películas cuyo título es más similar a `Love actually` son: [{Title: "Making Love", Cos_sim: 0.6508520529150759} ... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{Title: "Priest of Love", Cos_sim: 0.5700211091625234}]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;En esta versión se recomienda entre las 1486 películas en idioma original inglés que se estrenaron entre los años 1980 y 1985.

## **Datos**

Se usa un archivo de datos para cada uno de los end-points. Las funciones get_actor, get_director y recomendación utilizan conjuntos de datos con menor cantidad de actores, directores o películas que el dataset original. En la descripción de cada una se indican la cantidad de opciones posibles.

## **Metodología**

Para el sistema de recomendación de películas se utilizó vectorización y similitud del coseno. Se ordenan los títulos de las películas por coeficiente de similitud decreciente y se muestran los cinco títulos más similares respecto del título de pelicula ingresado. 

## **Futuras versiones**

Este proyecto es un Producto mínimo viable (MVP, por sus siglas en inglés). En versiones futuras se identificarán las distintas películas que tengan un mismo nombre en los end-points donde se consultan datos de las películas por títulos, se podrán consultas los datos de más actores o actrices y directores o directoras de películas. En el sistema de recomendación se incluirán titulos de películas de otros años y en otros idiomas originales. Y las recomendaciones considerarán otras características además del título de la película.

## **Autora**

M. Victoria Riso victoriariso@gmail.com

