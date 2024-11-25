#Algoritmo de Porter: Es uno de los algoritmos de stemming más utilizados y 
# fue desarrollado por Martin Porter en 1980. Este algoritmo aplica una serie de
#  reglas para cortar los sufijos y obtener la raíz de la palabra.

from nltk.stem import PorterStemmer

ps = PorterStemmer()
palabras = ["corriendo", "corre", "corrí"]
for palabra in palabras:
    print(ps.stem(palabra))