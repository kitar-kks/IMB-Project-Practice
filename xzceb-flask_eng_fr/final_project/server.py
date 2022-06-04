from machinetranslation import translator 
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

db = {}
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translator.en_to_fr(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translator.fr_to_en(textToTranslate)
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
