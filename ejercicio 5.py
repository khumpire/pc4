#Ejercicio 5

import requests
import csv

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]["USD"]["rate"]
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_precio_bitcoin_txt(precio):
    try:
        with open("precio_bitcoin.txt", "w") as file:
            file.write(precio)
        print("El precio de Bitcoin se ha guardado en el archivo precio_bitcoin.txt")
    except IOError:
        print("Error al guardar el precio de Bitcoin en el archivo precio_bitcoin.txt")

def guardar_precio_bitcoin_csv(precio):
    try:
        with open("precio_bitcoin.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Precio de Bitcoin"])
            writer.writerow([precio])
        print("El precio de Bitcoin se ha guardado en el archivo precio_bitcoin.csv")
    except IOError:
        print("Error al guardar el precio de Bitcoin en el archivo precio_bitcoin.csv")

precio = obtener_precio_bitcoin()

if precio is not None:
    guardar_precio_bitcoin_txt(precio)
    guardar_precio_bitcoin_csv(precio)