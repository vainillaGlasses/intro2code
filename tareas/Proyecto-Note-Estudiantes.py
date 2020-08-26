## =============================================================================
##
## Programa: PauPat.py
## Autor   : 
## Fecha   :
##
## Editar y crear archivos .txt 
##
## Entradas     : INSTRUCCIONES, AYUDA o la digitación de los comandos
##
## Salidas      : El contenido del archivo
##
## Restricciones: descubra y defina sus restricciones
##
## =============================================================================

## DECLARACIÓN DE VARIABLES GLOBALES
txtArchivo    = []
archivo       = ""
gi            = 0
patron        = ""
instrucciones = "Los comandos que puede ejecutar son las siguientes:\n" + \
          "Tenga en cuenta que el simbolo "'_'" representa un espacio en blanco y\n" +\
          "donde "'xxx'" representa la propiedad del comando\n"+\
          "- Digite --> Para \n" +\
          "    L_xxx    Cargar un Archivo de texto(.txt)\n" +\
          "    C        Borrar la Memoria\n" +\
          "    S        Guardar Archivo\n" +\
          "    S_xxx    Guardar como\n" +\
          "    D_xxx    Borrar Línea\n" +\
          "    I        Insertar línea al final del texto\n" +\
          "    I_n      Insertar línea en una pocisión "'n'"\n" +\
          "    P        Desplegar el Contenido del Archivo\n" +\
          "    F_xxx    Buscar el patrón x en el texto\n" +\
          "    N        Buscar la siguiente línea con el patrón\n"

ayuda  =  "   COMANDOS   EJEMPLO\n" +\
          "     L_xxx    --> L archivo.txt\n" +\
          "     C        --> C\n" +\
          "     S        --> S\n" +\
          "     S_xxx    --> S " + r"C:\\Usuarios\\Personal\\Desktop\\nombreArchivo" +" \n" +\
          "     D_xxx    --> D 5\n" +\
          "     I        --> I\n" +\
          "              ----> Esta es mi nueva linea\n"+\
          "     I_n      --> I 4\n" +\
          "              ----> Esta es mi nueva linea\n"+\
          "     P        --> P\n" +\
          "     F_xxx    --> F hola usuario\n" +\
          "     N        --> N\n"

titulo = "="*70 + "\n" + " " * 30 + "PauPat 2013" + "\n" + " " * 24 +\
         "Editor de Archivos txt" + "\n" + "="*70 + "\n" +\
         "="*70 + "\n" + "Para   recibir   asistencia   digite:   INSTRUCCIONES    ó    AYUDA\n"+\
         "="*70 + "\n" + "="*70 + "\n"

## DEFINICIÓN DE FUNCIONES

def sub_archivo(comando):
    """ Extraer línea por línea el contenido de un archivo y
        concatenarlo en la lista txtArchivo para su edición 
        Entrada     : comando
        Salida      : txtArchivo
        Restriccion : sólo pueden ser archivos .txt
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

def guardar():
    """ Guarda las modificaciones realizadas a txtArchivo
        Entrada     : Ninguna
        Salida      : Ninguna
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

def guardar_como(comando):
    """ Guarda las modificaciones en un nuevo archivo
        Entrada     : comando
        Salida      : Ninguna
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

def BorraLinea(comando):
    """ Borra una línea específica de txtArchivo
        Entrada     : comando
        Salida      : Ninguna
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

def I_final():
    """ Insertar línea al final de txtArchivo
        Entrada     : linea
        Salida      : Ninguna
        Restricción : Sólo se puede ingresar una línea a la vez
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion

def I_ind(comando):
    """ Insertar una línea en una pocisión 'n' a txtArchivo
        Entrada     : linea
        Salida      : Ninguna
        Restricción : Sólo se puede ingresar una línea a la vez
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion
  
def Pprint():
    """ Desplegar el contenido de txtArchivo en línea enumeradas
        Entrada     : Ninguna
        Salida      : Ninguna
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion
        
def Bpatron(i, comando):
    """ Buscar la primera instancia patrón en el texto
        Entrada     : i, comando
        Salida      : la línea que contiene el patrón debidamente enumerada
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion
    
def Npatron(comando):
    """ Buscar la primera instancia patrón en el texto
        Entrada     : comando
        Salida      : la siguiente línea que contiene el patrón debidamente enumerada
        Restricción : Ninguna
    """
    pass # Recuerden remover esta instruccion cuando programen la funcion
        
def principal():
    """ Función que evalua cual comando se ejecutará
        Entradas      : comando
        Salidas       : Ninguna
        Restricciones : Ninguna
    """
    print(titulo)

    comando = str(input("--> "))
    while comando:
        ini = comando[0]
        if comando == "AYUDA":
            print(ayuda)
            
        elif comando == "INSTRUCCIONES":
            print(instrucciones)
            
        elif ini == "L":
            sub_archivo(comando)
            
        elif ini == "C":
            txtArchivo.clear()

        elif ini == "S" and len(comando) == 1:
            guardar()
            
        elif ini == "S" and len(comando) > 2:
            guardar_como(comando)
                        
        elif ini == "D":
            BorraLinea(comando)                
        
        elif ini == "I" and len(comando) == 1:
            I_final()          
        
        elif ini == "I" and len(comando) > 2:
            I_ind(comando)
    
        elif ini == "P":
            Pprint()

        elif ini == "F":
            Bpatron(0, comando)
              
        elif ini == "N":
            Npatron(comando)
        
        else:
            print("ERROR DE COMANDO")
        
        comando = str(input("--> "))
    print("Fin de la edición")

    
if __name__ == "__main__":
	principal()
