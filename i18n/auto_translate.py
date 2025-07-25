"""
Update empty translations.

To run this script:
* pip install polib deepl
* DEEPL_API_TOKEN=.... python update_translations.py

This will process all .po files in this directory, translating any
untranslated strings, marking them as "fuzzy" translations.
"""
import polib
import deepl
import os
import re
from pathlib import Path


def translate(text, lang, api_token):
    # Define a dictionary to hold the mappings of tokens to placeholders
    placeholders = {}

    # Use a regular expression to find all the tokens
    tokens = re.findall(r'%\((.*?)\)s', text)

    # Replace each token with a unique placeholder
    for i, token in enumerate(tokens):
        placeholder = f'__PLACEHOLDER_{i}__'
        placeholders[placeholder] = f'%({token})s'
        text = text.replace(f'%({token})s', placeholder)

    # Perform the translation
    translator = deepl.Translator(api_token)
    translated_text = str(translator.translate_text(text, target_lang=lang))

    # Replace the placeholders back with the original tokens
    for placeholder, token in placeholders.items():
        translated_text = translated_text.replace(placeholder, token)

    return translated_text


def process_file(filename, lang, api_token):
    po = polib.pofile(filename)
    for entry in po.untranslated_entries():
        # Pluralized strings need more handling.
        if entry.msgid_plural:
            continue
        if not entry.msgstr:
            print(f"EN >>> {entry.msgid}")
            print('---------------------------------------------')
            entry.msgstr = translate(entry.msgid, lang, api_token)
            entry.fuzzy = True
            print(f"{lang} <<< {entry.msgstr}")
            print("\n")
        po.save(filename)


if __name__ == '__main__':
    try:
        api_token = os.environ["DEEPL_API_TOKEN"]
    except KeyError:
        print("Export DEEPL_API_TOKEN into the environment")
    else:
        i18n = Path()
        for filename in i18n.glob("contents+*.po"):
            lang = filename.name.split("+")[1].split(".")[0]
            # We don't need to translate English.
            # Farsi isn't a valid target language for DeepL.
            if lang not in {"en", "fa"}:
                # Map ISO language codes to the DeepL target codes
                target_lang = {
                    "pt": "pt-br",
                    "zh_CN": "zh-HANS",
                    "zh_TW": "zh-HANT",
                }.get(lang, lang)
                print(f"===== Processing {target_lang} =====")
                process_file(str(i18n / filename), target_lang, api_token)
