#Ejercicio 1
import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        precio = data['bpi']['USD']['rate_float']
        return precio
    except requests.RequestException as e:
        print(f'Error al obtener el precio de Bitcoin: {e}')
        return None

def calcular_valor_bitcoins():
    try:
        n = float(input('Ingrese la cantidad de bitcoins que posee: '))
        precio_bitcoin = obtener_precio_bitcoin()
        if precio_bitcoin is not None:
            valor_total = n * precio_bitcoin
            print(f'El costo actual de {n} bitcoins es: ${valor_total:,.4f} USD')
    except ValueError:
        print('Cantidad inválida de bitcoins.')

calcular_valor_bitcoins()

