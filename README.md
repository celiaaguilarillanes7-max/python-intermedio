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
## bucles
### la centencia wwhile
Es el primer mecanismo que existe en el python para repetir instrucciones.
la sematica tras esta sematica es : `´mientras se cumpla la condicion has algo`
ejemplo:
```python
salir:str="N"
while salir=="N":
    print("hola que tal")
    salir=input("desea salir (S/N)")
    print("Adios")
```

se puede cortar la ejecucion de un `while` haciendo el uso de `break`:
```python
intentos:int=0
respuesta_corecta:str="ayacucho"
while intentos<3:
respuesta_usuario:str=input("capital ayacucho: ")
if respuesta_correcta = respuesta_usuario
```

### la sentencia for
python permite recorrer aquellos tipos de datos que sean ojo listas y dicionario
**iterable**, Algunos ejemplos de tipos de datos que permiten hacer iterados son : cadenas de texto, listas, diccionarios, ficheros
```python
nombre:str="gargamel" # string, texto, cadena de texto
amigos:list[str]=['pepe','lucho','juan'] # lista de texto
alumno:dict[str:int|str]={
    "dni": 75946302
    "nombre":"juancito"
} # diccionario
```
A continuacion planteamos un ejemplo en el que vamos a recorrer una cadena de texto:
```python
texto:str="hola mundo"
for letra in texto:
  print(letra)
```
la clave para entender el ejercicio es darse cuenta que el bucle va tomando en cada iteracion, cada uno de los elementos de la variable , en el ejemplo `letra` va tomando cada iuna de las letras que tiene `texto`.
la variable `letra`puede tomar cualquier nombre.
**Romper un bucle for**
al igual que while para romper o termionar un bucle `for` debemos usar `break`.
*ojo* - para realizar la rotura se debe previamente cumplir una condicional.
```python
texto:str="holis de donde eres y a donde vas"
for l in texto:
    if l == "a":
        break
    print (l)
```

**secuencias de numeros**
Es muy abitual hace uso de secuencias en bucles, python aporta una funcion para realizar la cecuencia de numeros `range`, esta funcion devuelve o retornaun flujo de numeros en el rango especificado.
su estructura es lo siguiente:
la funcion `range(start,stop,step)`, puede recivir asta tres parametros pocicionales.
- `start` - es *opsional*y tiene valor por efecto `O`
- `stop` - es *obligatorio* (este valor simple llega a 1 menos que el valor asignado)
- `step` - es *opcional* y tiene valor por efecto `1` es el valor que ira 
```python
## 1 deseamos mostrar los numeros del 0 al 5 con la funcion range
for numero in range(6):
    print(numero)
    print("------------------------")
## 2 deseamos mostrar los numeros del 2 al 6
for numero in range(2,7):
    print(numero)
print("----------------------------")
## 3 mostrar los numeros pares que existen entre 1 y 10
for pares in range(2,11,2):
    print(pares)
```
> [!TIP] Se suele utilizar nombres de variables `i,j,k` para lo que se denomina `contadores`. o la variable que va despues del `for`.