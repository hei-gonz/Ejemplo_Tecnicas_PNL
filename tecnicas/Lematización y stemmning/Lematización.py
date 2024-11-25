from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
palabras = ["corriendo", "corre", "corrí"]
for palabra in palabras:
    print(lemmatizer.lemmatize(palabra, pos=wordnet.VERB))