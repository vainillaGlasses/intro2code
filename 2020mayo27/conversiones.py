# Ejercicio de Steven Goñi

#Instrucciones generales

"""Hacer un programa que 
reciba onzas/gramos y las convierta en gramos/onzas"""

int_tipo=int(input("Escriba \n 1 Si desea convertir de onzas a gramos "
                   "\n 2 Si desea convertir de gramos a onzas "))   #Da a escoger al usuario
                                                                    #la posibilidad de escoger el tipo
                                                                    #de conversión

float_tazaDeConversion = 28.3495231 #Una onza equivale a 28.35 gramos

if int_tipo == 1:
    float_entrada = float(input("Dígite las onzas que desea convertir a gramos "))
    float_gramos = float_entrada*float_tazaDeConversion #conversión de gramos a onzas
    print("El resultado de la conversión es de: " + str(float_gramos) + " g")
elif int_tipo == 2:
    float_entrada = float(input("Dígite los gramos que desea convertir a onzas "))
    float_onzas = float_entrada/float_tazaDeConversion
    print("El resultado de la conversión es de: " + str(float_onzas) + " oz")
else:
    #No hay opción válida
    print("No ha ingresado una opción válida")


print("Final del código")