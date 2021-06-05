def buscarNombre(dicc, nombre):
  """
  TODO: detaller información

  ingresa una lista con un diccionario de estudiantes y un String con un nombre.
  Retorna una lista con los códigos de los estudiantes coincidentes
  """
  resultado = []
  for i in range(len(dicc)):
    if dicc[i].get("nombre") == nombre:
      resultado.append(dicc[i].get("codigo"))
  
  return resultado

def buscarPorCarrera(dicc, carrera):
  """
   TODO: detaller información

  ingresa una lista con un diccionario de estudiantes y un String con una carrera.
  Retorna una lista con los nombres de los estudiantes coincidentes, y como últmo dato de la lista, el promedio de edad los estudiantes coincidentes.
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
  TODO: detaller información

  ingresa una lista con un diccionario de estudiantes.
  Retorna una lista con los nombres de los estudiantes que estén en el semestre más alto de todos: Ej, si el semestre más alto reportado es 9, entonces la lista debe tener los estudiantes que estén en 9 semestre.
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
  return resultado

def calcularPromedioNota(dicc):
  """
  TODO: detaller información

  ingresa una lista con un diccionario de estudiantes.
  Retorna un diccionario con el promedio de notas de los estudiantes donde las llaves del diccionario es los códigos de los estudiantes, y los valores del diccionario es el promedio de notas de las materias.
  """

  resultado = {}
  # usar el dicc.values() le puede ser muy útil en esta función
  return resultado