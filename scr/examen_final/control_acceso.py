###*Ejercicio CONTROL_ACCESO:* Control de Acceso con Intentos (Bucle while y break)
##Escribe un programa que simule el acceso a una cuenta personal mediante una contraseña previamente definida (por ejemplo, "python123").
##- El usuario tiene un máximo de 3 intentos para ingresar la clave correcta.
##- Si ingresa la contraseña correcta, el programa debe mostrar "Acceso concedido" y terminar inmediatamente con break.
##- Si se equivoca, debe mostrar cuántos intentos le quedan.
##- Si agota los 3 intentos sin éxito, debe imprimir "Cuenta bloqueada por seguridad

clave:str="python123"
intentos:str|int = 3

while intentos > 0:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == clave:
        print("Acceso concedido")
        break
    else:
        intentos = intentos - 1
        print("Intentos que quedan:", intentos)
if intentos == 0:
    print("Cuenta bloqueada por seguridad"