import os
class CatalogoPeliculas:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            # "a" es modo append
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")
        except Exception as e:
            print("Ocurrio un error al agregar", e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo de Peliculas")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio un error al listar")
        finally:
           archivo.close()
           
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo Eliminado", CatalogoPeliculas)
        except Exception as e :
            print("A ocurrido un error al eliminar el archivo", e)
            
         
        #C:\Cursos Anel\python\fundamentos\catalogo_peliculas\peliculas.txt
        #CatalogoPeliculas.ruta_archivo