###*Ejercicio CONT_VOCAL:* Contador de Vocales en un Texto (Bucle for y range)
##Pide al usuario que ingrese una frase o palabra. Utilizando un bucle for, recorre la cadena e imprime únicamente los números pares correspondiente a las posiciones/índices de los caracteres, junto con el carácter en dicha posición.

##Pista: Puedes combinar la función range() junto con len(texto) para iterar sobre los índices de la cadena
palabra:str=input("ingresa una palabre:")
for i in range(0,len(palabra),2):
    print(f"en el indice {i}tengo la palabra {palabra [i]}")
------------------------------
for i in range(len(palabra)):
    print(f"en el indice {j}tengo la palabra {palabra [j]}")
###

texto:str= input("Ingrese una frase: ")

for i in range(len(texto)):
    if i % 2 == 0:
        print(i, texto[i])