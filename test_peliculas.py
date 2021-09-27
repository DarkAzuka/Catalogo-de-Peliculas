from dominio.pelicula import Pelicula
from servicio.catalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != "4":
    print(" Menu de Opciones: ")
    print("1 Agregar Pelicula a tu catalogo")
    print("2 Tu Catalogo de Peliculas: ")
    print("3 Eliminar Pelicula de tu Catalogo")
    print("4 Salir")
    opcion = input("Escribe tu opcion 1, 4:")
    
    if opcion == "1":
       nombre_pelicula = input("Proporciona el nombre de la pelicula")
       pelicula = Pelicula(nombre_pelicula)
       CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar
else:
    print("Salimos del Programa...")