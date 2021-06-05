def buscarNombre(dicc, nombre):
  """
  Ingresa una lista con un diccionario de estudiantes y un String con un nombre.
  Retorna una lista con los códigos de los estudiantes coincidentes.
  Se recorre la lista con un for y luego se pregunta por la llave 
  nombre para encontrar su codigo asociado a cada nombre ingresado.
  """
  resultado = []
  for i in range(len(dicc)):
    if dicc[i].get("nombre") == nombre:
      resultado.append(dicc[i].get("codigo"))
  
  return resultado

def buscarPorCarrera(dicc, carrera):
  """
  Ingresa una lista con un diccionario de estudiantes y un String con una carrera.
  Retorna una lista con los nombres de los estudiantes coincidentes, y como último dato de la lista, 
  el promedio de edad los estudiantes coincidentes.
  Se declaran variables para calcular la suma de las edades y el promedio de ellas.
  Se evalua la carrera ingresada en busca de quien la cursa y el promedio de edades de los estudiantes que la cursan.
  """
  resultado = []
  divisor = suma = 0
  for i in range(len(dicc)):
    if dicc[i].get("carrera") == carrera:
      resultado.append(dicc[i].get("nombre"))
      suma += dicc[i].get("edad")
      divisor += 1
  promedio = suma//divisor
  resultado.append(promedio)

  return resultado

def encontrarMayorSemestre(dicc):
  """
  Ingresa una lista con un diccionario de estudiantes.
  Retorna una lista con los nombres de los estudiantes que estén en el semestre más alto de todos: 
  Ej, si el semestre más alto reportado es 9, entonces la lista debe tener los estudiantes que estén en 9 semestre.
  Se busca ente las lista el semestre mas alto reportado y luego con base en eso, se busca con un for los nombres de 
  los estudiantes que estan en ese semestre.
  """
  lista = []
  mayor = dicc[0].get("semestre")
  for i in range(len(dicc)):
      if dicc[i].get("semestre") > mayor:
        mayor = dicc[i].get("semestre")
  for j in range(len(dicc)):      
    if dicc[j].get("semestre") == mayor:
      lista.append(dicc[j].get("nombre"))
  return lista



def quienHaPerdido(dicc, materia):
  """
  TODO: detaller información

  ingresa una lista con un diccionario de estudiantes y un String con una materia.
  Retorna un diccionario con los estudiantes que hayan perdido la materia, las llaves del diccionario siempre serán los nombres del estudiante, y el valor del diccionario será la nota de la materia perdida.
  """
  resultado = {}
  for i in range(len(dicc)):
    if materia in dicc[i].get("materias"):
      if dicc[i].get("materias").get(materia) < 3:
        resultado[dicc[i].get("nombre")] = dicc[i].get("materias").get(materia)
  return resultado

def calcularPromedioNota(dicc):
  """
  TODO: detaller información

  ingresa una lista con un diccionario de estudiantes.
  Retorna un diccionario con el promedio de notas de los estudiantes donde las llaves del diccionario es los códigos de los estudiantes, y los valores del diccionario es el promedio de notas de las materias.
  """

  resultado = {}

  for i in range(len(dicc)):
    promedio = dicc[i].get("materias").values()

    resultado[dicc[i].get("codigo")] = 
  # usar el dicc.values() le puede ser muy útil en esta función
  return resultado