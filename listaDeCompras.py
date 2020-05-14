## Lista de Compras
## Sammy Arburola
## 2020mayo20

""" Preguntar los articulos de una lista de compras e imprimir el resultado final
    Entrada: str_articulo, float_cantidad, str_volumen
    Salida:  Pretty Print de la lista de compras
    Restricciones: N/A
"""

# Variables iniciales
flag_contruyendoLista = True
dict_compras = {}

# Entrada
print("Indicadores: agregar A, terminal T")
while flag_contruyendoLista:
    str_indicador = str(input(">>> "))
    if str_indicador == 'A':
        str_articulo = str(input("Articulo: "))
        float_cantidad = float(input("Cantidad: "))
        str_volumen = str(input("Volumen: "))
        
        # restricciones
        isinstance(str_articulo, str)
        isinstance(str_volumen, str)
        isinstance(float_cantidad, float)

        # guardar
        dict_compras[str_articulo] = (float_cantidad, str_volumen)

    elif str_indicador == 'T':
        flag_contruyendoLista = False
        break
    else:
        print("Error")

#print("Articulos")
#print(dict_compras.keys())

print('|'+"Lista de Compras".center(32, ' ') + '|' + '\n' + '-' * 34)
for articulo in dict_compras:
    print('|' + articulo.center(10, ' ') +\
          '|' + str(dict_compras[articulo][0]).center(10, ' ') +\
          '|' + dict_compras[articulo][1].center(10, ' ') + '|')

"""
ToDo
1. Guardar en un archivo, puede ser txt u hoja de calculo
2. Usar el indicador (str_indicador) para hacer una lista de supermercado,
   una lista de verduleria
3. si agrego un articulo por segunda vez, ¿Que pasa?
4. Usando slicing, agregar la información de los artículos en una sola línea
Opcional: usar pulsar enter para terminar de agregar articulos a la lista
"""
