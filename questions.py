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
    ("\n1.size()", "\n2.len()", "\n3.length()", "\n4.count()"),
    ("\n1. 3.14", "\n2. '42'", "\n3. 10", "\n4. True"),
    ("\n1. input()", "\n2. scan()", "\n3. read()", "\n4. ask()"),
    ("\n1. // Esto es un comentario", "\n2. /* Esto es un comentario */", "\n3. -- Esto es un comentario", "\n4. # Esto es un comentario"),
    ("\n1. =", "\n2. ==", "\n3. !=", "\n4. ==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Organizo las listas en una
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

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
# Se selecciona la pregunta, opciones y respuesta correcta
for juego, (question, options, correct_index) in enumerate(questions_to_ask, 1):
    separador = "*"*34
    print(f"\n{separador}\nPregunta NRO {juego}\n")

     # Se imprimen las preguntas y opciones
    print(f"{question}")
    print(" ".join(options))

    # El usuario tiene 2 intentos para responder correctamente
    for intentos in range(2):
        user_answer = get_user_answer()

        # Verificar si la respuesta del usuario es correcta
        if user_answer == correct_index:
            print("\n¡Correcto!")
            puntaje +=1
            break
         #Si no es correcta, se avanza con el segundo intento
        else:
            if intentos == 0:
                print("Incorrecto. Proba con otra opcion:")
                puntaje -=0.5
                user_answer = get_user_answer()
                if user_answer == correct_index:
                    print("\n¡Correcto!")
                    puntaje +=1
                    break  
                #Si vuelve a equivocarse, se muestra la opcion correcta          
                else:
                    puntaje -=0.5
                    opcion_correcta = int(correct_index)+1
                    respuesta_correcta = options[correct_index]
                    print(f"Incorrecto, no te preocupes, la proxima vez ira mejor! \nLa respuesta correcta es la número {opcion_correcta}: {respuesta_correcta}")
                    break
# Se devuelve el puntaje final y se informa el FIN del juego
puntaje = 0 if puntaje < 0 else puntaje
print(f"\nPUNTAJE FINAL: {puntaje}")
print(f"\n{separador}\nFINALIZASTE EL JUEGO")
            
