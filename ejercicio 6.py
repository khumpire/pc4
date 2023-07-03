#Ejercicio 6

import sqlite3
import requests
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def crear_tabla_bitcoin(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE bitcoin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                precio_usd REAL,
                precio_gbp REAL,
                precio_eur REAL
            )
        ''')
        conn.commit()
        print("La tabla bitcoin ha sido creada correctamente.")
    except sqlite3.Error as e:
        print("Error al crear la tabla bitcoin:", e)

def insertar_datos_bitcoin(conn, precios):
    try:
        cursor = conn.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur)
            VALUES (?, ?, ?, ?)
        ''', (fecha, precios["USD"]["rate_float"], precios["GBP"]["rate_float"], precios["EUR"]["rate_float"]))
        conn.commit()
        print("Datos de precio de Bitcoin insertados correctamente.")
    except sqlite3.Error as e:
        print("Error al insertar los datos de precio de Bitcoin:", e)

conn = sqlite3.connect("cryptos.db")

crear_tabla_bitcoin(conn)

precios = obtener_precio_bitcoin()

if precios is not None:
    insertar_datos_bitcoin(conn, precios)
conn.close()