import funciones

str_variableNombre = input("Digite su nombre")
funciones.saludar(str_variableNombre)
numero_elevado = funciones.elevar(8)
print("8 a la 2 es: ", numero_elevado)

numero_elevado = numero_elevado + 10
print(numero_elevado)
n = int(input("n:"))
funciones.imprimir_hasta_n(4)

lista = [1,2,3]
lista.append(funciones.llenarLista(3))
print(lista)

lista_numeros = [5,65,23,65,65,123,65,5]

def foo():
    lista_numeros.append("fin")
    global saludos
    saludos = "hola"

def goo():
    print(saludos)

print(saludos)
