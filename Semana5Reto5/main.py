import data as d
import model as m

#########  INFO OBLIGATORIA DEL PROGRAMADOR  ##########
#                                           
#   NOMBRE COMPLETO: 
#   GRUPO:
#
####################################################### 


def main():
  #@TODO: completar el llamado a las funciones
  print(m.buscarNombre(d.estudiantes,"Luisa"))
  print(m.buscarPorCarrera(d.estudiantes,"Medicina"))
  print(m.encontrarMayorSemestre(d.estudiantes))
  print(m.quienHaPerdido(d.estudiantes, "Algebra"))
  print(m.calcularPromedioNota([]))

main()