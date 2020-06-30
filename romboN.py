## Rombo N
## Sammy Arburola
## 2020mayo20

""" Imprimir un rombo de tamaño diagonal menor n
    Entrada: int_tamanio, entero
    Salida:  dibujo de un rombo
    Restricciones: N/A
"""

int_tamanio = 5 # int(input("Diagonal menor: "))

for i in [0, 1, 2, 3, 4]:
    print ( '1' * (int_tamanio - (i-1)) , '*' * ((i*2)-1))

for i in [5, 4, 3, 2, 1]:
    print ('1' * (int_tamanio-(i-1)),'*'*((i*2)-1))

