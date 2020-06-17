# El cero es par
n = int(input("Digite n:"))
contador = 0
while contador <= n:
    if (contador % 2) != 0:
        print(contador, " impar")
    # Opcional de resolucion: print( 2 * i - 1 )
    # Opcional de resolucion: empezar el contador en 1 y aumentar de 2  en de 2
    # si es divisible por 2 el resultado es 0
    contador += 1 # equivalente a contador = contador + 1