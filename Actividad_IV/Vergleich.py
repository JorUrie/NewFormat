import filecmp
import time
import os
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
# Se inicia el tiempo de medida del arraque del programa
ini = time.time()
# Limpiando pantalla
# Cambia dependiendo del SO
os.system ("cls")
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
def Line(Archive_1, Archive_2):
    # Abriendo archivos
    f1 = open(Archive_1)
    f2 = open(Archive_2)
    #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            # Comparando archivos
            if line1 in line2:
                # Imprimiendo los que son identicos
                print("Line ", i, ": IDENTICAL")
            break
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Cerrando programa
    f1.close()
    f2.close()
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
def Elemente(Archive_1, Archive_2):
    d1 = Archive_1
    d2 = Archive_2
    files = input('¿Qué elemento desea encontrar?: ')
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Comparacion superficial
    match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
    print('Comparación Superficial')
    print("Coinciden:", match)
    print("No coinciden:", mismatch)
    print("Errores:", errors)
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # Comparacion profunda
    match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow = False)
    print('Comparación profunda')
    print("Coiciden:", match)
    print("No Coiciden:", mismatch)
    print("Errores:", errors)
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
Archive_1 = 'tmig2620.22o'
Archive_2 = 'TMIG202209191800C.22o'
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
Line(Archive_1, Archive_2)
Elemente(Archive_1, Archive_2)
#==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/==/=#
fin = time.time()
print('Tiempo que tarda en ejecutar el programa: ', fin-ini, 'seg')