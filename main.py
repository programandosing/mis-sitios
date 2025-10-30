import random
from js import document

nivel = None
puntaje = 0
preguntas = 0
puntos_totales = 0
respuesta_correcta = 0

def mostrar(id):
    document.querySelectorAll(".pantalla").forEach(lambda e: e.classList.add("oculto"))
    document.getElementById(id).classList.remove("oculto")

def iniciar(n):
    global nivel, puntaje, preguntas
    nivel = n
    puntaje = 0
    preguntas = 0
    mostrar("juego")
    nueva_pregunta()

def nueva_pregunta():
    global a, b, respuesta_correcta, preguntas
    preguntas += 1
    if nivel == 1:
        a = random.randint(1, 3)
        b = random.randint(1, 10)
    elif nivel == 2:
        a = random.randint(4, 7)
        b = random.randint(1, 10)
    else:
        a = random.randint(8, 10)
        b = random.randint(1, 10)

    respuesta_correcta = a * b
    document.getElementById("numero_pregunta").innerText = f"Pregunta {preguntas}/10"
    document.getElementById("pregunta").innerText = f"¿Cuánto es {a} x {b}?"
    document.getElementById("mensaje").innerText = ""
    document.getElementById("imagen").src = ""
    document.getElementById("respuesta").value = ""

def comprobar():
    global puntaje, preguntas, puntos_totales
    try:
        r = int(document.getElementById("respuesta").value)
        msg = document.getElementById("mensaje")
        img = document.getElementById("imagen")

        if r == respuesta_correcta:
            puntaje += 1
            msg.innerText = random.choice(["¡Excelente! ¡Eres un genio!", "¡Perfecto!", "¡Muy bien hecho!"])
            msg.style.color = "purple"
            img.src = "imagenes/perfecto.jpg"
        else:
            msg.innerText = f"Ups... era {respuesta_correcta}. ¡Sigue intentando!"
            msg.style.color = "red"
            img.src = "imagenes/pesimo.jpg"
    except:
        msg.innerText = "Por favor ingresa un número válido"
        msg.style.color = "blue"
        return

    from pyodide.ffi import create_proxy
    import asyncio

    async def esperar():
        await asyncio.sleep(2.5)
        if preguntas < 10:
            nueva_pregunta()
        else:
            mostrar_resultado()
    asyncio.ensure_future(esperar())

def mostrar_resultado():
    global puntaje, puntos_totales
    mostrar("resultado")
    puntos_ganados = puntaje * 10
    puntos_totales += puntos_ganados

    document.getElementById("puntaje").innerText = f"Puntaje: {puntaje}/10"
    document.getElementById("puntos_ganados").innerText = f"Puntos Ganados: +{puntos_ganados}"
    document.getElementById("total").innerText = f"Puntos Totales: {puntos_totales}"
    document.getElementById("puntos_totales").innerText = f"Puntos Totales: {puntos_totales}"

    if puntaje >= 9:
        premio, color, msg = "TROFEO DE ORO", "#ffd700", "¡Eres un maestro de las tablas!"
    elif puntaje >= 6:
        premio, color, msg = "MEDALLA DE PLATA", "#c0c0c0", "¡Muy bien! Sigue practicando"
    elif puntaje >= 3:
        premio, color, msg = "MEDALLA DE BRONCE", "#cd7f32", "¡Bien hecho! A mejorar un poco más"
    else:
        premio, color, msg = "PREMIO DE CONSUELO", "#b3e0ff", "¡No te rindas, campeón!"

    div = document.getElementById("premio")
    div.innerText = premio
    div.style.backgroundColor = color
    document.getElementById("mensaje_extra").innerText = msg

def volver_menu():
    mostrar("menu_principal")

def salir():
    mostrar("menu_principal")