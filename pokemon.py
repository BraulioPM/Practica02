# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Seminario 
#Juan Garcia y Braulio Pareja
# Vamos a desarrollar el programa de Python que nos permita, a partir de una lista de 
#palabras, encontrar la lista más larga posible de palabras de manera que la última letra de 
#una palabra coincida con la primera de la siguiente palabra. Para probar el programa la lista 
#de palabras con las que vamos a trabajar son la que encontramos en el fichero pokemon.txt 

def pok(elemento, lista):
    for elemento2 in lista1:
       
        if elemento[-1]==elemento2[0]:
            lista2.append(elemento2)
            lista1.remove(elemento2)
            pok(elemento2,lista1)
            break
    
    
    
fichero=open('pokemon.txt','r')

contenido = fichero.read()
fichero.close()
lista=[]

for palabra in contenido.split(' '):
    lista.append(palabra)

lista.remove('\r\n')
lista3=[]

for elemento in lista:
    lista1=lista[:]
    lista2=[]
    lista2.append(elemento)
    lista1.remove(elemento)
    pok(elemento,lista1)
                
    if len(lista2)>len(lista3):
        
        lista3=lista2[:]
    
print lista3
print "Palabras: ",len(lista3)

# <codecell>


# <codecell>


# <codecell>


