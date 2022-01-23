#Import necesary libraries.
from selenium import webdriver
import pandas as pd
import time




#Create instance of driver.
driver = webdriver.Chrome(executable_path = r'chromedriver.exe')

def get_links():
    # Test link: "https://www.starz.com/ar/es/series/reign/63571"

    #Series url to get episodies.
    url = input('Ingrese un link de una serie de www.starz.com: ')
    #Load url on driver. Wait 8 seconds to load all metadata.
    driver.get(url)
    time.sleep(8)

    #Get all links in url.
    lista_links = []


    for link in driver.find_elements_by_xpath('.//a'):
        lista_links.append(link.get_attribute('href'))


    #Filter None.
    lista_links = list(filter(None, lista_links))


    # Creating match patron to get seasons and episode.
    # Insert to redo episodes links.
    season_match = "/season-"
    episode_match = "/episode-"


    # Get season links.
    lista_temporadas = [link for link in lista_links if season_match in link]


    # Get season links. Remove all links with "episode" on it.
    # At first time, get attribute href only get links for first season, ignoring any other.

    return [link for link in lista_temporadas if episode_match not in link]

def get_metadata(lista_temporadas):
    languaje_insert = "/ar/es"
    episode_match = "/episode-"

    
    #Get serie title.
    titulo_serie= driver.find_element_by_xpath('.//*[@id="seriesDetailsH1"]').text


    # List to save episode links.
    lista_episodios = []


    # List to get all href from season.
    lista_links_episodios = []
        

    # Save all links from all seasons.
    for link in lista_temporadas:
        driver.get(link)
        time.sleep(5)
        for i in driver.find_elements_by_xpath('.//a'):
            lista_links_episodios.append(i.get_attribute('href'))


    #Filter None.
    lista_links_episodios = list(filter(None, lista_links_episodios))


    # Filter by string "/episode-"
    lista_episodios = [link for link in lista_links_episodios if episode_match in link]


    # By default, episode links are in English.
    # If continue like that, all metadata retrieved are in English.
    # Add "/ar/es" to get metadata in Spanish.
    # "/ar/es" string is in languaje_insert variable.
    # Insert after 'm/'
    index = link.find('m/')
    lista_episodios = [link[:index+1]+languaje_insert+link[index+1:] for link in lista_episodios]
        

    # List to save episodes metadata.
    # Then, use it to store data in .csv and .json.
    lista_episodios_final = []


    # Get metadata from xpath.
    # Wait 5 seconds for each episode to load all data.
    # Then, save it into dictionary to append it to lista_episodios_final.
    # It might crash if the driver doesn't have enough time to retrive the metadata.
    # If that happends, try to execute this loop again.
    for link in lista_episodios:
        print(link)
        driver.get(link)
        time.sleep(5)
        titulo = driver.find_element_by_xpath('.//html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/h5').text
        clasificacion = driver.find_element_by_xpath('.//html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/ul/li[1]').text
        duracion = driver.find_element_by_xpath('.//html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/ul/li[2]').text
        anio = driver.find_element_by_xpath('.//html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/ul/li[3]').text
        tipo_de_sonido = driver.find_element_by_xpath('.//html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/ul/li[4]').text
        sinopsis = driver.find_element_by_xpath('/html/body/starz-root/starz-base-modal/div/div/div/div[2]/starz-episode-details-modal/div/section/div/div[1]/div[2]/div[1]/p[1]').text
        diccionario_episodio = {
            'titulo':titulo,
            'clasificacion':clasificacion,
            'duracion':duracion,
            'año':anio,
            'tipo_de_sonido': tipo_de_sonido,
            'sinopsis':sinopsis
        }
        lista_episodios_final.append(diccionario_episodio)
    print('******FIN******')


    # Transform list into DataFrame.
    df = pd.DataFrame(lista_episodios_final)


    df.to_csv('datasets/'+titulo_serie+' lista de episodios.csv')


    df.to_json('datasets/'+titulo_serie+' lista de episodios.json')

lista_de_temporadas = get_links()
get_metadata(lista_de_temporadas)
driver.quit()




