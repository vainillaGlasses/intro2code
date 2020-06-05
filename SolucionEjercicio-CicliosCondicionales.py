## Ejercicio variables, if, listas, while...

#paso 1
int_score = 0
lista_presguntas = ["Cual es el animal mas largo? ", "Cual oso vive en el polo? ", "Cual es el animal mas rápido? "]
lista_respuestas = ["Ballena Azul", "Polar", "Cheeta"]
oportunidades = 0

int_preguntasHechas = 0
#paso 2
print("Adivina el Animal")

while int_preguntasHechas < len(lista_presguntas):
    ## Pregunta
    respuesta = input(lista_presguntas[int_preguntasHechas])
    
    ## Validar la respuesta
    if lista_respuestas[int_preguntasHechas].lower() == respuesta.lower():
        print("Correcto!")
        int_score += 1
        int_preguntasHechas += 1
    else:
        if oportunidades < 2:
            print("Lo sentimos, sigue jugando!")
        else:
            int_preguntasHechas += 1
        oportunidades += 1
    
print("nota final: ", int_score)