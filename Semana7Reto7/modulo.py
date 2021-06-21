import pandas as pnd

#Funcion para cargar el json y convertirlo a dataframe
def cargarJsonADataFrame(path):
    dataframe = pnd.read_json(path)
    return dataframe

#Funcion para mostrar los 5 primeros del dataframe
def mostrar5primeros(dataframe):
    return dataframe.head(5)

#Funcion para mostrar los 5 ultimos del dataframe
def mostrar5ultimos(dataframe):
    return dataframe.tail(5)

#Funcion para evaluar si dentro del dataframe existe un dato con una edad o mayor a ella
def mayoresDe(dataframe, edad):
    return dataframe[dataframe["edad"]>=edad]

#Funcion para crear un dataframe con base a otro de entrada, tomando las columnas 
def nuevoDataframe(dataframe):
    opcion = int(input("Elija la cantidad de columnas que desea mostrar: "))
    lista = [input("Ingrese el nombre de la columna del Dataframe a agregar: ") for i in range(opcion)]
    newDataframe = dataframe[lista]
    return newDataframe

#Funcion para agregar una nueva columna llamada costo con datos de una lista entrante
def agregarColumna(lista, dataframe):
    newDataframe = dataframe.assign(costo = lista)
    return newDataframe

#Funcion para evaluar si un dato de la lista supera el costo ingresado
def matriculaCostosa(dataframe, costo):
    return dataframe[dataframe["costo"]>costo]

#Funcion para exportar un archivo excel
def haciaExcel(dataframe):
    dataframe.to_excel("Semana7Reto7/archivoExcel.xlsx")