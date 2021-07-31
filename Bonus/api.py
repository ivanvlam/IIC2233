import json
import requests


# ------------------------------------------------------------------------------------------------
# DEFINIR AQUI LAS CONSTANTES QUE SERAN UTILIZADAS PARA INTERACTUAR CON LA API
NOMBRE = "Iván Vergara"
USERNAME = "ivanvlam"
DOCUMENTO = 1
BASE_URL = "https://actividad-bonus-iic2233.herokuapp.com/{}"


# ------------------------------------------------------------------------------------------------
# Completar a continuación el código para realizar las solicitudes necesarias a la API. Cada
# función recibe los argumentos necesarios para realizar la consulta y aplicar lógica adicional,
# en caso de ser necesario

# Registro en aplicación
def registro(nombre, username):
    # Registrarse en API
    datos = {
        "nombre": nombre,
        "username": username
    }
    
    respuesta = requests.post(BASE_URL.format("estudiantes"), data=datos)
    
    # Retornar código de respuesta
    return respuesta.status_code


# Descarga de documento Markdown
def descargar_documento(identificador_documento, ruta_documento):
    # Obtener documento Markdown
    documento = requests.get(BASE_URL.format(f"documentos/{identificador_documento}"))
    
    # Guardar texto en un archivo
    with open(ruta_documento, 'w') as archivo:
        archivo.write(documento.json()['texto'])


# Probar una de las consulas
def entregar_consulta(n_consulta, identificador_documento, patron, respuesta):
    # Subir resultados a API
    datos = {
        "consulta": n_consulta,
        "documento": identificador_documento,
        "regex": patron,
        "respuesta": respuesta
    }

    recibido = requests.post(BASE_URL.format(f"estudiantes/{USERNAME}/consultas"), json=datos)
    proceso = recibido.json()['proceso']

    resultados = requests.get(BASE_URL.format(f"estudiantes/{USERNAME}/consultas/{proceso}"))
    
    # Retornar identificador de proceso
    return resultados.json()['proceso']

if __name__ == '__main__':
    #aceptado = registro(NOMBRE, USERNAME)
    #print(aceptado)
    
    #estudiantes = requests.get(BASE_URL.format(f"estudiantes/{USERNAME}/consultas"))
    #for estudiante in estudiantes.json():
    #    print(estudiante)
    
    descargar_documento(DOCUMENTO, 'test.md')
    