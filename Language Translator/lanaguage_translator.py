from googletrans import Translator


def translate_text(text, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text


def main():
    text = input("Enter the text you want to translate: ")
    target_lang = input(
        "Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")
    translated_text = translate_text(text, target_lang)
    print(f"Translated text: {translated_text}")


if __name__ == "__main__":
    main()
