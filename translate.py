from googletrans import Translator

a = Translator()
# a = Translator.translate('If source language is not given, google translate attempts to detect the source language.')

a.translate('If', dest='ja')