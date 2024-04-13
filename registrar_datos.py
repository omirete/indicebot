import argparse
from helpers.alvear import registrar_datos_alvear

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--folder',
    type=str,
    help='Carpeta donde se guardarán los datos')
args = parser.parse_args()
carpeta_base = args.folder

registrar_datos_alvear(carpeta_base)
