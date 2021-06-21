#########  INFO OBLIGATORIA DEL PROGRAMADOR  ##########
#
#   NOMBRE COMPLETO: LEONARDO PERDOMO DURAN
#   GRUPO: 52
#
#######################################################

import modulo as mod
import pandas as pnd


def main():
    #Se inicializa una lista con valores simulados del costo de matricula de 10 estudiantes
    costoDeMatricula = [2014000, 1405550, 2300093, 5590000,
        3431212, 5431212, 3231233, 3213123, 2340000, 5202121]
    #Se hace carga un archivo json y se convierte a dataframe usando la libreria pandas de python
    dataframe = mod.cargarJsonADataFrame("Semana7Reto7/estudiantes.json")
    
    #Se imprimen los 5 primeros estudiantes incluidos en el dataframe
    print(mod.mostrar5primeros(dataframe))
    print()
    #Se imprimen los 5 ultimos estudiantes en el dataframe
    print(mod.mostrar5ultimos(dataframe))  
    print()
    #Se imprime el listado de mayores de 20 años de edad
    print(mod.mayoresDe(dataframe, 20))
    print()

    #Se crea un nuevo listado dataframe basado en el anterior, la funcion pregunta que columnas se quieren incluir
    newDataframe = mod.nuevoDataframe(dataframe)
    #Se le añade una nueva columna llamada costos y se le agrega la informacion de la lista antes inicializada
    newDataframe2 = mod.agregarColumna(costoDeMatricula, newDataframe)
    #Se pregunta por los estudiantes que pagaron mas de 5M 
    newDataframe3 = mod.matriculaCostosa(newDataframe2, 5000000)

    #Se imprimen los dataframes antes creados
    print(newDataframe)
    print()
    print(newDataframe2)
    print()
    print(newDataframe3)


main()
