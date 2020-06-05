## Ejercicio variables, if, listas, for, while...

#paso 1
int_score = 0

#paso 2
print("Adivina el Animal")

# paso 3
str_preg1 = input("Cual oso vive en el polo? ")
str_respuestaCorrecta = "Polar"

#paso 4
if str_preg1.lower() == str_respuestaCorrecta.lower():
    print("Correcto!")
    int_score += 1
else:
    print("Incorrecto")

str_preg2 = input("Cual es el animal mas rápido? ")
str_respuestaCorrecta = "Cheeta"

if str_preg2.lower() == str_respuestaCorrecta.lower():
    print("Correcto!")
    int_score += 1
else:
    print("Incorrecto")

print("nota final: ", int_score)
