#Import all necesaries libraries
from selenium import webdriver
import pandas as pd
import time

#Create an instance of webdriver to scrap.
#It uses an chrome driver located on root path.
driver = webdriver.Chrome(executable_path = r'chromedriver.exe')

def get_links():
    #Get url to scrap all the series.
    url_series = "https://www.starz.com/ar/es/view-all/blocks/1523514"

    #Set url to the drive. Wait 8 seconds to load all the data from url.
    driver.get(url_series)
    time.sleep(8)


    #Create an empty list to get all links in html variable.
    lista_links = []


    #Iterate throught xpath looking for href attribute.
    for link in driver.find_elements_by_xpath('.//a'):
        lista_links.append(link.get_attribute('href'))


    #Filter none objects.
    lista_links = list(filter(None, lista_links))


    #Series links have '/series/' string on their urls.
    #Create a varible to filter later.
    movies_match = '/series/'



    #List comprehension to filter by the previous string.
    #Convert to set to remove duplicates.
    #Then, convert to list again to iterate.
    #Now, we have the links of all series.
    return list(set([link for link in lista_links if movies_match in link]))

def get_metadata(useful_links):
    #Empty list to save the collection of dictionaries.
    #Dictionary to save metada from series and append it on the list.
    lista_series = []


    #Iterate throught series links.
    #Get data from url and wait 5 second to get all data from the url.
    #Get data from xpath and save it.
    #Then, create a dictionary to store metadata and append it on the list.
    # It might crash if the driver doesn't have enough time to retrive the metadata.
    # If that happends, try to execute this loop again.
    for i in useful_links:
        print(i)
        driver.get(i)
        time.sleep(4)
        titulo = driver.find_element_by_xpath('.//*[@id="seriesDetailsH1"]').text
        clasificacion = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[1]').text
        episodios = driver.find_element_by_xpath('./html/body/starz-root/div/div[1]/section/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[2]/span[1]').text +' '+ driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[2]/span[3]').text
        genero = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[3]').text
        anio = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[4]').text
        sinopsis = driver.find_element_by_xpath('.//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/div[2]').text[:-8]
        diccionario_series = {
            'titulo':titulo,
            'clasificacion':clasificacion,
            'episodios':episodios,
            'genero':genero,
            'año':anio,
            'sinopsis':sinopsis
        }
        lista_series.append(diccionario_series)
    print("******Fin******")


    #Transform list to pandas dataframe.
    df = pd.DataFrame(lista_series)


    #Save it to csv file
    df.to_csv('datasets/series.csv')


    #Save it to json file
    df.to_json('datasets/series.json')

lista_de_series = get_links()
get_metadata(lista_de_series)
driver.quit()




