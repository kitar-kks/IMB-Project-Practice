import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-06-04',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def en_to_fr(*args):
    translation = language_translator.translate(
        text=args,
        model_id='en-fr').get_result()
    return translation.get("translations")[0].get("translation")

def fr_to_en(*args):
    translation = language_translator.translate(
        text=args,
        model_id='fr-en').get_result()
    return translation.get("translations")[0].get("translation")
