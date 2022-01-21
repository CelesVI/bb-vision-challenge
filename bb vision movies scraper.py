
#Import all necesaries libraries
from selenium import webdriver
import pandas as pd
import time

#Create an instance of webdriver to scrap.
#It uses an chrome driver located on root path.
driver = webdriver.Chrome(executable_path = r'chromedriver.exe')


def get_links():

    #Get url to scrap all the movies.
    url_pelis = "https://www.starz.com/ar/es/view-all/blocks/1523534"

    #Set url to the drive. Wait 8 seconds to load all the data from url.
    driver.get(url_pelis)
    time.sleep(8)

    #Create an empty list to get all links in html variable.
    lista_links = []

    #Iterate throught xpath looking for href attribute.
    for link in driver.find_elements_by_xpath('.//a'):
        lista_links.append(link.get_attribute('href'))

    #Filter none objects.
    lista_links = list(filter(None, lista_links))


    #Movies links have '/movies/' string on their urls.
    #Create a varible to filter later.
    movies_match = '/movies/'


    #List comprehension to filter by the previous string.
    #Convert to set to remove duplicates.
    #Then, convert to list again to iterate.
    #Now, we have the links of all movies.
    return list(set([link for link in lista_links if movies_match in link]))


def get_metadata(useful_links):
    #Empty list to save the collection of dictionaries.
    #Dictionary to save metada from movies and append it on the list.
    lista_peliculas = []


    #Iterate throught movies link.
    #Get data from url and wait 5 second to get all data from the url.
    #Get data from xpath and save it.
    #Then, create a dictionary to store metadata and append it on the list.
    for i in useful_links:
        print(i)
        driver.get(i)
        time.sleep(5)
        titulo = driver.find_element_by_xpath('.//*[@id="moviesDetailsH1"]').text[4:]
        clasificacion = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[1]').text
        duracion = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[2]').text
        genero = driver.find_element_by_xpath('//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[3]').text
        anio = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[4]').text
        tipo_de_audio = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[5]').text
        sinopsis = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p[1]').text
        diccionario_pelicula = {
            'titulo':titulo,
            'clasificacion':clasificacion,
            'duracion':duracion,
            'genero':genero,
            'año':anio,
            'tipo_de_audio':tipo_de_audio,
            'sinopsis':sinopsis
        }
        lista_peliculas.append(diccionario_pelicula)
    print('******FIN******')

    #Transform list to pandas dataframe.
    df = pd.DataFrame(lista_peliculas)

    #Save it to csv file
    df.to_csv('datasets/peliculas.csv')

    #Save it to json file
    df.to_json('datasets/peliculas.json')

lista_de_peliculas = get_links()
get_metadata(lista_de_peliculas)
driver.quit()




