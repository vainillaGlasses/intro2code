## crear isdigit()
variableGlobal = "hola mundo"

#   nombre  parametros
def esdigito(tira):
    """ Vericar si una tira es un numero
        Entrada: tira, de tipo str o int
        Salida: True si la tira contiene numeros enteros, False si tiene letras
        Validacion / Restriccion: tira tiene que ser un str
    """
    # Validacion
    #      condicion
    assert isinstance(tira, str), "Error: no escribio una tira"

    # revision de cada letra
    for letra in tira:
        # if por cada numero
        # preguntando si esta en el range de los ascii
        #   isinstance(int(letra), int)
        if int(letra) in [0,1,2,3,4,5,6,7,8,9]:
            print(":)")
        else:
            return False ## retornar una respuesta
    return True ## retornar una respuesta
print("estoy fuera de la funcion") 


def aux_summa():
    pass #para cuando no he hecho una funcion

## como llamo una funcion
esdigito("123456")