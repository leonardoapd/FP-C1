#########  INFO OBLIGATORIA DEL PROGRAMADOR  ##########
#                                           
#   NOMBRE COMPLETO: LEONARDO PERDOMO DURAN
#   GRUPO: 52
#
#######################################################  

"""
Así es mi pequeño saltamontes, ya estás en capacidad de hacer el programa competo desde cero.
no olvidescrear los modulos necesarios, importar las librerías y una función main que de un poco de orden al archivo pincipal
"""

from numpy import cosh
import modulo as mod
import pandas as pnd

def main():
    dataframe = mod.cargarJsonADataFrame("Semana7Reto7/estudiantes.json")
    print(mod.mostrar5primeros(dataframe))
    print("""
    #################################################################################################################
    """)
    print(mod.mostrar5ultimos(dataframe))
    print("""
    #################################################################################################################
    """)
    print(mod.mayoresDe(dataframe, 20))
    print("""
    ###########################################################
    """)
    newDataframe = mod.nuevoDataframe(dataframe)
    print(newDataframe)
    print("""
    ###########################################################
    """)
    costoDeMatricula = [2014000, 1405550, 2300093, 5590000, 3431212, 5431212, 3231233, 3213123, 2340000, 5202121]
    newDataframe2 = mod.agregarColumna(costoDeMatricula, newDataframe)
    print(newDataframe2)
    print("""
    ###########################################################
    """)
    newDataframe3 = mod.matriculaCostosa(newDataframe2, 5000000)
    print(newDataframe3)
    mod.haciaExcel(newDataframe3)

main()
