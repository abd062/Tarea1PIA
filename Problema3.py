"""
Created on Thu Oct 31 18:02:49 2024

@author: ara06
"""
import string

def conjunto_numeros(mensaje):

    numeros = input(mensaje)
    conjunto = set(int(num) for num in numeros.split())
    
    return conjunto

#Obtenemos los conjuntos de números
conjunto1 = conjunto_numeros("Introduce un conjunto de números serparado por espacios: ")
conjunto2 = conjunto_numeros("Introduce un segundo conjunto de números separados por espacios: ")

interseccion = conjunto1 & conjunto2
union = conjunto1 | conjunto2
diferencia_simetrica = conjunto1 ^ conjunto2

print("Intersección: ", interseccion)
print("Unión: ", union)
print("Diferencia simétrica: ", diferencia_simetrica)
