# CONTROL DE FLUJO
## condicionales 
###  la sentencia if
esta sentencia al igual que en otros lenguajes de programacion en su escritura devemos añadir una `expreson de comparacion `, terminandpo en dos puntos `:`
```python
temperatura:float=40.0
if temperatura > 20:
    print ("alta temperatura)
``` 
en este caso solo se ejecutara el bloque `if` si la condicion es `verdadero`, para controlar si la condicion es `falsa` debemos usar la sentencia `else`.
```python
temp:int=40
if temp>35:
    print("temperatura alta")
else:
    print("temperatura normal")
```
podriamos tener muchas condicionales, lo que se llamariA tecnicamente **condiciones anidadas**
```python
temp:int=20
if temp <20:
    if temp <10:
        print("nivel azul mucho frio")
    else:
        print("nivel verde normal")
    else:
        if temp < 30:
       print("nivel naranja")
    else:
        print("nivel rojo")
```
python ofrece una mejora en la escritura de condiciones anidadas, para ello podemos usar las sentencias `elif`

```python
temp:int=20
if temp <20:
    if temp <10:
        print("nivel azul mucho frio")
    else:
        print("nivel verde normal")
        elif temp < 30:
       print("nivel naranja")
    else:
        print("nivel rojo")
```

### sentencia match-case
Esta es una nueva centencia condiional, similar a los if anidados:
```python
vocal:str= "a"
match vocal:
case "a":
    print("es una vocal")
case "e":
    print("es iun vocal")
case "i":
    print("es una vocal")
case "o":
    print("es iun vocal")
case "u":
    print("es una vocal")

```
una manera de hacer codigo mas corto es :
```python
    vocal:str=input("ingrese una letra: ")
case "a"| "e" | "i" |"o" | "u" :
    print("es una vocal")
case _:
    print("es una consonante")
```