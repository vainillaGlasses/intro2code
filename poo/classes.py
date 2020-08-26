## Binario https://docs.google.com/presentation/d/1wyoHoASGGUPrhPgR2K5Bx852JY_zVL2iadAjiIRZxj4/edit#slide=id.g87c88df04f_0_31
## Ejemplos https://www.tutorialspoint.com/python/python_classes_objects.htm
## Poli https://uniwebsidad.com/libros/algoritmos-python/capitulo-15/polimorfismo

## Clase

class Employee:
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Nombre : ", self.name,  ", Salario: ", self.salary)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

## Delete
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts)
del pt1
del pt2
del pt3

## Herencia
class Numero:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def getNombre(self):
        print(self.nombre)

    def getNumero(self):
        print(self.nombre +" en decimal es: "+str(self.numero))
    def aBinario(self):
        print(bin(numero)[2:])

class Binario(Numero):
    def getNumero(self):
        print(self.nombre +" en binario es: "+str(self.numero))
    def aDecimal(self):
        print(int(self.numero,2))

## Ocultamiento
class Contador:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = Contador()
counter.count()
counter.count()
print (counter.__secretCount)

## Polimorfismo
def frecuencias(secuencia):
    """ Calcula las frecuencias de aparición de los elementos de
        la secuencia recibida.
        Devuelve un diccionario con elementos: {valor: frecuencia}
    """
    # crea un diccionario vacío
    frec = dict()
    # recorre la secuencia
    for elemento in secuencia:
        frec[elemento] = frec.get(elemento, 0) + 1
    print(frec)
frecuencias(["peras", "manzanas", "peras", "manzanas", "uvas"])
frecuencias((1,3,4,2,3,1))
frecuencias("Una frase")
frecuencias(range(2,20,3))
frecuencias(4)
