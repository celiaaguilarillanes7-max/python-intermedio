"""1. escribe un programa que acepte la opcion de dos jugadores en piedra_papel
- entrada: persona1=piedra,persona2=papel
- salida:gana persona2,papel envuelve piedra

2. escribe un programa que hacepte 3 numeros y calcule el minimo
- entrada: 7,4,8
- salida: 4
"""
persona1 = input("Persona 1: ")
persona2 = input("Persona 2: ")

if persona1 == persona2:
    print("Empate")
elif persona1 == "piedra":
    if persona2 == "papel":
        print("Gana persona 2")
    else:
        print("Gana persona 1")
elif persona1 == "papel":
    if persona2 == "piedra":
        print("Gana persona 1")
    else:
        print("Gana persona 2")
""""""
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

if num1 <= num2:
    if num1 <= num3:
        minimo = num1
    else:
        minimo = num3
else:
    if num2 <= num3:
        minimo = num2
    else:
        minimo = num3

print("El minimo es:", minimo)