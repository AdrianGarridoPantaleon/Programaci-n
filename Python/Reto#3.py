import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def main():
    longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16): "))
    if longitud < 8 or longitud > 16:
        print("Longitud no válida.")
        return
    
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ")
    incluir_numeros = input("¿Incluir números? (s/n): ")
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ")

    contrasena = generar_contrasena(longitud, incluir_mayusculas=='s', incluir_numeros=='s', incluir_simbolos=='s')
    print("Contraseña generada:", contrasena)

main()