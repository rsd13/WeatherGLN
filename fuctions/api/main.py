from aemet import run_api
import argparse
import datetime

HELP1="Recoge los datos númericos de una provincia con un rango de fechas. Las fechas tienen que estar en formato YYYYMMDD. Ej: -n 20210101 20210301"
HELP2="Recoge los textos de una provincia con de un solo dia. Las fechas tienen que estar en formato YYYYMMDD. Ej: -t 20210101 20210301"
HELP3="Recoge los textos y datos númericos de una provincia para el mismo dia. Las fechas tienen que estar en formato YYYYMMDD. Ej: --t 20210101 20210301"


def parse():
    parser = argparse.ArgumentParser()                 # analizador de argumentos
    #grupo que limpia 
    grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
    #grupo.add_argument('-c', '--clear', help='Limpia el dataset y lo deja prepardo para el analisis',action='store_true')           # action guarda el argumento
    grupo.add_argument('-t',action='store',nargs=2,dest='numero',default=[],help=HELP1)
    #grupo.add_argument('-d2',action='append', dest='d2',default=[],help="Añade los estados que se quiere comparar. Ej: -as California -as 'New York' ...")

    #parser.add_argument('string1', help='Primer numero de la operacion.',type=str)
    return parser.parse_args()


def main(): 
    args=parse()
    # opciones
   
    if args.numero:
        try:
            [datetime.datetime.strptime(date, '%Y%m%d') for date in args.numero ]
        except ValueError:
            raise ValueError("Formato de fecha incorrecto, deberia ser YYYYMMDD")
        run_api("n",args.numero)
      
    else:
        print ('Error: se requiere uno o mas argumentos para realizar la accion. Pulsa -h para más información')
    


if __name__=='__main__':
	main()