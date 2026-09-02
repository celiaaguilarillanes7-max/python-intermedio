## Usando while crear un programa que me de un pregunta para responder y que solo tengo 3 oportunidades  para dar con la respúesta correcta

respuesta = ""
intentos = 0

while respuesta != "Tierra" and intentos < 3:
    respuesta = input("¿Cuál es el planeta donde vivimos? ")
    intentos = intentos + 1

    if respuesta != "Tierra":
        print("Respuesta incorrecta")
        print("Te quedan", 3 - intentos, "oportunidades")

if respuesta == "Tierra":
    print("¡Respuesta correcta!")
else:
    print("Se acabaron tus 3 oportunidades")
