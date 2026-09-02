## creatr un programa de login que mientras que la persona no ponga el usuario y contraseña correcto le siga pidiendo esa informacion, si el usuario/contraseña son correctos entoces darle un mensaje de bi9embenida y salir del programa
usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = ""
contrasena = ""

while usuario != usuario_correcto:
    usuario = input("Ingrese usuario: ")

    if usuario != usuario_correcto:
        print("Usuario incorrecto")

while contrasena != contrasena_correcta:0
    contrasena = input("Ingrese contraseña: ")

    if contrasena != contrasena_correcta:
        print("Contraseña incorrecta")

print("¡Bienvenido!")