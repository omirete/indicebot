import json
from typing import Union
from requests import get


from .rubros import rubros
from ..utils import verificar_o_crear_carpetas, utc_timestamp, random_wait


def guardar_datos(data, carpeta: str):
    """
    Guarda los datos indicados en las carpetas y archivos correspondientes.
    """
    with open(f'{carpeta}/{utc_timestamp()}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def registrar_datos_alvear_por_rubro(rubro: str, carpeta: str):
    if rubro in [None, ""]:
        raise TypeError("Tenés que indicar el rubro.")

    base_endpoint = "https://alvearonline.com.ar:9993/api/Catalogo/GetCatalagoSeleccionado"
    params = {
        "idCatalogo": 1042,  # Siempre es 1042. Puede cambiar en el futuro.
        # "subfiltros": None,
        # "page": 1,
        # Si no se envía "pageSize", el servidor devuelve el listado completo
        # "pageSize": 40,
        "idInstalacion": 3,  # no me queda claro qué es esto, pero siempre es 3
        "idSubRubro": rubros[rubro]["id"],
        "esRubro": rubros[rubro]["esRubro"],
        "vistaFavoritos": False
    }

    carpeta_base = carpeta or './historial'
    folder_path = f'{carpeta_base}/alvear/{rubro}'
    verificar_o_crear_carpetas(folder_path)

    response = get(base_endpoint, params, timeout=10)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        guardar_datos(response.json(), folder_path)


def registrar_datos_alvear(carpeta: Union[str, None] = None):
    for rubro in rubros:
        print(f'Registrando datos del Alvear. Rubro: {rubro}')
        registrar_datos_alvear_por_rubro(rubro, carpeta)
        # Para ser buenos ciudadanos (y para que no nos bloqueen la IP 😅),
        # vamos a esperar aleatoriamente entre 5 y 8 segundos después de cada
        # consulta (valores arbitrarios). Con esto intentamos evitar
        # congestionar la web.
        random_wait(5, 8)
