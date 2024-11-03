"""
Created on Thu Oct 31 18:02:49 2024

@author: ara06
"""

def lista_enteros(lista):
    positivos = []
    negativos = []
    
    #Iteramos la lista de entrada y separamos los números
    for num in lista:
        if num >= 0:
            positivos.append(num)
        else:
            negativos.append(num)
            
    #Ordenamos las listas
    positivos.sort()
    negativos.sort()
    
    
    return positivos, negativos

num = [2, 15, -63, 8, 0, -12, -7, 6, 22, -6]

lista_positivos, lista_negativos = lista_enteros(num)

print("Positivos:", lista_positivos)
print("Negativos:", lista_negativos)

