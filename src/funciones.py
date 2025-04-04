vocales = ("a","e","i","o","u","A","E","I","O","U")
def verificaVocal(oracion):
    #hacemos una lista de la oracion, separada por " "
    palabras = oracion.split(" ")
    #devolvemos el valor de si la 2da palabra empieza con vocals
    return (palabras[1][0] in vocales)

def imprimir_oracion(oracion):
    #se transforma el str en un lista
    listaDeOraciones = oracion.split("\n")
    #recorremos las oraciones y hacemos la impresion de las que cumplas que su 2da palabra empiece con vocal 
    [print(x)for x in listaDeOraciones if (verificaVocal(x))]

def imprimir_tituloMax(titles):
    max = ""
    for x in titles:
        if (len(x)> len(max)):
            max = x
    return max
 
def imprimir_round(jugadores, mvps):
    print('-'*25)
    jugadores_ordenados = sorted(jugadores, key=lambda item: item[1]['points'], reverse=True)
    print(f"jugadores Kills Asistencias muerte Mvps puntaje".center(10))
    for jugador,dato in jugadores_ordenados:
        print(f"{jugador} {dato['kills']} {dato['assists']} {mvps[jugador]} {dato['points']}".center(10))

def sumarDatos(jugador, datos, contador_total):
    for indice, dato in datos.items():
        contador_total[jugador][indice] += dato
def imprimir_ejercicio10(rounds):
    #se inicializa el contabilizacion de los MVPS
    mvps = {'Shadow':0, 'Blaze':0,'Viper': 0,'Frost': 0,'Reaper':0}
    contador_total ={ 'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'points':0},
                        'Blaze': {'kills': 0, 'assists': 0, 'deaths':0, 'points':0},
                        'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'points':0},
                        'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'points':0},
                        'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'points':0}
                    }
    for i,round in enumerate(rounds,start = 1):
        print(f"ronda {i}")
        best_name = " "
        best_points = -2
        for jugador,datos in round.items():
            datos['points'] = datos['kills']*3 + datos['assists'] + (-1 if datos['deaths'] else 0)
            if datos['points'] > best_points:
                best_name = jugador
                best_points = datos['points']
            sumarDatos(jugador,datos,contador_total)
        mvps[best_name] += 1
        imprimir_round(round.items(),mvps)
    print("ranking final") 
    imprimir_round(contador_total.items(),mvps)
        
       
    


