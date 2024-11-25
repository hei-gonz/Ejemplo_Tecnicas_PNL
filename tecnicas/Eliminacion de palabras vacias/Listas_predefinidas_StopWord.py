from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

texto = "El procesamiento de lenguaje natural es todo un mundo y útil en muchas aplicaciones."
stop_words = set(stopwords.words('spanish'))
palabras = word_tokenize(texto)

palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]
print(palabras_filtradas)