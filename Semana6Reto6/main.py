import model as m

#########  INFO OBLIGATORIA DEL PROGRAMADOR  ##########
#                                           
#   NOMBRE COMPLETO: 
#   GRUPO:
#
#######################################################  



def main():
  """
  TODO: realizar los llamados correspondientes a las funciones que tienen cada desafío que compone el reto.
  """
   # Se obtiene la matriz de claves
  claves = m.cargarClave() 
  # Se obtiene la matriz de alias
  alias = m.cargarAlias() 
  print(alias)
  # Se descifran los nombres
  print(m.descifrarAlias(claves,alias)) 
  # Se guardan los nombres en un archivo binario 
  m.guardarOculto(m.descifrarAlias(claves,alias)) 
  # Se carga el archivo binario y se muestra una lista con el contenido de los nombres descifrados
  print(m.cargarOcultoYDepurar())

main()