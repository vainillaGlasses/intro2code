## Leer Archivo
## Sammy Arburola
## 2020mayo20

""" Imprimir cada linea de un archivo
    Entrada: str_nombreAchivo
    Salida:  lineas enumeradas del archivo
    Restricciones: N/A
"""

# Entrada
str_nombreAchivo = str(input("Nombre del archivo: "))
# archivoEjemplo.txt

# Programa
file_file2open = open (str_nombreAchivo,'r')
list_contenido = file_file2open.readlines()

int_contadorDeLineas = 1
for linea in list_contenido:
    print(str(int_contadorDeLineas), linea, end='')
    int_contadorDeLineas += 1
file_file2open.close()