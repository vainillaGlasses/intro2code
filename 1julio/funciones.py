def saludar(nombre):
    """ voy a saludar
        Entrada: str
        Salida: no hay variable de salida, print
        Restricciones: no hay
    """
    print("Hola ", nombre)

## Funciones
# f(x) = x**2
def elevar(numero):
    return numero ** 2

## Procedimientos
def imprimir_hasta_n(n):
    for i in range(n):
        print(i)

def llenarLista(limiteRango):
    """ hacer una lista con los numeros de un rango
    """
    lista = []
    for i in range(limiteRango):
        lista.append(i)
    return lista