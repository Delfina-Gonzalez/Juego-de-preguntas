import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Función para obtener y verificar la respuesta del usuario
def get_user_answer():
    user_answer = input("\nRespuesta: ")
    
    # Verifica si la respuesta es un número y si está en el rango de respuestas posibles
    if user_answer.isdigit() and 0<(int(user_answer))<(len(questions)):
        user_answer = int(user_answer) - 1  # Restamos 1 porque las opciones son 1-based
        return user_answer
    else:
        print("Respuesta no válida")
        sys.exit(1)

puntaje = int (0)

# El usuario deberá contestar 3 preguntas
for juego in range(1, 4):
    separador = "*"*34
    print(f"\n{separador}\nPregunta NRO {juego}")

    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intentos in range(2):
        user_answer = get_user_answer()

        # Verificar si la respuesta del usuario es correcta
        if user_answer == correct_answers_index[question_index]:
            print("\n¡Correcto!")
            puntaje +=1
            break
        else:
            if intentos == 0:
                print("Incorrecto. Segundo intento:")
                puntaje -=0.5
                user_answer = get_user_answer()
                if user_answer == correct_answers_index[question_index]:
                    print("\n¡Correcto!")
                    puntaje +=1
                    break            
                else:
                    puntaje -=0.5
                    opcion_correcta = int(correct_answers_index[question_index]+1)
                    respuesta_correcta = answers[question_index][correct_answers_index[question_index]]
                    print(f"Incorrecto. La respuesta correcta es la número {opcion_correcta}: {respuesta_correcta}")
                    break
puntaje = 0 if puntaje < 0 else puntaje
print(f"\n PUNTAJE FINAL: {puntaje}")
print(f"\n{separador}\n FINALIZASTE EL JUEGO")
            
