import marshal
def cargarClave():
  """
  No tiene valores de ingreso
  Retorna una matriz de palabras
  """

  # Se inicializa una matriz vacia para guardar los datos de la clave
  lista = [] 
  # Se lee el archivo clave.txt
  archivo = open("Semana6Reto6/Data/clave.txt","r")
  for linea in archivo:
    columnas = []
  # Se crea una lista de los elementos del archivo claves.txt que estaban separados por ","
    silaba = linea.split(",")
    if '\n' in silaba[-1]:
      silaba[-1] = silaba[-1][:-1]
      columnas.extend(silaba)
    else:
      columnas.extend(silaba)
  # Se agrega la lista anterior a la matriz lista        
    lista.append(silaba) 
  # Se cierra el archivo creado
  archivo.close()
  return lista


def cargarAlias():
  """
  No tiene valores de ingreso,
  Retorna una matriz con cadenas de 3 valores [entero coma entero] Ej ['5,6']
  """
  # Se inicializa una matriz vacia para guardar los datos del alias
  listaAlias = [] 
  # Se lee el archivo alias.txt
  archivo = open("Semana6Reto6/Data/alias.txt","r")
  aux = archivo.readline()
  # Se separa el texto contenido en el archivo alias.txt y se guarda en una lista 
  aux = aux.split("$") 
  for j in aux:
    # Se separa nuevamente
    elemento = j.split("*")
    # Y se guarda en la matriz
    listaAlias.append(elemento)
  archivo.close()
  return listaAlias

def descifrarAlias(claves,alias):
  """
  Ingresa una matriz con las claves de los nombres, y una matriz con las coordenadas para buscar en las claves
  Retorna una matriz con cada uno de los nombres descifrados
  """
   # Se crea una lista vacia para almacenar el resultado de la busqueda entre las matrices
  resultado = [] 
  for i in range(len(alias)): # Se recorre la matriz alias
    columna = []
    for j in range(len(alias)-1):
      # Se extrae la informacion contenida en la matriz, cada posicion contiene numeros de coordenadas que se usaran en la matriz clave  
      coordenada = alias[i][j]  
      coordenada = coordenada.split(",") 
      #print(claves[int(coordenada[0])-1][int(coordenada[1])-1])
      # Y con la informacion se busca dentro de la matrz clave y se añade a resultado
      columna.append(claves[int(coordenada[0])-1][int(coordenada[1])-1]) # Y con la informacion se busca dentro de la matrz clave y se añade a resultado
      coordenada = []
    resultado.append(columna)  
  return resultado
  
def guardarOculto(nombres):
  """
  ingresa una matriz de nombres
  no tiene valor de retorno, pero debe grabar un archivo binario con el nombre chapas.mtic
  """
  # Se crea un archivo binario
  file = open("chapas.mtic", "bw")
  # Y se le guarda la informacion proveniente del resultado con los nombres antes contenidos 
  marshal.dump(nombres, file) 
  file.close()

def cargarOcultoYDepurar():
  """
  No tiene parámteros de ingreso
  Retorna una lista con los nombres de cada uno de los alias como cada elemento de la lista
  """
  lista = []
  # Se lee el archivo binario
  file = open("chapas.mtic", "br") 
  aux = marshal.load(file)
  cadena = ""
  # Se decifra concatenando las cadenas correspodientes y añadiendolas a una lista
  for i in aux:
    for j in i:
      cadena += j
    lista.append(cadena)
    cadena = ""
  return lista
