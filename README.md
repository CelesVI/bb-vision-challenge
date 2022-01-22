# bb-vision-challenge

[Link al sitio](https://bb.vision/)

# Motivación 

La idea consiste de hacer un web scraper de la página https://www.starz.com/ar/es/ y obtener la metadata de las películas y series allí hosteadas.
Una vez obtenida la metadata, guardarla en formato .csv o .json.
Luego, se usará la información para una posterior análisis.

# Objetivos principales.

* Obtener la información de las películas y series.
* Obtener metadata (título, año, duración, etc.) de cada pélicula y serie.
* Guardar la información en un archivo .csv o .json.

# Tecnologías usadas.

* Lenguaje : Python 3.x.
* Librerías : selenium, pandas, time.

Dentro del proyecto, hay un archivo requirements.txt para ejecutar e instalar las librerías mencionadas.
También un driver de Chrome que sirve como browser para el scraping.

# Recorrido

Primero apunto al caso particular, es decir, obtener la metadata de un película y de una serie con selenium.
Una vez obtenidos, se crea un diccionario donde se guarda la metedata (clave y valor) y se agrega al final de una lista.
Por último, se crea el dataframe usando pandas con la lista hecha como parámetro. Este dataframe se guarda en formato .csv y .json

Un vez hecho el caso particular, vamos al general.
Para eso se usa un link donde están todas las películas y series, respectivamente.
Primero se obtiene todos los links dentro del link, buscándolo por el atributo 'href' que se guardan dentro de una lista.
Luego, se hacen los filtrados correspondientes para quedarnos con los links que son de utilidad.
Los links útiles pasan por el mismo proceso que el caso particular, agrupándolos todos en una lista para luego crear el dataframe.

Por último, se realiza la obtención de la metadata de los episodios de una serie.
Esta se realiza de manera similar al caso general, trabajando con los links de cada temporada.

Los resultados se almacenan en la carpeta datasets.

# Instalación

* Bajar el repositorio
* Para los archivos .ipynb, crear una instancia de jupyter notebook para su ejecución.
* Para los archivos .py, utilizar un IDE como Visual Studio Code para su ejecución.

Ambas hacen lo mismo y poseen docstrings de forma adecuada.


# Modelo de negocio

Starz es una compañía de televisión premiun que ofrece películas y series a través una aplicación, starzplay, tanto para android y apple como para TV.
Poseé una colección de péliculas, series y series originales cuyo géneros incluyen acción, drama, terror, romance, entre otros.
El contenido que ofrece es para mayores de edad, ya que la mayoría de su contenido tiene una clasificación SAM16.
Tiene un modo gratuito de prueba subcribiéndose por mail, donde puede acceder al contenido. Finalizado el período, debe subcribirse por una cuota de U$S 2,49 por mes.
El usuario tiene la opción de descargar algunos de sus contenidos, con la posibilidad de verlo offline. Luego, este se borra de su dispositivo automáticamente.














