''' Este programa cambia de formato un archivo dando informacion preveniente de dos archivos
El archivo resultante es un ASCII con nombre
Una disculpa si en los comentarios tengo faltas de ortografia, tengo un teclado en ingles y
Cambiar de Espanol a ingles se vuelve tedioso y desesperante'''
# Importando bibliotecas
#-----------------------------------------------------------------------------------------------------------------
'''Es necesario descargar la biblioteca Regex
La biblioteca os es para introducir comandos desde Python'''
import os
import re
import csv
import string
import time
#-----------------------------------------------------------------------------------------------------------------
# Se inicia el tiempo de medida del arraque del programa
ini = time.time()
# Limpiando pantalla
# Cambia dependiendo del SO
os.system ("cls")
#-----------------------------------------------------------------------------------------------------------------
'''Eliminando las lineas que tengan # y * del archivo copiado (Que son los comentarios)
Se ha dividido en dos porque una funcion borra los # y otra los *
La funcion pide un archivo de entrada
Nam_Neue_Arch: De preferencia que sea el archivo que se copio anteriormente para 
no modificar el original.
Nam_Alt_Arch: Es el nombre del archivo nuevo y con el que se estara trabajando'''
def EliminarAst(Nam_Neue_Arch, Nam_Alt_Arch):
    file1 = open(Nam_Neue_Arch, 'r')
    file2 = open(Nam_Alt_Arch, 'w')
    for line in file1.readlines():
        x = re.findall("\*", line)
        if not x:
            file2.write(line)
    file1.close()
    file2.close()
#-----------------------------------------------------------------------------------------------------------------
def EliminarGato(Nam_Neue_Arch, Nam_Alt_Arch):
    file1 = open(Nam_Neue_Arch, 'r')
    file2 = open(Nam_Alt_Arch, 'w')
    for line in file1.readlines():
        x = re.findall("#", line)
        if not x:
            file2.write(line)
    file1.close()
    file2.close()
#-----------------------------------------------------------------------------------------------------------------
# Esta funcion nos permite eliminar los espacios en blanco
def Leerraum(Nam_Neue_Arch, Nam_Alt_Arch):
    with open(Nam_Alt_Arch,'r') as fr:
        with open(Nam_Neue_Arch,'w') as fd:
            for text in fr.readlines():
                    if text.split():
                            fd.write(text)
    fr.close()
    fd.close()
#-----------------------------------------------------------------------------------------------------------------
''' Esta funcion se ha codificado debido a los efectos secundarios de la funcion anterior que nos permite 
identificar un Estado y reescribirlo con un determinado formato.
Esta funcion le quita el formato de lista y lo reescribe quitando las comas, parentesis y demas caracteres 
especiales'''
def Format(Nam_Neue_Arch, Nam_Alt_Arch):
    with open(Nam_Neue_Arch, 'r') as file1:
        with open(Nam_Alt_Arch, 'w') as file2:
            for line in file1.readlines():
                lines = line.split()
                # Se transforman las listas en string
                Strlines = str(lines)
                # Se eliminan signos de puntuacion que estan fuera de lugar
                file2.writelines(Strlines.translate(str.maketrans('', '', string.punctuation)) + '\n')
    file1.close()
    file2.close()
#-----------------------------------------------------------------------------------------------------------------
''' Esta función solo transforma un archivo ASCII a CSV 
Esta funcion ha sido elaborada para que sea mas facil extraer determinados datos'''
def ASCIIzuCSV(Alte_Archive, Archive_csv):
    # Esta parte ayuda a que cada carte separada por espacios quede dentro de una celda
    out = open(Archive_csv, 'w', newline = '')
    csv_writer = csv.writer(out, dialect='excel')
    f = open(Alte_Archive, 'r')
    for line in f.readlines():
        line = line.replace ('\ t', ',') # Remplazando cada espacio por una coma
        lista = line.split () #Convierta la cadena en una lista, para que pueda escribir csv por celda
        csv_writer.writerow(lista)
    f.close()
    out.close()
#-----------------------------------------------------------------------------------------------------------------
# Función para leer y guardar una determinada columna de algun archivo y guardarla como una lista
def Spalte(Archive, Position):
    with open(Archive, newline = '') as f:
         Stat = []
         for line in f:
             Stat.append(line)
    # /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
    # Convirtiendo cada renglon en una lista para despues seleccionar un determinado renglon
    # Leyendo un renglon del archivo que hemos cargado
    Neuen = []
    N = []
    for i in range(len(Stat)):
        Neuen = 0
        # Primero se lee cada elemento de la lista
        NeueListe = Stat[i]
        # Se transforma cada String en una Lista
        Neuen = NeueListe.split(',')
        # Se guarda la posicion especifica que se da en la funcion
        N.append(Neuen[Position])
    f.close()
    return N
#-----------------------------------------------------------------------------------------------------------------
'''Es una version mejorada de Spalte donde se puede tomar cualquier columna. En la version de Spalte teniamos el
problema que no se podian elegir columnas mayores a 3 porque a los ojos de python el resto de las casillas no existen, 
por que aquellas casillas 'inexistentes' fueron rellenados con espacios en blanco (' ') de esta manera si queremos 
columna 5 no habra error como en la version anterior'''
def Spalte_II(Archive, Saeule, n):
    le_archive = []
    # Esta parte nos permite abrir el archivo csv y leer cada linea como si fuera una lista
    with open(Archive) as File:
        reader = csv.reader(File, delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
        for row in reader:
            if len(row)<n: # n es la fila faltante para que sea del mismo tamano que el resto
                row.extend([' ']*6)
                le_archive.append(row)
            else:
                le_archive.append(row)
    ''' Finalemente la lista le_archive contiene el documento completo, los espacios vacios, como se mencionaba
     anteriormente fueron rellenados con espacios vacios para que asi pueda ser tomado cualquier columan de la lista 
     y no marque error como la definicion spaten.
    A continuacion vamos a cdificar como elegir solo una columna teniendo como resultado una multilista que en el valor
    de return tenemos un resultado de tipo lista'''
    rubrik = []
    for i in range(len(le_archive)):
        rubrik.append(le_archive[i][Saeule])
    return rubrik, le_archive
#-----------------------------------------------------------------------------------------------------------------
'''Esta definicion conveirte un ASCII aun CSV para que sea mas facil de extraer la informacion. 
Se ha emplado las definiciones anteriores.
 *******IMPORTANTE******** no se ha eliminado el archivo original y el archivo csv sera eliminado mas adelante
 para que solo quede en la carpeta los archivos originales y el archivo de salida que se ha pedido'''
def Archive(Archive_Eingang, Archive_csv):
    Arch_A = 'stalocs_A'
    Arch_B = 'stalocs_B'
    Arch_C = 'stalocs_C'
    Leerraum(Arch_A, Archive_Eingang)
    EliminarAst(Arch_A, Arch_B)
    EliminarGato(Arch_B, Arch_C)
    ASCIIzuCSV(Arch_C, Archive_csv)
    # Este comando cambia dependiendo del SO
    os.remove(Arch_A)
    os.remove(Arch_B)
    os.remove(Arch_C)
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
''' Se extraen las columnas de interes del archivo sitevecs
Debemos tener cuidado que ambos archivos tengan las mistas estaciones para obtener toda la informacion'''
def SiteVecs(Arch_C, Arch_D):
    # Se extraen las columnas de las estaciones junto a sus estados
    Sta_sts = Spalte(Arch_C, 0)
    Sta_sis = Spalte(Arch_D, 0)
    # Es el tamagno de las listas extraidas
    Grosse_Sta_sts = len(Sta_sts)
    Grosse_Sta_sis = len(Sta_sis)
    # -----------------------------------------------------------------------------------------------------------------
    # Se busca que elementos que ambos archivos tienen en comun para tener la mayor informacion posible de cada estacion
    # Y se acomodan de acuerdo al alrchivo con mas filas
    Gemeinsam = []
    for i in range(Grosse_Sta_sts):
        for j in range(Grosse_Sta_sis):
            if Sta_sis[j] in Sta_sts[i]:
                Gemeinsam.append(Sta_sis[j])
    # -----------------------------------------------------------------------------------------------------------------
    '''En esta parte hacemos una ,, enciclopedia" de las estaciones con las que contamos con toda la información
    posible'''
    # Eliminamos elementos repetidos, pero dejando el primer elemento en aparaecer
    Zusammen = []
    for item in Gemeinsam:
        if item not in Zusammen:
            Zusammen.append(item)
    # -----------------------------------------------------------------------------------------------------------------/
    i = 0
    together = []
    for i in range(len(Sta_sis)):
        if Sta_sis[i] in Zusammen:
            together.append(Sta_sis[i])
    # -----------------------------------------------------------------------------------------------------------------/
    '''Se hacen varias listas:
    Stati: Es la lista que contiene tanto las fechas (marcadas como un asterisco) como las estaciones
    Buch: Solo contiene las estaciones
    Datum: Contiene las fechas'''
    i = 0
    Stati = []
    Buch = []
    Datum = []
    for i in range(len(Sta_sis)):
        if Sta_sis[i] in together:
            Stati.append(Sta_sis[i])
            Buch.append(Sta_sis[i])
        else:
            Stati.append('*')
            Datum.append(Sta_sis[i])
    # Se calcula los idices de los valores que no corresponden a las estaciones para el resto de la informacion
    j = 0
    Skale = []
    for j in range(len(Datum)):
        if Datum[j] in Sta_sis:
            Ska = Sta_sis.index(Datum[j])
            Skale.append(Ska)
    # Skale es la lista donde se guarda el resto de las posiciones
    # -----------------------------------------------------------------------------------------------------------------
    '''Se busca el indice de cada una de las estaciones ya partidas las listas. 
    Tener cuidado de esta parte. en caso de no tener elementos repetidos mas adelante se omite divir las lista y se 
    modifica lo que esta codificado a continuacion'''
    i = 0
    St_1 = []
    for i in range(len(Buch)):
        Sta_1 = Sta_sis.index(Buch[i])
        St_1.append(Sta_1+1)
    St_1.append(St_1[-1]+2)
    '''Se han unido ambas lista por lo que ahora resta agregar otro lugar, creando una "Estacion fantasma" que nos 
    permitira calcular cuantas veces se debera repetir la estacion'''
    # -----------------------------------------------------------------------------------------------------------------
    '''Para calcular cuantas veces se repite una estacion se usa a continuacion (cuando se suma se hace referencia a 
    la posicion): (estacion+1 - estacion)-1'''
    i = 0
    j = 0
    Station = []
    for i in range(len(St_1)-1):
        Zahl = ((St_1[i+1] - St_1[i])-1)
        Station.extend([Buch[i]] * Zahl)
    # Con esto tenemos la lista de las estaciones
    # -----------------------------------------------------------------------------------------------------------------
    '''En esta parte se va extraer la informacion de las antenas, sin embargo, como se encunetran en varias columnas
    del csv, se pinsa extraer columna por columna y unirlo'''
    # Se extrae las columnas que contienen las antenas
    ANT_0 = Spalte_II(Arch_D, 5, 9)[0]
    ANT_1 = Spalte_II(Arch_D, 6, 9)[0]
    ANT_2 = Spalte_II(Arch_D, 7, 9)[0]
    ANT_3 = Spalte_II(Arch_D, 8, 9)[0]
    '''Primero se introduce elemento a elemento de cada lista y se pasa a una cadena y se separa por comas. Despues
    se guarda en una lista de esta manera se juntan las tres casillas y se guardan en una lista'''
    i = 0
    ANT_Zussamen = []
    for i in range(len(ANT_1)):
        ANT_Wor = ANT_0[i]
        ANT_Zussamen.append(ANT_Wor)
    j = 0
    ANT = []
    for j in range(len(Skale)):
        s = Skale[j]
        ant = ANT_Zussamen[s]
        ANT.append(ant)
    '''Con Skale que es la posicion del resto de las estaciones en las que no se encuentra las estaciones ni los 
    espacios en blanco, se ha extraido el nombre de las enatenas. Se ha hecho de esta manera porque existen espacios 
    en blanco en la columna de las antenas'''
    # ------------------------------------------------------------------------------------------------------------------
    # Se hace lo mismo para extraer el tipo de antena
    i = 0
    ANT_Zus= []
    for i in range(len(ANT_1)):
        ANT_Zus.append(ANT_2[i] + ' ' + ANT_3[i])
    j = 0
    ANT_type = []
    for j in range(len(Skale)):
        s = Skale[j]
        ant_type = ANT_Zus[s]
        ANT_type.append(ant_type)
    # ------------------------------------------------------------------------------------------------------------------
    # Se hace los mismo (como en las antenas) con su localizacion
    E = Spalte_II(Arch_D, 2, 9)[0]
    N = Spalte_II(Arch_D, 3, 9)[0]
    V = Spalte_II(Arch_D, 4, 9)[0]
    i = 0
    s = 0
    e = []
    n = []
    v = []
    for i in range(len(Skale)):
        s = Skale[i]
        Standpunkt_e = E[s]
        Standpunkt_n = N[s]
        Standpunkt_v = V[s]
        e.append(Standpunkt_e)
        n.append(Standpunkt_n)
        v.append(Standpunkt_v)
    # ------------------------------------------------------------------------------------------------------------------
    # Ahora se extrae el RX de la misma manera que los casos anteriores
    rx = Spalte_II(Arch_D, 1, 9)[0]
    i = 0
    s = 0
    RX = []
    for i in range(len(Skale)):
        s = Skale[i]
        r = rx[s]
        RX.append(r)
    # ------------------------------------------------------------------------------------------------------------------
    # Se extrae las listas con la informacion que se busca
    return Station, Datum, ANT, e, n, v, RX, Skale, Buch, ANT_type
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
def StaLocs(Arch_C):
    # Extrayendo los monumentos
    Denkmal = Spalte_II(Arch_C, 1, 4)[0]
    # Extrayendo las estaciones
    Station = Spalte_II(Arch_C, 0, 4)[0]
    # Extrayendo la posicion de las antenas
    x = Spalte_II(Arch_C, 3, 4)[0]
    y = Spalte_II(Arch_C, 4, 4)[0]
    z = Spalte_II(Arch_C, 5, 9)[0]
    return Station, Denkmal, x, y, z,
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
'''Con toda la informacion extraida anteriormente se llama en esta funcion para ensamblar hacer cada parte del documento
que se nos pide.Cada funcion tienen nombre de lo pedido en el archivo StaDbFormat'''
def KEYBOARDS():
    key = ['KEYBOARDS: ' + 'ANT' + ' ID' + ' RX' + ' STATE' ]
    return key
# ---------------------------------------------------------------------------------------------------------------------
def ID(Arch_C, Arch_D):
    # Se extraen las estaciones del archivo Stalocs y se ordenan alfabeticamente para que no haya problema en acomodar
    # todo nuevamente
    Buch = SiteVecs(Arch_C, Arch_D)[8]
    i = 0
    station = []
    for i in range(len(Buch)):
        station.append(str(Buch[i] + ' ID Mexico'))
    Ort = sorted(station)
    return Ort
# ---------------------------------------------------------------------------------------------------------------------
def STATE (Arch_C, Arch_D):
    # Se extrae la informacion del archivo StaLocs
    station_L, monument, x, y, z = StaLocs(Arch_C)
    station_V, date, ant, e, n, v, rx, skale, buch, ant_type = SiteVecs(Arch_C, Arch_D)
    # ------------------------------------------------------------------------------------------------------------------
    i, j = 0, 0
    state = []
    for i in range(len(station_L)):
        for j in range(len(station_V)):
            # Solo para las estaciones en las que se coicide ambos archivos se toma en cuenta
            if sorted(station_V[j]) == sorted(station_L[i]):
                state.append(station_V[j] + ' STATE ' + date[j] + ' ' + rx[j] + ' ' + x[i] + ' ' + y[i] + ' ' + z[i] + ' 0')
    State = sorted(state)
    return State
# ---------------------------------------------------------------------------------------------------------------------
def ANT(Arch_C, Arch_D):
    # Extraemos la informacion del archivo sitevecs
    station, date, ant, e, n, v, rx, skale, buch, ant_type = SiteVecs(Arch_C, Arch_D)
    # Se guarda toda la informacion en forma de diccionario
    # Primero quitamos el signo de '+', '_' y de '-' de la informacion que se ha extraido de las antenas porque lo que sigue
    #despues de esos simbolos son el radome
    a = []
    for i in range(len(ant)):
        a.append(ant[i].replace("+", " "))
    an = []
    for j in range(len(a)):
        an.append(a[j].replace("-", " "))
    Ant = []
    i = 0
    for i in range(len(an)):
        Ant.append(an[i].replace("_", " "))
    i, j = 0, 0
    ANT = []
    for i in range(len(station)):
        for j in range(len(buch)):
            if sorted(station[i]) == sorted(buch[j]):
                ANT.append(station[i] + ' ANT ' + date[i] + ' ' + rx[i] + ' ' + Ant[i] + ' ' + e[i] + ' ' + n[i] + ' ' + v[i])
    ant = sorted(ANT)
    return ant
# ---------------------------------------------------------------------------------------------------------------------
def RX(Arch_C, Arch_D):
    # Extraemos la informacion del archivo sitevecs
    station, date, ant, e, n, v, rx, skale, buch, ant_type = SiteVecs(Arch_C, Arch_D)
    RX = []
    for i in range(len(station)):
        for j in range(len(buch)):
            if sorted(station[i]) == sorted(buch[j]):
                RX.append(station[i] + ' RX ' + date[i] + ' ' + rx[i] + ' ' + ant_type[i])
    Rx = sorted(RX)
    return Rx
# ---------------------------------------------------------------------------------------------------------------------
# Ahora a escribir todo dentro de un archivo ASCII
def Schreiben(Arch_C, Arch_D):
    key = KEYBOARDS()
    id = ID(Arch_C, Arch_D)
    state = STATE(Arch_C, Arch_D)
    ant = ANT(Arch_C, Arch_D)
    rx = RX(Arch_C, Arch_D)
    # Abriendo el archivo
    with open('staDb_sifs', 'w') as f:
        item = 0
        for item in id:
            f.write("%s\n" % item)
        item = 0
        for item in state:
            f.write("%s\n" % item)
        item = 0
        for item in ant:
            f.write("%s\n" % item)
        item = 0
        for item in rx:
            f.write("%s\n" % item)
    f.close()
    # ------------------------------------------------------------------------------------------------------------------
    # Se abre el archivo para poder ordenarlo de como se ha colocado en KEYBOARDS
    file  = open('staDb_sifs')
    Ordnung = file.readlines()
    Ordnung.sort()
    # ------------------------------------------------------------------------------------------------------------------
    # Se abre nuevamente el mismo archivo para sustituirlo y poder escribir sobre el mismo
    with open('staDb_sifs', 'w') as f:
        item = 0
        for item in key:
            f.write("%s\n" % item)
        item = 0
        for item in Ordnung:
            f.write("%s" % item)
    f.close()
# ---------------------------------------------------------------------------------------------------------------------
def staDb_sifs(Arch_A, Arch_B):
    # Esto es por default
    Arch_C = 'CSVstalocs.csv'
    Arch_D = 'CSVsitevecs.csv'
    Archive(Arch_A, Arch_C)
    Archive(Arch_B, Arch_D)
    Schreiben(Arch_C, Arch_D)
    os.remove('CSVstalocs.csv')
    os.remove('CSVsitevecs.csv')
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------
''' En el programa principal solo se debe introducio el nombre los archivos'''
#############################################################
#############################################################
### -----------   Es el progrma pincipal   -------------- ###
###                                                       ###
Arch_A = 'stalocs'                                        ###
Arch_B = 'sitevecs'                                       ###
staDb_sifs(Arch_A, Arch_B)                                ###
###                                                       ###
#---------------------------------------------------------###
#############################################################
#############################################################
#-----------------------------------------------------------------------------------------------------------------
fin = time.time()
print('Tiempo en ejecutar el programa: ', fin-ini, 'seg')