import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv


def getParameterEnv(name):
    """
    recoge el value pasando un key del fichero .env
    name: key del fichero .env que se quiere recoger
    """
    #consigue el parametro del .env
    return os.environ.get(name)


def getEnv():
    """
    recoge la información de la API de AEMET


    """
    #se consigue el path del fichero 
    file_env = join(dirname("./"), '.env')
    #toma las variables de entorno de .env.
    load_dotenv(file_env)
   
def authRequest(date):
    """
    se encarga de recoger y guardar en la base de datos toda la información númerica y/o texto de los datos de AEMT
    dates<lst>: lista que contiene el rango de fechas para recuperar la información
    return<json>: JSON con la información obtenida en la API
    """

    params = {
        'api_key': getParameterEnv("KEY")
    }
    url = getParameterEnv("URL_NUM") + date
    print(url)
    headers = {
         'cache-control': "no-cache"
    }

    response = requests.get(url,headers=headers, params=params)
    return response.json()




def run_api(arg,dates):
    """
    se encarga de recoger y guardar en la base de datos toda la información númerica y/o texto de los datos de AEMT
    arg<string>: argumento para ver que información recoger
    dates<lst>: lista que contiene el rango de fechas para recuperar la información
    """
    #consigue los .env
    getEnv()
    #hace llamada a la API
   
    for date in range(int(dates[0]),int(dates[1])):
        json = authRequest(str(date))
        print(json)
