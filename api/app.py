from googletrans import Translator
import hug

translator = Translator()

@hug.post("/translate")
def translate_text(request):
    try:
        text_to_translate = request['text_to_translate']
        dest = request['dest']

        translated_text = translator.translate(text_to_translate, dest=dest)

        # Obtenir les informations sur les langues source et cible
        source_lang = get_language_info(translated_text.src)
        dest_lang = get_language_info(dest)

        translation_result = f"{source_lang} ➜ {dest_lang}"

        return {"translation": translated_text.text, "translation_info": translation_result}
    except Exception as e:
        raise hug.HTTPBadRequest("Error", str(e))

@hug.get("/ping")
def healthcheck():
    return {"status": "API is running smoothly"}
