import requests

def process_data(data):
    """
    Función recursiva para descomponer estructuras anidadas de diccionarios y listas.
    """
    if isinstance(data, dict):
        return [(k, process_data(v)) for k, v in data.items()]
    elif isinstance(data, list):
        # Si la lista contiene diccionarios, los dejamos tal cual
        if all(isinstance(item, dict) for item in data):
            return data  # No tocar si son diccionarios dentro de la lista
        # Si no son diccionarios, procesamos los elementos de la lista
        return [process_data(item) for item in data]
    else:
        return data

def get_api_data(url: str) -> list:
    """
    Recoge datos JSON desde una API y los convierte en una lista de tuplas <key, value>.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa (código 200)
        try:
            data = response.json()  # Intentar convertir la respuesta a JSON
        except ValueError as json_error:
            print(f"Error al procesar JSON: {json_error}")
            return []  # Retornar lista vacía en caso de error de JSON
        return process_data(data)
    except requests.exceptions.RequestException as req_error:
        print(f"Error en la solicitud a la API: {req_error}")
        return []  # Retornar lista vacía en caso de error en la solicitud
