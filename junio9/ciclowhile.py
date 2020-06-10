preguntasYrespuestas = { "quien ladra? ": "perro", "quien maulla? ": "gato"}
print(preguntasYrespuestas)
agregarAnimal = input("Animal: ")
agregarPregunta = input("pregunta para quiz: ")

preguntasYrespuestas[agregarPregunta] = agregarAnimal
print("ya agregar paso")
print(preguntasYrespuestas)