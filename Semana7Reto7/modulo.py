import pandas as pnd

def cargarJsonADataFrame(path):
    dataframe = pnd.read_json(path)
    return dataframe

def mostrar5primeros(dataframe):
    return dataframe.head(5)

def mostrar5ultimos(dataframe):
    return dataframe.tail(5)

def mayoresDe(dataframe, edad):
    return dataframe[dataframe["edad"]>=edad]

def nuevoDataframe(dataframe):
    opcion = int(input("Elija la cantidad de columnas que desea mostrar: "))
    lista = [input("Ingrese el nombre de la columna del Dataframe a agregar: ") for i in range(opcion)]
    newDataframe = dataframe[lista]
    return newDataframe

def agregarColumna(lista, dataframe):
    newDataframe = dataframe.assign(costo = lista)
    return newDataframe

def matriculaCostosa(dataframe, costo):
    return dataframe[dataframe["costo"]>costo]

def haciaExcel(dataframe):
    dataframe.to_excel("Semana7Reto7/archivoExcel.xlsx")