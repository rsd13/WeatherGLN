import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import date


PAHT_TEXTOS = "./../../dataset/"
CODIGOS_PROVINCIA_AEMET={
    'alicante':"03",
    'rioja':"26",
    'madrid':"28",
    'tenerife':"381"
}

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
   
def authRequest(value):
    """
    se encarga de recoger y guardar en la base de datos toda la información númerica y/o texto de los datos de AEMT
    dates<lst>: lista que contiene el rango de fechas para recuperar la información
    return<json>: JSON con la información obtenida en la API
    """
    params = {
        'api_key': getParameterEnv("KEY")
    }
   
    url = getParameterEnv("URL_TEXT_HOY").format(var1=value) + "2021-12-22" #date.today().strftime("%Y-%m-%d")
    print(url)
    headers = {
         'cache-control': "no-cache"
    }
    response = requests.get(url,headers=headers, params=params) 
    return response.json()
    
def saveText(data,value):
    """
    consigue el texto de la predicción meteorologica y lo guarda
    data: URL que contiene el texto de la predicción meteorologica
    value: nombre de la provincia que se guarda los datos
    """
    response = requests.get(data["datos"])
    path = "%s%s/"%(PAHT_TEXTOS,"prueba")
    #si no existe el directorio se crea
    if  not os.path.exists(path):
        os.makedirs(path)
    fichero = open("%s%s.txt"%(path,"2021-12-22"),"w")
    fichero.write(response.text)
    fichero.close()
    print("Predición meteorologica de %s del dia %s guardada"%(value,"2021-12-22"))


def run_api(arg, **kwargs):
    """
    se encarga de recoger y guardar en la base de datos toda la información númerica y/o texto de los datos de AEMT
    arg<string>: argumento para ver que información recoger
    dates<lst>: lista que contiene el rango de fechas para recuperar la información
    """
    #consigue los .env
    getEnv()
    #hace llamada a la API
    if arg=="t":
        for key, value in CODIGOS_PROVINCIA_AEMET.items():
            json = authRequest(value)
            saveText(json,key)

    """ 
    for date in range(int(dates[0]),int(dates[1])):
        json = authRequest(str(date))
        print(json)
    """
