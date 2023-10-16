# Importanción de Librerias Necesarias.
import requests
import json

# Creamos una funcion para mostrar toda la informacion de la pelicula.
def mostrarPelicula(datos):
    print("\nInformación de la pelicula:")
    print(f"Title: {datos['Title']}")
    print(f"Released: {datos['Released']}")
    print(f"Year: {datos['Year']}")
    # Para comprobar si hay información sobre el director preguntamos antes de mostrarlo si hay datos.
    if datos.get("Director") == "":
        print(f"Director: {datos['Director']}")
    else:
        print("Director: The director is not known.")
    print(f"Genre: {datos['Genre']}")
    print(f"Actors: {datos['Actors']}")
    print(f"Sinopsis: {datos['Plot']}")
    print(f"Language: {datos['Language']}")
    print(f"Country: {datos['Country']}")
    # Para comprobar si hay información sobre si ha sido premiado preguntamos antes de mostrarlo si hay datos.
    if datos.get("Awards") == "":
        print(f"Awards: {datos['Awards']}")
    else:
        print(f"Awards: Has not been awarded yet.")
    print(f"Taquilla: {datos['BoxOffice']}")

# Creamos una funcion para mostrar toda la información de la serie.
def mostrarSerie(datos):
    print("\nInformación de la serie:")
    print(f"Title: {datos['Title']}")
    print(f"Released: {datos['Released']}")
    print(f"Year: {datos['Year']}")
    # Para comprobar si hay informacion sobre el director preguntamos antes de mostrarlo si hay datos.
    if datos.get("Director") == "":
        print(f"Director: {datos['Director']}")
    else:
        print(f"Director: The director is not known.")
    print(f"Genre: {datos['Genre']}")
    print(f"Actors: {datos['Actors']}")
    print(f"Sinopsis: {datos['Plot']}")
    print(f"Language: {datos['Language']}")
    print(f"Country: {datos['Country']}")
    # Para comprobar si hay informacion sobre si ha sido premiado preguntamos antes de mostrarlo si hay datos.
    if datos.get("Awards") == "":
        print(f"Awards: {datos['Awards']}")
    else:
        print(f"Awards: Has not been awarded yet.")

# Creamos una funcion para buscar las peliculas y series por su titulo.
def buscarPeliculaYSeriePorTitulo(api_key):
    busqueda = input("\nIntroduce el título de la pelicula o serie: ")
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={busqueda}"
    response = requests.get(url) # Usando la url de la API lo que hace la peticion con lo que el usuario ha solicitado.

    if response.status_code == 200: # Es para comprobar si se ha conectado a la API cuando se ha hecho la llamada anteriomente.
        datos = json.loads(response.text)
        if datos.get("Response") == "True": # Si en los datos cargados existe la informacion que se solicita pues nos mostrara lo solicitado.
            if datos.get("Type") == "movie": # Pero antes de mostrar se comprobara si lo solicitado es una pelicula o una serie.
                mostrarPelicula(datos)
            else:
                mostrarSerie(datos)
        else:
            print("Series or Movie not found.")
    else:
        print("Error connecting to API.") # Mensaje de Error por si no se ha podido conectar a la API.

def main():
    # Creamos una variable que se le va asignar nuestra clave para conectarno a la API para poder hacer nuestras busquedas.
    api_key = 'ca4b88fd'

    while True:
        print("\nMenú de opciones:")
        print("1. Buscar una película o Serie por Titulo")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            buscarPeliculaYSeriePorTitulo(api_key)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Introduce 1 o 2.")

if __name__ == "__main__":
    print("Bienvenido al Rastreador de Películas y Series de TV")
    main()