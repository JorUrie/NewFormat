'''Este programa lee un archivo y determina su generacion y bloque. Esto lo logra leyendo otro archivo'''
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Exportando bibliotecas
import os
import csv
import string
import tabulate
from termcolor import colored
import time
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Se inicia el tiempo de medida del arraque del programa
ini = time.time()
# Limpiando pantalla
# Cambia dependiendo del SO
os.system ("cls")
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Haciendo una funcion para llamar a un archivo y eliminar los ecabezados pero compiandolo en un nuevo archivo
# Kopfzeile es el numero de renglones que tiene como encabezado
def Lire(Archive, Archive_1, Kopfzeile):
    file1 = open(Archive, 'r')
    file2 = open(Archive_1, 'w')
    # Se lee el archivo de entrada considerando que cada renglon es una lista
    Archive = []
    for linea in file1.readlines():
        lines = linea.split()
        Archive.append(lines)
    for i in range(Kopfzeile, len(Archive), 1):
        file2.write(str(Archive[i]).translate(str.maketrans(' ', ' ', string.punctuation)) + '\n')
    file1.close()
    file2.close()
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# El fichero se transforma en un CSV
''' Esta función solo transforma un archivo ASCII a CSV 
Esta funcion ha sido elaborada para que sea mas facil extraer determinados datos'''
def ASCIIzuCSV(Archive_ASCII, Archive_CSV):
    # Esta parte ayuda a que cada carte separada por espacios quede dentro de una celda
    out = open(Archive_CSV, 'w', newline = '')
    csv_writer = csv.writer(out, dialect = 'excel')
    f = open(Archive_ASCII, 'r')
    for line in f.readlines():
        line = line.replace(',', ' ') # Remplazando cada espacio por una coma
        lista = line.split() #Convierta la cadena en una lista, para que pueda escribir csv por celda
        csv_writer.writerow(lista)
    f.close()
    out.close()
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Con esta funcion se extrae una columna determinada de un archivo CSV
def Kolumne(Archive, Saeule):
    le_archive = []
    # Esta parte nos permite abrir el archivo csv y leer cada linea como si fuera una lista
    with open(Archive) as File:
        reader = csv.reader(File, delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
        for row in reader:
            if len(row) == 2:
                row.insert(0, ' ')
            if len(row) < 8: # n es la fila faltante para que sea del mismo tamano que el resto
                row.extend([' ']*7)
                le_archive.append(row)
            else:
                le_archive.append(row)
    ''' A continuacion vamos a codificar como elegir solo una columna teniendo como resultado una multilista que en el 
    valor de return tenemos un resultado de tipo lista'''
    rubrik = []
    for i in range(len(le_archive)):
        rubrik.append(le_archive[i][Saeule])
    Aufbau = []
    for j in range(len(rubrik)):
        if rubrik[j] == ' ' or rubrik[j] == '':
            Aufbau.append('0')
        else:
            Aufbau.append(rubrik[j])
    return Aufbau, rubrik, le_archive
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
''' Aqui se ejecutan las funciones para extraer la infomacion del archivo tmig262-.22o
Eintrag_Archive: Es el archivo de entrada, con el que el usuario cuenta
Ausgabe_Archive: Es el archivo de salida sin encabezados
Arbeite_Archive: Es el archivo CSV y sin encabzados del que se extrae la informacion
n: Es el numero de columna que se quiere extraer '''
def tmig(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, n):
    Lire(Eintrag_Archive, Ausgabe_Archive, 24)
    ASCIIzuCSV(Ausgabe_Archive, Arbeite_Archive)
    liste = Kolumne(Arbeite_Archive, n)[0]
    os.remove(Ausgabe_Archive)
    return liste
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
''' Aqui se ejecutan las funciones para extraerr la infomacion del archivo PRN_GPS.unknown
Eintrag_Archive: Es el archivo de entrada, con el que el usuario cuenta
Ausgabe_Archive: Es el archivo de salida sin encabezados
Arbeite_Archive: Es el archivo CSV y sin encabzados del que se extrae la informacion
n: Es el numero de columna que se quiere extraer '''
def PRN(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, n):
    Lire(Eintrag_Archive, Ausgabe_Archive, 1)
    ASCIIzuCSV(Ausgabe_Archive, Arbeite_Archive)
    liste = Kolumne(Arbeite_Archive, n)[0]
    os.remove(Ausgabe_Archive)
    return liste
# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Esta funcion verifica si no hay elementos repidos sobre la misma lista
def Vergleich(Vektor):
    Einheits = []
    for Vektor in Vektor:
        if Vektor not in Einheits:
            Einheits.append(Vektor)
    return Einheits
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Nombres de los archivos creados
Archive_1 = 'tmig2620.22o'
Archive_2 = 'Archive_SK_RINEX'
Archive_3 = 'Archive_CSV_RINEX.csv'
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
Archive_4 = 'PRN_GPS.unknown'
Archive_5 = 'Archive_SK_GPS'
Archive_6 = 'Archive_CSV_GPS.csv'
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
''' Se extrae las columnas e informacion necesaria del archivo tmig2620.22o'''
def Signal(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive):
    # Se extrae la cantidad, PRN y tipo del vector de donde se encuentra la informacion
    G = tmig(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, 7)
    Position_G = []
    Kette = []
    for i in range(len(G)):
        if G[i] != '0':
            Position_G.append(i)
            Kette.append(G[i])
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Cambiando formato de la informacion extraida
    Neue_Kette = []
    for j in range(len(Kette)):
        Neue_Kette.append(Kette[j][0: 1] + ' ' + Kette[j][1:4] + ' ' + Kette[j][4:7] + ' ' + Kette[j][7:10] + ' ' +
            Kette[j][10:13] + ' ' + Kette[j][13:16] + ' ' + Kette[j][16:19] + ' ' + Kette[j][19:22])
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Se verifica si se repiten los tipos de lectura
    Abstand = Vergleich(Neue_Kette)
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Se une la lista anterior en una misma
    Verbunden = ' '.join(Abstand)
    Vereint = Verbunden.split(' ')
    Ohne_Wiederholung = Vergleich(Vereint)
    ###############################
    Ohne_Wiederholung.remove('6') # Tener cuidado en esta parte, se puede cambiar, agregar o lo que se mas conveniente
    Ohne_Wiederholung.remove('7') #
    Ohne_Wiederholung.pop(6)      # Se elimina un elemento que aparecia a continuacion: ''
    ###############################
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    return Ohne_Wiederholung, Kette, Position_G, Abstand
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Idenificando la generacion del satelite de acuerdo al bloque y la fecha. La informacion se obtiene del archivo
# PRN_GPS.unknown.
def Aendern(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive):
    GPS = Signal(Archive_1, Archive_2, Archive_3)[0]
    Date_1 = PRN(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, 0)
    Date_2 = PRN(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, 1)
    prn = PRN(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, 3)
    Block = PRN(Eintrag_Archive, Ausgabe_Archive, Arbeite_Archive, 4)
    Data = []
    for i in range(len(Date_1)):
        if Block[i] == 'IIA' or Block[i] == 'IIR' or int(Date_1[i][0: 4]) < 2005:
            Data.append(
                Date_1[i][0: 4] + '-' + Date_1[i][4: 6] + '-' + Date_1[i][6: 8] + ' ' + Date_2[i][0: 4] + '-' + Date_2[
                    i][4: 6] + '-' + Date_2[i][6: 8] + ' ' + 'G' + prn[i] + ' ' + Block[i] + ' ' + 'Legacy')
        else:
            Data.append(
                Date_1[i][0: 4] + '-' + Date_1[i][4: 6] + '-' + Date_1[i][6: 8] + ' ' + Date_2[i][0: 4] + '-' + Date_2[
                    i][4: 6] + '-' + Date_2[i][6: 8] + ' ' + 'G' + prn[i] + ' ' + Block[i] + ' ' + 'Modernized')
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    i = 0
    Information = []
    for i in range(len(GPS)):
        for j in range(len(Data)):
            if GPS[i] in Data[j]:
                Information.append(Data[j])
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    j = 0
    Formular = []
    for j in range(len(Information)):
        Formular.append(Information[j].split(' '))
    Formular.insert(0, [colored('Launch Date', 'light_magenta'), colored('Deactiv. Date', 'light_magenta'),
        colored('PRN', 'light_magenta'), colored('Block', 'light_magenta'), colored('Generation', 'light_magenta')])
    print(colored('\n \t La información con la se cuenta es como se muestra en la tabla a continuación: \n', 'light_red',
        attrs = ['dark']))
    print(tabulate.tabulate(Formular, headers = 'firstrow'))
    print(colored('\n \t NOTA: Las señales contenidas son: L1, L2, C1, P1, C2, P2, S1, S2 \n \t \t En la fecha: 19/09/22'
        ' tomando una muestra cada 2 seg. \n', 'light_blue'))
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
# Esta funcion nos permite escribir una lista en un archivo ASCII
def Schreiben(Lese, prn, Liste):
    Name = Lese + '_' + str(prn)
    with open(Name, 'w') as f:
        for item in Liste:
            f.write("%f\n" % item)
    f.close()
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
def Herkunft(Lesezeichen, PRN):
    Kette = Signal(Archive_1, Archive_2, Archive_3)[1]  # Muestra los encabezados y el resto es '0'
    Position = Signal(Archive_1, Archive_2, Archive_3)[2]   # Es la posicion en la que se ubican los encabezados
    Bibliothek = Vergleich(Kette)   # Es para saber cuantos tipos de encabezados hay
    #print(Bibliothek)
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Extrayendo todos los vectores del archivo tming que seran necesarios
    T1 = tmig(Archive_1, Archive_2, Archive_3, 0)
    T2 = tmig(Archive_1, Archive_2, Archive_3, 1)
    T3 = tmig(Archive_1, Archive_2, Archive_3, 2)
    T4 = tmig(Archive_1, Archive_2, Archive_3, 3)
    T5 = tmig(Archive_1, Archive_2, Archive_3, 4)
    #print(Position)
    # Sustituyendo los renglones donde se tiene el encabezado del tipo de lecturas (para eso se ha extraido la posicion)
    for i in range(len(Kette)):
        T1[Position[i]] = Kette[i]
        T2[Position[i]] = Kette[i]
        T3[Position[i]] = Kette[i]
        T4[Position[i]] = Kette[i]
        T5[Position[i]] = Kette[i]
    #print(T1)
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Extreyendo la informacion
    '''Lamentablemente como se tienen diferentes encabezados, si se cambia de archivos se tiene que cambiar esta parte
    del codigo para que funcione adecuandamente. 
    En esta parte se da un encabezado y tomando en cuenta esta informacion se busca el renglon y la informacion que se 
    desea porque depende del encabezado'''
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    if Lesezeichen == 'L1' and PRN == 22:
        t0 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t0.append(float(T1[i+1])*0.00001)
            if T1[i] == Bibliothek[1]:
                t0.append(float(T1[i+3])*0.00001)
            if T1[i] == Bibliothek[2]:
                t0.append(float(T1[i+1])*0.00001)
            if T1[i] == Bibliothek[3]:
                t0.append(float(T1[i+1])*0.00001)
            if T1[i] == Bibliothek[4]:
                t0.append(float(T1[i+1])*0.00001)
        return t0
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 22:
        t1 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t1.append(float(T2[i+1])*0.00001)
            if T2[i] == Bibliothek[1]:
                t1.append(float(T2[i+3])*0.00001)
            if T2[i] == Bibliothek[2]:
                t1.append(float(T2[i+1])*0.00001)
            if T2[i] == Bibliothek[3]:
                t1.append(float(T2[i+1])*0.00001)
            if T2[i] == Bibliothek[4]:
                t1.append(float(T2[i+1])*0.00001)
        return t1
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 22:
        t2 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t2.append(float(T3[i+1])*0.0001)
            if T3[i] == Bibliothek[1]:
                t2.append(float(T3[i+3])*0.0001)
            if T3[i] == Bibliothek[2]:
                t2.append(float(T3[i+1])*0.0001)
            if T3[i] == Bibliothek[3]:
                t2.append(float(T3[i+1])*0.0001)
            if T3[i] == Bibliothek[4]:
                t2.append(float(T3[i+1])*0.0001)
        return t2
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 22:
        t3 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t3.append(float(T4[i+1])*0.00001)
            if T4[i] == Bibliothek[1]:
                t3.append(float(T4[i+3])*0.00001)
            if T4[i] == Bibliothek[2]:
                t3.append(float(T4[i+1])*0.00001)
            if T4[i] == Bibliothek[3]:
                t3.append(float(T4[i+1])*0.00001)
            if T4[i] == Bibliothek[4]:
                t3.append(float(T4[i+1])*0.00001)
        return t3
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 22:
        t4 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t4.append(float(T5[i+1])*0.0001)
            if T5[i] == Bibliothek[1]:
                t4.append(float(T5[i+3])*0.0001)
            if T5[i] == Bibliothek[2]:
                t4.append(float(T5[i+1])*0.0001)
            if T5[i] == Bibliothek[3]:
                t4.append(float(T5[i+1])*0.0001)
            if T5[i] == Bibliothek[4]:
                t4.append(float(T5[i+1])*0.0001)
        return t4
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 22:
        t5 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t5.append(float(T1[i+2])*0.00001)
            if T1[i] == Bibliothek[1]:
                t5.append(float(T1[i+4])*0.00001)
            if T1[i] == Bibliothek[2]:
                t5.append(float(T1[i+2])*0.00001)
            if T1[i] == Bibliothek[3]:
                t5.append(float(T1[i+2])*0.00001)
            if T1[i] == Bibliothek[4]:
                t5.append(float(T1[i+2])*0.00001)
        return t5
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 22:
        t6 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t6.append(float(T2[i+2])*0.0001)
            if T2[i] == Bibliothek[1]:
                t6.append(float(T2[i+4])*0.0001)
            if T2[i] == Bibliothek[2]:
                t6.append(float(T2[i+2])*0.0001)
            if T2[i] == Bibliothek[3]:
                t6.append(float(T2[i+2])*0.0001)
            if T2[i] == Bibliothek[4]:
                t6.append(float(T2[i+2])*0.0001)
        return t6
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 22:
        t7 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t7.append(float(T3[i+2])*0.0001)
            if T3[i] == Bibliothek[1]:
                t7.append(float(T3[i+4])*0.0001)
            if T3[i] == Bibliothek[2]:
                t7.append(float(T3[i+2])*0.0001)
            if T3[i] == Bibliothek[3]:
                t7.append(float(T3[i+2])*0.0001)
            if T3[i] == Bibliothek[4]:
                t7.append(float(T3[i+2])*0.0001)
        return t7
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 23:
        t8 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t8.append(float(T1[i + 3]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t8.append(float(T1[i + 5]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t8.append(float(T1[i + 3]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t8.append(float(T1[i + 3]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t8.append(float(T1[i + 3]) * 0.00001)
        return t8
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 23:
        t9 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t9.append(float(T1[i + 3]) * 0.00001)
            if T2[i] == Bibliothek[1]:
                t9.append(float(T1[i + 5]) * 0.00001)
            if T2[i] == Bibliothek[2]:
                t9.append(float(T1[i + 3]) * 0.00001)
            if T2[i] == Bibliothek[3]:
                t9.append(float(T1[i + 3]) * 0.00001)
            if T2[i] == Bibliothek[4]:
                t9.append(float(T1[i + 3]) * 0.00001)
        return t9
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 23:
        t10 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t10.append(float(T3[i + 3]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t10.append(float(T3[i + 5]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t10.append(float(T3[i + 3]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t10.append(float(T3[i + 3]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t10.append(float(T3[i + 3]) * 0.0001)
        return t10
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 23:
        t11 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t11.append(float(T4[i + 3]) * 0.00001)
            if T4[i] == Bibliothek[1]:
                t11.append(float(T4[i + 5]) * 0.00001)
            if T4[i] == Bibliothek[2]:
                t11.append(float(T4[i + 3]) * 0.00001)
            if T4[i] == Bibliothek[3]:
                t11.append(float(T4[i + 3]) * 0.00001)
            if T4[i] == Bibliothek[4]:
                t11.append(float(T4[i + 3]) * 0.00001)
        return t11
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 23:
        t12 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t12.append(float(T5[i + 3]) * 0.0001)
            if T5[i] == Bibliothek[1]:
                t12.append(float(T5[i + 5]) * 0.0001)
            if T5[i] == Bibliothek[2]:
                t12.append(float(T5[i + 3]) * 0.0001)
            if T5[i] == Bibliothek[3]:
                t12.append(float(T5[i + 3]) * 0.0001)
            if T5[i] == Bibliothek[4]:
                t12.append(float(T5[i + 3]) * 0.0001)
        return t12
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 23:
        t13 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t13.append(float(T1[i + 4]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t13.append(float(T1[i + 6]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t13.append(float(T1[i + 4]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t13.append(float(T1[i + 4]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t13.append(float(T1[i + 4]) * 0.00001)
        return t13
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 23:
        t14 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[0]:
                t14.append(float(T2[i + 4]) * 0.0001)
            if T2[i] == Bibliothek[1]:
                t14.append(float(T2[i + 6]) * 0.0001)
            if T2[i] == Bibliothek[2]:
                t14.append(float(T2[i + 4]) * 0.0001)
            if T2[i] == Bibliothek[3]:
                t14.append(float(T2[i + 4]) * 0.0001)
            if T2[i] == Bibliothek[4]:
                t14.append(float(T2[i + 4]) * 0.0001)
        return t14
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 23:
        t15 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t15.append(float(T3[i + 4]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t15.append(float(T3[i + 6]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t15.append(float(T3[i + 4]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t15.append(float(T3[i + 4]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t15.append(float(T3[i + 4]) * 0.0001)
        return t15
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 29:
        t16 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t16.append(float(T1[i + 5]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t16.append(float(T1[i + 7]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t16.append(float(T1[i + 7]) * 0.00001)
        return t16
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 29:
        t17 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t17.append(float(T1[i + 5]) * 0.00001)
            if T2[i] == Bibliothek[1]:
                t17.append(float(T1[i + 7]) * 0.00001)
            if T2[i] == Bibliothek[2]:
                t17.append(float(T1[i + 7]) * 0.00001)
        return t17
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 29:
        t18 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t18.append(float(T3[i + 5]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t18.append(float(T3[i + 7]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t18.append(float(T3[i + 7]) * 0.0001)
        return t18
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 29:
        t19 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t19.append(float(T4[i + 5]) * 0.00001)
            if T4[i] == Bibliothek[1]:
                t19.append(float(T4[i + 7]) * 0.00001)
            if T4[i] == Bibliothek[2]:
                t19.append(float(T4[i + 7]) * 0.00001)
        return t19
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 29:
        t20 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t20.append(float(T5[i + 5]) * 0.0001)
            if T5[i] == Bibliothek[1]:
                t20.append(float(T5[i + 7]) * 0.0001)
            if T5[i] == Bibliothek[2]:
                t20.append(float(T5[i + 7]) * 0.0001)
        return t20
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 29:
        t21 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t21.append(float(T1[i + 6]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t21.append(float(T1[i + 8]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t21.append(float(T1[i + 8]) * 0.00001)
        return t21
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 29:
        t22 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[0]:
                t22.append(float(T2[i + 6]) * 0.0001)
            if T2[i] == Bibliothek[1]:
                t22.append(float(T2[i + 8]) * 0.0001)
            if T2[i] == Bibliothek[2]:
                t22.append(float(T2[i + 8]) * 0.0001)
        return t22
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 29:
        t23 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t23.append(float(T3[i + 6]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t23.append(float(T3[i + 8]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t23.append(float(T3[i + 8]) * 0.0001)
        return t23
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 18:
        t24 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t24.append(float(T1[i + 7]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t24.append(float(T1[i + 9]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t24.append(float(T1[i + 9]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t24.append(float(T1[i + 7]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t24.append(float(T1[i + 7]) * 0.00001)
        return t24
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 18:
        t25 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t25.append(float(T1[i + 7]) * 0.00001)
            if T2[i] == Bibliothek[1]:
                t25.append(float(T1[i + 9]) * 0.00001)
            if T2[i] == Bibliothek[2]:
                t25.append(float(T1[i + 9]) * 0.00001)
            if T2[i] == Bibliothek[3]:
                t25.append(float(T1[i + 7]) * 0.00001)
            if T2[i] == Bibliothek[4]:
                t25.append(float(T1[i + 7]) * 0.00001)
        return t25
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 18:
        t26 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t26.append(float(T3[i + 7]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t26.append(float(T3[i + 9]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t26.append(float(T3[i + 9]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t26.append(float(T3[i + 7]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t26.append(float(T3[i + 7]) * 0.0001)
        return t26
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 18:
        t27 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t27.append(float(T4[i + 7]) * 0.00001)
            if T4[i] == Bibliothek[1]:
                t27.append(float(T4[i + 9]) * 0.00001)
            if T4[i] == Bibliothek[2]:
                t27.append(float(T4[i + 9]) * 0.00001)
            if T4[i] == Bibliothek[3]:
                t27.append(float(T4[i + 7]) * 0.00001)
            if T4[i] == Bibliothek[4]:
                t27.append(float(T4[i + 7]) * 0.00001)
        return t27
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 18:
        t28 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t28.append(float(T5[i + 7]) * 0.0001)
            if T5[i] == Bibliothek[1]:
                t28.append(float(T5[i + 9]) * 0.0001)
            if T5[i] == Bibliothek[2]:
                t28.append(float(T5[i + 9]) * 0.0001)
            if T5[i] == Bibliothek[3]:
                t28.append(float(T5[i + 7]) * 0.0001)
            if T5[i] == Bibliothek[4]:
                t28.append(float(T5[i + 7]) * 0.0001)
        return t28
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 18:
        t29 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t29.append(float(T1[i + 8]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t29.append(float(T1[i + 10]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t29.append(float(T1[i + 10]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t29.append(float(T1[i + 8]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t29.append(float(T1[i + 8]) * 0.00001)
        return t29
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 18:
        t30 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[0]:
                t30.append(float(T2[i + 8]) * 0.0001)
            if T2[i] == Bibliothek[1]:
                t30.append(float(T2[i + 10]) * 0.0001)
            if T2[i] == Bibliothek[2]:
                t30.append(float(T2[i + 10]) * 0.0001)
            if T2[i] == Bibliothek[3]:
                t30.append(float(T2[i + 8]) * 0.0001)
            if T2[i] == Bibliothek[4]:
                t30.append(float(T2[i + 8]) * 0.0001)
        return t30
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 18:
        t31 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t31.append(float(T3[i + 8]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t31.append(float(T3[i + 10]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t31.append(float(T3[i + 10]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t31.append(float(T3[i + 8]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t31.append(float(T3[i + 8]) * 0.0001)
        return t31
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 10:
        t32 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t32.append(float(T1[i + 9]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t32.append(float(T1[i + 11]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t32.append(float(T1[i + 11]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t32.append(float(T1[i + 9]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t32.append(float(T1[i + 11]) * 0.00001)
        return t32
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 10:
        t33 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t33.append(float(T1[i + 9]) * 0.00001)
            if T2[i] == Bibliothek[1]:
                t33.append(float(T1[i + 11]) * 0.00001)
            if T2[i] == Bibliothek[2]:
                t33.append(float(T1[i + 11]) * 0.00001)
            if T2[i] == Bibliothek[3]:
                t33.append(float(T1[i + 9]) * 0.00001)
            if T2[i] == Bibliothek[4]:
                t33.append(float(T1[i + 11]) * 0.00001)
        return t33
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 10:
        t34 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t34.append(float(T3[i + 9]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t34.append(float(T3[i + 11]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t34.append(float(T3[i + 11]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t34.append(float(T3[i + 9]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t34.append(float(T3[i + 11]) * 0.0001)
        return t34
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 10:
        t35 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t35.append(float(T4[i + 9]) * 0.00001)
            if T4[i] == Bibliothek[1]:
                t35.append(float(T4[i + 11]) * 0.00001)
            if T4[i] == Bibliothek[2]:
                t35.append(float(T4[i + 11]) * 0.00001)
            if T4[i] == Bibliothek[3]:
                t35.append(float(T4[i + 9]) * 0.00001)
            if T4[i] == Bibliothek[4]:
                t35.append(float(T4[i + 11]) * 0.00001)
        return t35
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 10:
        t36 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t36.append(float(T5[i + 9]) * 0.0001)
            if T5[i] == Bibliothek[1]:
                t36.append(float(T5[i + 11]) * 0.0001)
            if T5[i] == Bibliothek[2]:
                t36.append(float(T5[i + 11]) * 0.0001)
            if T5[i] == Bibliothek[3]:
                t36.append(float(T5[i + 9]) * 0.0001)
            if T5[i] == Bibliothek[4]:
                t36.append(float(T5[i + 11]) * 0.0001)
        return t36
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 10:
        t37 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t37.append(float(T1[i + 10]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t37.append(float(T1[i + 12]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t37.append(float(T1[i + 12]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t37.append(float(T1[i + 10]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t37.append(float(T1[i + 12]) * 0.00001)
        return t37
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 10:
        t38 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[0]:
                t38.append(float(T2[i + 10]) * 0.0001)
            if T2[i] == Bibliothek[1]:
                t38.append(float(T2[i + 12]) * 0.0001)
            if T2[i] == Bibliothek[2]:
                t38.append(float(T2[i + 12]) * 0.0001)
            if T2[i] == Bibliothek[3]:
                t38.append(float(T2[i + 10]) * 0.0001)
            if T2[i] == Bibliothek[4]:
                t38.append(float(T2[i + 12]) * 0.0001)
        return t38
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 10:
        t39 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t39.append(float(T3[i + 10]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t39.append(float(T3[i + 12]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t39.append(float(T3[i + 12]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t39.append(float(T3[i + 10]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t39.append(float(T3[i + 12]) * 0.0001)
        return t39
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 24:
        t40 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t40.append(float(T1[i + 11]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t40.append(float(T1[i + 13]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t40.append(float(T1[i + 13]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t40.append(float(T1[i + 11]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t40.append(float(T1[i + 13]) * 0.00001)
        return t40
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 24:
        t41 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[0]:
                t41.append(float(T1[i + 11]) * 0.00001)
            if T2[i] == Bibliothek[1]:
                t41.append(float(T1[i + 13]) * 0.00001)
            if T2[i] == Bibliothek[2]:
                t41.append(float(T1[i + 13]) * 0.00001)
            if T2[i] == Bibliothek[3]:
                t41.append(float(T1[i + 11]) * 0.00001)
            if T2[i] == Bibliothek[4]:
                t41.append(float(T1[i + 13]) * 0.00001)
        return t41
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 24:
        t42 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t42.append(float(T3[i + 11]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t42.append(float(T3[i + 13]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t42.append(float(T3[i + 13]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t42.append(float(T3[i + 11]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t42.append(float(T3[i + 13]) * 0.0001)
        return t42
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 24:
        t43 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[0]:
                t43.append(float(T4[i + 11]) * 0.00001)
            if T4[i] == Bibliothek[1]:
                t43.append(float(T4[i + 13]) * 0.00001)
            if T4[i] == Bibliothek[2]:
                t43.append(float(T4[i + 13]) * 0.00001)
            if T4[i] == Bibliothek[3]:
                t43.append(float(T4[i + 11]) * 0.00001)
            if T4[i] == Bibliothek[4]:
                t43.append(float(T4[i + 13]) * 0.00001)
        return t43
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 24:
        t44 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[0]:
                t44.append(float(T5[i + 11]) * 0.0001)
            if T5[i] == Bibliothek[1]:
                t44.append(float(T5[i + 13]) * 0.0001)
            if T5[i] == Bibliothek[2]:
                t44.append(float(T5[i + 13]) * 0.0001)
            if T5[i] == Bibliothek[3]:
                t44.append(float(T5[i + 11]) * 0.0001)
            if T5[i] == Bibliothek[4]:
                t44.append(float(T5[i + 13]) * 0.0001)
        return t44
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 24:
        t45 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[0]:
                t45.append(float(T1[i + 12]) * 0.00001)
            if T1[i] == Bibliothek[1]:
                t45.append(float(T1[i + 14]) * 0.00001)
            if T1[i] == Bibliothek[2]:
                t45.append(float(T1[i + 14]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t45.append(float(T1[i + 12]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t45.append(float(T1[i + 14]) * 0.00001)
        return t45
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 23:
        t46 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[0]:
                t46.append(float(T2[i + 12]) * 0.0001)
            if T2[i] == Bibliothek[1]:
                t46.append(float(T2[i + 14]) * 0.0001)
            if T2[i] == Bibliothek[2]:
                t46.append(float(T2[i + 14]) * 0.0001)
            if T2[i] == Bibliothek[3]:
                t46.append(float(T2[i + 12]) * 0.0001)
            if T2[i] == Bibliothek[4]:
                t46.append(float(T2[i + 14]) * 0.0001)
        return t46
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 24:
        t47 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[0]:
                t47.append(float(T3[i + 12]) * 0.0001)
            if T3[i] == Bibliothek[1]:
                t47.append(float(T3[i + 14]) * 0.0001)
            if T3[i] == Bibliothek[2]:
                t47.append(float(T3[i + 14]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t47.append(float(T3[i + 12]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t47.append(float(T3[i + 14]) * 0.0001)
        return t47
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 15:
        t48 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[1]:
                t48.append(float(T1[i + 1]) * 0.00001)
        return t48
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 15:
        t49 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[1]:
                t49.append(float(T1[i + 1]) * 0.00001)
        return t49
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 15:
        t50 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[1]:
                t50.append(float(T3[i + 1]) * 0.0001)
        return t50
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 15:
        t51 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[1]:
                t51.append(float(T4[i + 1]) * 0.00001)
        return t51
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 15:
        t52 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[1]:
                t52.append(float(T5[i + 1]) * 0.0001)
        return t52
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 15:
        t53 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[1]:
                t53.append(float(T1[i + 2]) * 0.00001)
        return t53
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 15:
        t54 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[1]:
                t54.append(float(T2[i + 2]) * 0.0001)
        return t54
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 15:
        t55 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[1]:
                t55.append(float(T3[i + 2]) * 0.0001)
        return t55
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 27:
        t56 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[2]:
                t56.append(float(T1[i + 5]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t56.append(float(T1[i + 5]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t56.append(float(T1[i + 5]) * 0.00001)
        return t56
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 27:
        t57 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[2]:
                t57.append(float(T1[i + 5]) * 0.00001)
            if T2[i] == Bibliothek[3]:
                t57.append(float(T1[i + 5]) * 0.00001)
            if T2[i] == Bibliothek[4]:
                t57.append(float(T1[i + 5]) * 0.00001)
        return t57
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 27:
        t58 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[2]:
                t58.append(float(T3[i + 5]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t58.append(float(T3[i + 5]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t58.append(float(T3[i + 5]) * 0.0001)
        return t58
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 27:
        t59 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[2]:
                t59.append(float(T4[i + 5]) * 0.00001)
            if T4[i] == Bibliothek[3]:
                t59.append(float(T4[i + 5]) * 0.00001)
            if T4[i] == Bibliothek[4]:
                t59.append(float(T4[i + 5]) * 0.00001)
        return t59
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 27:
        t60 = []
        for i in range(len(T5)):
            if T5[i] == Bibliothek[2]:
                t60.append(float(T5[i + 5]) * 0.0001)
            if T5[i] == Bibliothek[3]:
                t60.append(float(T5[i + 5]) * 0.0001)
            if T5[i] == Bibliothek[4]:
                t60.append(float(T5[i + 5]) * 0.0001)
        return t60
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 27:
        t61 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[2]:
                t61.append(float(T1[i + 6]) * 0.00001)
            if T1[i] == Bibliothek[3]:
                t61.append(float(T1[i + 6]) * 0.00001)
            if T1[i] == Bibliothek[4]:
                t61.append(float(T1[i + 6]) * 0.00001)
        return t61
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 27:
        t62 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[2]:
                t62.append(float(T2[i + 6]) * 0.0001)
            if T2[i] == Bibliothek[3]:
                t62.append(float(T2[i + 6]) * 0.0001)
            if T2[i] == Bibliothek[4]:
                t62.append(float(T2[i + 6]) * 0.0001)
        return t62
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 27:
        t63 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[2]:
                t63.append(float(T3[i + 6]) * 0.0001)
            if T3[i] == Bibliothek[3]:
                t63.append(float(T3[i + 6]) * 0.0001)
            if T3[i] == Bibliothek[4]:
                t63.append(float(T3[i + 6]) * 0.0001)
        return t63
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    elif Lesezeichen == 'L1' and PRN == 31:
        t64 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[4]:
                t64.append(float(T1[i + 9]) * 0.00001)
        return t64
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'L2' and PRN == 31:
        t65 = []
        for i in range(len(T2)):
            if T2[i] == Bibliothek[4]:
                t65.append(float(T1[i + 9]) * 0.00001)
        return t65
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C1' and PRN == 31:
        t66 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[4]:
                t66.append(float(T3[i + 9]) * 0.0001)
        return t66
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P1' and PRN == 31:
        t67 = []
        for i in range(len(T4)):
            if T4[i] == Bibliothek[4]:
                t67.append(float(T4[i + 9]) * 0.00001)
        return t67
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'C2' and PRN == 31:
        t68 = []
        for i in range(len(T5)):
             if T5[i] == Bibliothek[4]:
                t68.append(float(T5[i + 9]) * 0.0001)
        return t68
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'P2' and PRN == 31:
        t69 = []
        for i in range(len(T1)):
            if T1[i] == Bibliothek[4]:
                t69.append(float(T1[i + 10]) * 0.00001)
        return t69
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S1' and PRN == 31:
        t70 = []
        for i in range(len(T1)):
            if T2[i] == Bibliothek[4]:
                t70.append(float(T2[i + 10]) * 0.0001)
        return t70
    # -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
    elif Lesezeichen == 'S2' and PRN == 31:
        t71 = []
        for i in range(len(T3)):
            if T3[i] == Bibliothek[4]:
                t71.append(float(T3[i + 10]) * 0.0001)
        return t71
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    else:
        print(colored('\n \t La información no esta disponible porque no no existe \t \n', 'red', attrs = ['dark']))
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
def Anzeichen():
    print(colored('\n \t ¿Desea extraer información del catálogo presentado anteriormente? \n'))
    Whal = input(print(colored('Presione [y/n]: \n', 'light_cyan', attrs = ['dark'])))
    if Whal == 'y':
        print(colored('\n \t ¿Qué informacion desea consultar? \n',
            'light_red', attrs = ['bold']) + colored('(Ingrese: L1, L2, C1, P1, C2, P2, S1, S2 y el PRN) \n',
                'light_yellow', attrs = ['bold']) + colored('Por ejemplo: S1 (presiona Enter) 22 (presiona Enter) \n',
                    'dark_grey', attrs = ['bold']))
        Lese = input(colored('Ingresa el tipo de observación: ', 'light_blue', attrs = ['bold']))
        prn = input(colored('Ingresa el PRN (Solo el valor numérico): ', 'light_red', attrs = ['bold']))
        print(colored('\n La información se esta extrayendo... \n', 'light_green', attrs = ['bold']))
        Suche =  Herkunft(Lese, int(prn))
        Schreiben(Lese, prn, Suche)
        print(colored('\n La información esta lista en un archivo tipo ACII con nombre ', 'light_blue', attrs = ['bold']) +
              Lese + '_' + prn + colored(' en su carpeta \n', 'light_blue',
                attrs = ['bold']))
    if Whal == 'n':
        print(colored('\n Fin \n', 'light_cyan', attrs = ['bold']))
    os.remove('Archive_CSV_GPS.csv')
    os.remove('Archive_CSV_RINEX.csv')
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
print('Ejecutando programa..')
Aendern(Archive_4, Archive_5, Archive_6)
Anzeichen()
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#
fin = time.time()
print('Tiempo que tarda en ejecutar el programa: ', fin-ini, 'seg')
#\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\#