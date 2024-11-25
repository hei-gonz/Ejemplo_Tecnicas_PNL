import nltk
from nltk.tokenize import word_tokenize

# Descargar recursos necesarios
nltk.download('punkt')

texto = "El procesamiento de lenguaje natural es todo un mundo."
tokens = word_tokenize(texto)

print(tokens)