from googletrans import Translator
import googletrans

print(googletrans.LANGUAGES)

translator = Translator()
result = translator.translate('It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout', src='en', dest='be')

print(result.src)
print(result.dest)
print(result.text)

# pip install googletrans==3.1.0a0

