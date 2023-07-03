#Ejercicio 2

import random

from pyfiglet import Figlet

def obtener_fuente_aleatoria():
    figlet = Figlet()
    fuentes = figlet.getFonts()
    return random.choice(fuentes)

def imprimir_texto_en_fuente(fuente, texto):
    figlet = Figlet(font=fuente)
    print(figlet.renderText(texto))

fuente = input("Ingrese el nombre de una fuente (presione Enter para una fuente aleatoria): ")
if not fuente:
    fuente = obtener_fuente_aleatoria()

texto = input("Ingrese el texto a imprimir: ")

imprimir_texto_en_fuente(fuente, texto)