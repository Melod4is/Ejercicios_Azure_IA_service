#las librerias para el servicio de texto se instala como:  pip install azure-ai-textanalytics==5.3.0


from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    global ai_endpoint
    global ai_key

    try:
        # configurando variables de entorno
        load_dotenv()
        ai_endpoint = os.getenv('AI_ENDPOINT')
        ai_key = os.getenv('AI_KEY')

        # utilizar "salir" para dejar de consumir los servicios
        userText =''
        while userText.lower() != 'salir':
            userText = input('\nIngresar texto ("salir" para detener ejecución)\n')
            if userText.lower() != 'salir':
                language = GetLanguage(userText)
                print('Idioma:', language)

    except Exception as ex:
        print(ex)

def GetLanguage(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name


if __name__ == "__main__":
    main()