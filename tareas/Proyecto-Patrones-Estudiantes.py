##--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.-##
##
## Programa: Patrones.py
## Autor   : 
## Fecha   : 
##
##     Los  Patrones Armoon  son representaciones mediante figuras
## especiales de números en binario (1`s y 0`s). Se rellenan según
## a  la  especificación  numeral  del  usuario  y  mediante  este
## programa también se permite la suma de ellos.
##
##--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.-##

## Función: 
def sumando(num):
    """ Retorna el operando a partir de la revisión de las restricciones
        En caso de ser un dígito válido retorna el valor correpondiente,
        de lo contrario la salida será 0

        Entrada:
            número correspondiente al operando

        Salida :
            operando

        Restricciones:
            la entrada debe ser un entero positivo
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

## Función: Dibujo tipo 1 (hexagono) Patrones ArMoon    
def hexagono(contador, _6bits):
    """ Dibuja el simbolo del Patrón ArMoon
              *-----*
             ***---***
            *****-*****
            -----*-----
             ---***---
              -*****-

        Entradas:
            contador, tira de bits
        Salida  :
            impresión del patron
        Restricciones:
            contador debe ser entero positivo,
            el largo de la tira de binario debe ser 6
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

## Función: Dubujo tipo 2 (reloj de arena) Patrones ArMoon
def arena(contador, _6bits):
    """ Dibuja el simbolo del Patrón ArMoon
              -----*-----
               ---***---
                -*****-
                *-----*
               ***---***
              *****-*****

        Entradas:
            contador, tira de bits
        Salida  :
            impresión del patron
        Restricciones:
            contador debe ser entero positivo,
            el largo de la tira de binario debe ser 6
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion
    
## Función: Impresión de Patrones ArMoon
def imprime_patron(operando):
    """ Recibe un número decimal para el cual va a realizar la
        concatenación de simbolos los cuales formaran el patrón ArMoon

        Entrada:
            número decimal 
        Salida :
            Impresión del patrón ArMoon
        Restricciones:
            la entrada debe ser entero positivo
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

## Función: Sumador ArMoon
def suma_ArMoon(sumando1, sumando2):
    """ Suma dos sumandos decimales en ArMoon
        Entrada:
            sumando1 y sumando2
        Salidas:
            resultado de la sumar ArMoon en decimal
        Restricciones:
            las entradas son enteros postivo
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion


## Función: Menú Principal
def menu():
    """ Implementar el menú para que el usuario pueda elegir la acción a realizar

        Entradas:
            Ninguna
            
        Salidas:
            Ninguna
            
        Restricciones:
            Ninguna
    """
    
    ## Presentación del programa
    print(":=" * 37)
    print(" Mosaico ArMoon ".center(74, "|"))
    print(":=" * 37 + "\n")
    instrucciones = "Para esta versión de Mosaica ArMoon tiene disponibles estos comandos\n" +\
          "1. Ingresar primer  operando\n2. Ingresar segundo operando\n" +\
          "3. Imprimir primer  operando\n4. Imprimir segundo operando\n" +\
          "5. Imprimir suma\n6. Terminar\n  ?: para ver las Instrucciones\n"
    print(instrucciones)
    
    ## Lectura de la opción
    opcion = input("OPCIÓN > ")

    ## Difinición de operandos
    operando1 = 0
    operando2 = 0

    ## Evaluación de instruacciones
    while opcion:
        if opcion == "?":        ## Mostrar las intruciones
                print("?" * 73)
                print(" Instrucciones ".center(73, "·"))
                print("?" * 73)
                print(instrucciones + "\n") 
            
        elif opcion == "6":      ## Terminar
            break

        elif opcion in ["1", "2", "3", "4", "5"]:  ## Escoger la opción del menú

            if opcion == "1":    ## Opción No. 1
                print("=:" * 37)
                print(" Primer Sumando ".center(73, "="))
                print("=:" * 37)
                num = 1
                operando1 = sumando(num)
                
            elif opcion == "2":  ## Opción No. 2
                print("=:" * 37)
                print(" Segundo Sumando ".center(73, "="))
                print("=:" * 37)
                num = 2
                operando2 = sumando(num)
                
            elif opcion == "3":  ## Opción No. 3
                print("**=" * 24)
                print(" Armoon Sumando 1 ".center(73, "-"))
                print("**=" * 24)
                imprime_patron(operando1)
                
            elif opcion == "4":  ## Opción No. 4
                print("**=" * 24)
                print(" Armoon Sumando 2 ".center(73, "-"))
                print("**=" * 24)
                imprime_patron(operando2)
                
            elif opcion == "5":  ## Opción No. 5
                print(":-" * 37)
                print(" Suma Armoon ".center(73, "·"))
                print(":-" * 37)
                resultado = suma_ArMoon(operando1, operando2)
                imprime_patron(resultado)

        opcion = input("\nOPCIÓN > ")

    print("¡Fin!")

## Programa Principal
if __name__ == "__main__":
    menu()
