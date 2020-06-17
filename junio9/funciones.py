#funciones
# def : palabra para hacer funcion 
# nombre: como se llama mi funcion
# (parametros o argumentos): son mis input para la funcion

# esto es una variable global
variableFueraDeLaFuncion = "sumando"

print ("Hola a funciones")

def sumar(numero1, numero2):
    print(variableFueraDeLaFuncion)
    print("Resultado ", numero1 + numero2)

def restar(numero1, numero2):
    return numero1 - numero2


agenda = {}

def llenarAgenda(nombre, email, telefono):
    """ Aquí puedo agregar una descripción
        Entra: nombre, email, telefono
        Salida: agenda de contactos
        Restriccion: nombre es string, 
                     el email tiene que tener un @, PISTA: arroba in email
                     telefono es un numero entero
    """
    ## Restriciones
    ##     si es true continua, sino da mjs de error
    assert isinstance(nombre, str), "nombre no str"
    assert isinstance(telefono, int), "el telefono debe ser int"
    assert ("@" in email), "error de email"

    agenda[nombre]=telefono
    ## Tarea: guardar el correo y telefono

# solo puedo ejecutar o llamar una funcion, si ya la defini

llenarAgenda("Sammy", "samantha@gdgpuravida.xyz", 12345678)