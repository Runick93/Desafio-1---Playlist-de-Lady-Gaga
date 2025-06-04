from datetime import date

# Normalizacion de Datos.
def Get_Titulo(tema:str) -> str:
    titulo_retorno = "Titulo desconocido"

    partes = tema.split("-")
    if len(partes) > 1:
        titulo_retorno = partes[1].split(" ")[1]
    else: 
        titulo_retorno = partes[0]
    
    return titulo_retorno

def Get_Colaboradores(tema:str) -> str:
    colaboradores_retorno = "Lady Gaga"

    partes = tema.split("-")
    if len(partes) > 1:
        colaboradores_retorno = partes[0]

    return colaboradores_retorno

def Get_Vistas(vistas:str) -> int:
    vistas_retorno = 0

    partes = vistas.split(" ")
    if len(partes) > 0 or len(partes) <= 2:
        vistas_retorno = int(partes[0]) * 1000000

    return vistas_retorno

def Get_Duracion(duracion:str) -> int:
    duracion_retorno = 0
    partes = duracion.split(":")

    if len(partes) > 0 or len(partes) <= 2:
        minutos = int(partes[0])
        segundos = int(partes[1])
        duracion_retorno =  minutos * 60 + segundos     

    return duracion_retorno

def Get_FechaLanzamiento(fecha:str) -> date:
    
    partes = fecha.split("-")

    año = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])
    fecha_retorno = date(año, mes, dia)
    
    return fecha_retorno

# Ordenamientos.
def Ordenar_Temas(playlist:list, key:str, modo_ordenamiento = "desc") -> None:

    for i in range(0, len(playlist) - 1, 1):
        for j in range(i + 1, len(playlist), 1):
            dur_i = playlist[i][key]
            dur_j = playlist[j][key]
            
            # Ordenar por key ascendente o descendente
            if (dur_i > dur_j and modo_ordenamiento == "asc") or (dur_i < dur_j and modo_ordenamiento == "desc"):
                
                aux_nombre = playlist[i]
                playlist[i] = playlist[j]
                playlist[j] = aux_nombre


# Promedios
def Calcular_Promedio(playlist:list, key:str) -> float:

    cantidad_canciones = len(playlist)
    promedio = 0
    suma = 0

    for i in range(cantidad_canciones):
        vistas = playlist[i][key]
        suma = suma + vistas
    
    promedio = suma / cantidad_canciones

    return promedio


# Busquedas
def Buscar_Extremos(playlist:list, key:str, extremo:str = "min") -> list: 
    valor_extremo = None
    indices_encontrados = []

    for i in range(len(playlist)):
        if (valor_extremo == None) or (playlist[i][key] > valor_extremo and extremo == "max") or (playlist[i][key] < valor_extremo and extremo == "min"):
            valor_extremo = playlist[i][key]

    for i in range(len(playlist)):
        if playlist[i][key] == valor_extremo:
            indices_encontrados.append(i)

    return indices_encontrados

def Buscar_Por_Codigo(playlist:list, codigo_pedido:str) -> int:
    
    indice_tema = -1

    for i in range(len(playlist)):
        link_video = playlist[i]["link"]
        codigo_video = link_video[len(link_video) - 11 : len(link_video)]
        
        if codigo_video == codigo_pedido:
            indice_tema = i 
    
    return indice_tema

def Buscar_Por_Colaborador(playlist:list, nombre_colaborador:str) -> int:
    
    indices_tema= []

    for i in range(len(playlist)):
        colaboradores = playlist[i]["colaboradores"]
        nombres_colaboradores = colaboradores.split("|")
        
        for colaborador in range(len(nombres_colaboradores)):

            if colaborador == nombre_colaborador:
                indices_tema.append(i) 
    
    return indices_tema

    
# Imprimir
def Imprimir_Diccionario(diccionario: dict):
    keys = list(diccionario.keys())
    values = list(diccionario.values())

    for i in range(len(keys)):
        print(f"{keys[i]}: {values[i]}")
