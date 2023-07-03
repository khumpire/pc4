#Ejercicio 4

def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                resultado = numero * i
                file.write(f"{numero} x {i} = {resultado}\n")
        print(f"Se ha guardado la tabla de multiplicar de {numero} en el archivo tabla-{numero}.txt")
    except IOError:
        print("Error al guardar la tabla de multiplicar.")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            tabla = file.read()
            print(tabla)
    except FileNotFoundError:
        print(f"No existe el archivo tabla-{numero}.txt.")

def mostrar_linea_tabla(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if linea <= len(lineas):
                print(lineas[linea - 1])
            else:
                print(f"No existe la línea {linea} en el archivo tabla-{numero}.txt.")
    except FileNotFoundError:
        print(f"No existe el archivo tabla-{numero}.txt.")


while True:
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        guardar_tabla_multiplicar(numero)
    elif opcion == "2":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        mostrar_tabla_multiplicar(numero)
    elif opcion == "3":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        linea = int(input("Ingrese el número de línea entre 1 y 10: "))
        mostrar_linea_tabla(numero, linea)
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")