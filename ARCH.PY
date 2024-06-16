def mostrar_menu():
    print("MENU")
    print("a. Leer archivo .txt")
    print("b. Contar letras y espacios")
    print("c. Generar resumen en otro archivo .txt")
    print("d. Salir")


def leer_archivo(nombre_archivo):
    try:
        with open("hola mundo.txt", 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f'Error: El archivo "{nombre_archivo}" no se encontró.')
    except IOError:
        print(f'Error: No se pudo leer el archivo "{nombre_archivo}".')


def contar_letras_y_espacios(contenido):
    letras = sum(c.isalpha() for c in contenido)
    espacios = sum(c.isspace() for c in contenido)
    return letras, espacios


def generar_resumen(nombre_archivo_entrada, nombre_archivo_salida):
    contenido = leer_archivo(nombre_archivo_entrada)
    if contenido:
        letras, espacios = contar_letras_y_espacios(contenido)
        try:
            with open(nombre_archivo_salida, 'w') as archivo_salida:
                archivo_salida.write(f'Resumen del archivo "{nombre_archivo_entrada}":\n')
                archivo_salida.write(f'- Cantidad de letras: {letras}\n')
                archivo_salida.write(f'- Cantidad de espacios: {espacios}\n')
            print(f'Se ha generado el resumen en el archivo "{nombre_archivo_salida}".')
        except IOError:
            print(f'Error: No se pudo escribir en el archivo "{nombre_archivo_salida}".')


# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada (a, b, c, d): ").strip().lower()

        if opcion == 'a':
            nombre_archivo = input("Ingrese el nombre del archivo .txt a leer: ").strip()
            contenido = leer_archivo(nombre_archivo)
            if contenido:
                print(f'Contenido del archivo "{nombre_archivo}":')
                print(contenido)

        elif opcion == 'b':
            nombre_archivo = input("Ingrese el nombre del archivo .txt para contar letras y espacios: ").strip()
            contenido = leer_archivo(nombre_archivo)
            if contenido:
                letras, espacios = contar_letras_y_espacios(contenido)
                print(f'Cantidad de letras en "{nombre_archivo}": {letras}')
                print(f'Cantidad de espacios en "{nombre_archivo}": {espacios}')

        elif opcion == 'c':
            nombre_archivo_entrada = input("Ingrese el nombre del archivo .txt a resumir: ").strip()
            nombre_archivo_salida = input("Ingrese el nombre del archivo de resumen .txt a generar: ").strip()
            generar_resumen(nombre_archivo_entrada, nombre_archivo_salida)

        elif opcion == 'd':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida (a, b, c, d).")
