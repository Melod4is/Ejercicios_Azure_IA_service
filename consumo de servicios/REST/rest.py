from dotenv import load_dotenv
import os
import http.client, base64, json, urllib
from urllib import request, parse, error

def main():
    global ai_endpoint
    global ai_key

    try:
        # configuración de variables de entorno
        load_dotenv()
        ai_endpoint = os.getenv('AI_ENDPOINT')
        ai_key = os.getenv('AI_KEY')

        # creando imput (para salir se escribe salir)
        userText =''
        while userText.lower() != 'salir':
            userText = input('Ingresa texto ("salir"  para finalizar la ejecución)\n')
            if userText.lower() != 'salir':
                GetLanguage(userText)


    except Exception as ex:
        print(ex)

def GetLanguage(text):
    try:
        # Construyendo JSON request body
        jsonBody = {
            "documents":[
                {"id": 1,
                 "text": text}
            ]
        }

        # JSON que envia el servicio
        print(json.dumps(jsonBody, indent=2))

        # Creando un HTTP request para la REST interface
        uri = ai_endpoint.rstrip('/').replace('https://', '')
        conn = http.client.HTTPSConnection(uri)

        # Añadiendo la authentication key al request header
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': ai_key
        }

        # usando el Text Analytics language API
        conn.request("POST", "/text/analytics/v3.1/languages?", str(jsonBody).encode('utf-8'), headers)

        # Enviando el request
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

        # si el llamado es exitoso obtener el request
        if response.status == 200:

            # mostrando el resultado
            results = json.loads(data)
            print(json.dumps(results, indent=2))

            # Estrayendo la deteccion de lenguaje de cada documento
            for document in results["documents"]:
                print("\nIdioma:", document["detectedLanguage"]["name"])

        else:
            # si hay un error lo imprime en consola
            print(data)

        conn.close()


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()