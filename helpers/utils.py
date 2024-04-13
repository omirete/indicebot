import os
from datetime import datetime, timezone
from random import random
from time import sleep


def verificar_o_crear_carpetas(path: str):
    """
    Revisa que la ubicación especificada exista. De lo contrario, crea las carpetas necesarias.
    """
    if not os.path.exists(path):
        head = os.path.split(path)[0]
        if head != '':
            verificar_o_crear_carpetas(head)
        os.mkdir(path)
    

def utc_timestamp() -> str:
    now = datetime.now(timezone.utc)
    return now.isoformat()[:19].replace(':', '-')


def random_wait(min_secs: float, max_secs: float):
    seconds = min_secs + (max_secs-min_secs)*random()
    print(
        f"Siendo buen@s ciudadan@s y esperando {round(seconds, 2)} segundos.")
    sleep(seconds)
