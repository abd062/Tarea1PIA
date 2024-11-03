"""
Created on Thu Oct 31 18:02:49 2024

@author: ara06
"""

import string

def frecuencia_palabras(frase):
    
    #Convertimos a minuscula y eliminamos signos de puntuación
    frase = frase.lower()
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    
    #Dividimos la frase en palabras
    palabras = frase.split()
    
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
            
    frecuencias_ord = dict(sorted(frecuencias.items()))
    
    print("Frecuencia de palabras: ")
    for palabra, frecuencia in frecuencias_ord.items():
        print(f"{palabra}: {frecuencia}")
        
        
frase = input("Introduzca una frase, por favor: ")
frecuencia_palabras(frase)