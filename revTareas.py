
int_score  = 0
preguntas_hechas = 0
oportunidades = 3

lista_animales = [
  'Leon',
  'Jirafa',
  'Cheeta'
]

lista_preguntas = [
  'Que animal se dice que es el rey de la selva?: ',
  'Que animal es el mas alto?: ',
  'Que animal es el mas rapido?: '
]

print('Guess the Animal')

for i in lista_preguntas:

  # Dentro del while validamos si está o no correcta la respuesta del usuario, en caso que este incorrecta entra a ejecutar las instrucciones del while
  while (lista_animales[preguntas_hechas] != input(lista_preguntas[preguntas_hechas])):
    print('Incorrecto!!')
    oportunidades -= 1
    print('Te quedad ' + str(oportunidades) + ' oportunidades\n')
    # Si las oportunidades llegan a cero, deja de preguntar y continua con el codigo que va despues del while
    if(oportunidades == 0):
      break
  
  # Si las oportunidades no llegaron a cero, quiere decir que respondió bien y se suma un punto al score
  if oportunidades != 0:
    print('Correcto!!\n')
    int_score += 1
  
  print('==========================================================')
  preguntas_hechas += 1
  oportunidades = 3

print("Tu puntaje final es de: " + str(int_score) + '\n')
