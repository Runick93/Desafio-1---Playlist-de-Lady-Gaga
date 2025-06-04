import Utils

def Mostrar_Menu():
    print("-= Menú de opciones =-")
    print("1 - Normalización de Datos.")
    print("2 - Mostrar Lista de Temas.")
    print("3 - Ordenar Temas.")
    print("4 - Promedio de Vistas.")
    print("5 - Máxima Reproducción.")
    print("6 - Mínima Reproducción.")
    print("7 - Búsqueda por Código.")
    print("8 - Listar por Colaborador.")
    print("9 - Listar por Mes de Lanzamiento.")
    print("10 - Salir.")

# 1
def Normalizacion_De_Datos(playlist:list) -> list:
    playlist_estadarizada = list()

    for i in range(len(playlist)):
        
        diccionario ={
            'titulo': Utils.Get_Titulo(playlist[i]["Tema"]),
            'colaboradores': Utils.Get_Colaboradores(playlist[i]["Tema"]),
            'vistas': Utils.Get_Vistas(playlist[i]["Vistas"]),
            'duracion': Utils.Get_Duracion(playlist[i]["Duracion"]),
            'link': playlist[i]["Link Youtube"],
            'fechaLanzamiento': Utils.Get_FechaLanzamiento(playlist[i]["Fecha lanzamiento"]),
        }        
        playlist_estadarizada.append(diccionario)
    
    return playlist_estadarizada

# 2
def Mostrar_Lista_Temas(playlist: list):
    
    for i in range(len(playlist)):
        print(f"Tema: {playlist[i]['titulo']} \t\t Duracion: {playlist[i]['duracion']}")

# 3
def Ordenar_Temas(playlist:list):
    Utils.Ordenar_Tema(playlist, "duracion", "desc")

# 4
def Promedio_De_Vistas(playlist:list):
    promedio = Utils.Calcular_Promedio(playlist, "vistas")
    print(f"Promedio de vistas: {promedio}")  #mostrar con millones o mostrar el numero float?

# 5
def Maxima_Reproduccion(playlist:list):
    lista_extremos = Utils.Buscar_Extremos(playlist, "vistas", "max")
    for i in range(len(lista_extremos)):
        indice_extremo = lista_extremos[i]
        Utils.Imprimir_Diccionario(playlist[indice_extremo])

# 6
def Minima_Reproduccion(playlist:list):
    lista_extremos = Utils.Buscar_Extremos(playlist, "vistas", "min")
    for i in range(len(lista_extremos)):
        indice_extremo = lista_extremos[i]
        Utils.Imprimir_Diccionario(playlist[indice_extremo])

# 7
def Busqueda_Por_Codigo(playlist:list, codigo:str):
    indice = Utils.Buscar_Por_Codigo(playlist, codigo)
    if not indice < 0:
        Utils.Imprimir_Diccionario(playlist[indice])
    else:
        print(f"No se encontro el codigo '{codigo}'")

# 8
def Listar_Por_Colaborador(playlist:list, nombre_colaborador:str):
    indices = Utils.Buscar_Por_Colaborador(playlist, nombre_colaborador)
    
    if not len(indices) < 0:
        for i in range(len(indices)):
            Utils.Imprimir_Diccionario(playlist[i])
    else:
        print(f"No se encontro el colaborador '{nombre_colaborador}'")
    print()

# 9                         
def Listar_Por_Mes_Lanzamiento():
    print()                                