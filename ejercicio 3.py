#Ejercicio 3
import requests

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as f:
                f.write(response.content)
            print(f"La imagen se ha descargado correctamente como '{nombre_archivo}'.")
        else:
            print(f"Error al descargar la imagen. Código de respuesta: {response.status_code}")
    except requests.RequestException as e:
        print("Error al descargar la imagen:", e)

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
nombre_archivo = "imagen_descargada.jpg"

descargar_imagen(url, nombre_archivo)
