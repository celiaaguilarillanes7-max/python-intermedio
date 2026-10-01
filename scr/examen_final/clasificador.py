###*Ejercicio CLASIFICAADOR*: Clasificador de Clima (Condicionales if-elif-else)
##Escribe un programa que pida al usuario la temperatura actual en grados Celsius (número decimal) y muestre un mensaje según los siguientes rangos:
#- Si es menor a 10: "Mucho frío"
#- Si está entre 10 y 25 (inclusive): "Clima templado"
#- Si está entre 26 y 35 (inclusive): "Clima cálido"
#- Si es mayor a 35: "Alerta de calor extremo

temp:int=20
if temp <20:
    print("mucho frio")
elif temp <=25:
    print("clima templado")
elif temp <=35:
    print("clima calido")
else:
    print("alerta de calor extremo")

###
temp_actual:float=float(input("ingrese la temperatura actual:"))
if temp_actual<10:
  print("mucho ffrio")
elif 10<=temp_actual<=25:
  print("clima templado")
elif 26<=temp_actual<=35:
   print("clima calido")
else:
   print("alerta de calor extremo")