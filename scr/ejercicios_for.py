## 1. crear una lista de ingredientes ["camote","papa","queso","huevo"] crear un programa que recorra con for los elementos de la lista y me retorne el valor y su indise del ingrediente "queso".

ingredientes =list[str]=["camote", "papa", "queso", "huevo"]

for i in ingredientes:
    if i == "queso":
        print(f"el valor es:{i}")
        print(f"el indice es:{ingredientes.index(i)}")

## 2. del siguiente texto "errar el umano dijo el pato bajandose de la gallina" encontrar en error ortografico y corregir por el correcto.

texto:str= "errar el umano dijo el pato bajandose de la gallina"

lista_texto:list=texto.split(" ")
for i in lista_texto:
    if i=="umano":
        lista_texto[lista_texto.index("umano")]="humano"
print("".join(lista_texto))
## opcion 2
texto_corregido:str=texto.replace("umano","humano")
print(texto_corregido)