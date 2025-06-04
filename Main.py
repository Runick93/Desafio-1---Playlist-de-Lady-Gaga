import Data
import Application

def main():    
    continuar = True
    playlist_standarizada = []

    while continuar:
        Application.Mostrar_Menu()
        opcion = input("Elege una opcion: ")
        print()

        match opcion:
            case "1":
                playlist_standarizada = Application.Normalizacion_De_Datos(Data.playlist_lady_gaga)

            case "2":
               Application.Mostrar_Lista_Temas(playlist_standarizada)

            case "3":
                Application.Ordenar_Temas(playlist_standarizada)
                
            case "4":
                Application.Promedio_De_Vistas(playlist_standarizada)
                
            case "5":
                Application.Maxima_Reproduccion(playlist_standarizada)
                
            case "6":
                Application.Minima_Reproduccion(playlist_standarizada)
                
            case "7":
                codigo_video = input("Ingrese el codigo de video q desea buscar: ")
                Application.Busqueda_Por_Codigo(playlist_standarizada, codigo_video)
                
            case "8":                
                nombre_colaborador = input("Ingrese el nombre de un colaborador: ")
                Application.Listar_Por_Colaborador(playlist_standarizada, nombre_colaborador)
                                
            case "9":
                mes_lanzamiento = input("Ingrese el mes de lanzamiento: ")
                Application.Listar_Por_Mes_Lanzamiento(playlist_standarizada, mes_lanzamiento)
                                
            case "10":
                print("Hasta luego")
                continuar = False

            case _:
                print("Opcion no valida. Intente de nuevamente.")
                
    

if __name__ == "__main__":
    main()