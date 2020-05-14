## Rombo N
## Sammy Arburola
## 2020mayo20

""" Imprimir un rombo de tamaño diagonal menor n
    Entrada: int_tamanio, entero
    Salida:  dibujo de un rombo
    Restricciones: N/A
"""

int_tamanio = int(input("Diagonal menor: "))

for fila in range(int_tamanio):
    print ('%s%s'%(' '*(int_tamanio-(fila-1)),'*'*((fila*2)-1)))

for fila in range(int_tamanio,0,-1):
    print ('%s%s'%(' '*(int_tamanio-(fila-1)),'*'*((fila*2)-1)))