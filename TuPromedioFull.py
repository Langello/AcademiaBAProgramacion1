# Ingresar notas, calcular el promedio y luego mostrar sobresaliente(8 a 10), regular (4 a 7) y reprobado (0 a 3)
# Preguntar luego de poner cada nota si desea ingresar una más
# En caso de que el promedio no este entre 0 y 10 volver pedir las notas nuevamente.


def calificacion():
    continuar = input(
        "Bienvenido presione enter para empezar o escriba quit para salir").lower()
    if continuar != "quit":
        sumNotas = 0
        ingresos = 0
        while continuar != "listo":
            nota = int(input("Ingrese una nota"))
            sumNotas += nota
            ingresos += 1
            continuar = input(
                "Ingrese listo si ya puso todas las notas, para seguir poniendo notas presione enter").lower()
        promedio = round(sumNotas/ingresos, 1)

        if promedio >= 8 and promedio <= 10:
            tuCalificacion = "Sobresaliente"
        elif promedio >= 4 and promedio < 8:
            tuCalificacion = "Regular"
        elif promedio >= 0 and promedio < 4:
            tuCalificacion = "Reprobado"
        else:
            print("Tu promedio es", promedio,
                  " y no esta entre 0 y 10, presiona enter y volvamos a empezar...")
            input()
            return calificacion()
        print("Tu promedio es", promedio,
              "y tu calificacion es: ", tuCalificacion)
    else:
        quit()


calificacion()

input("Presione enter para finalizar")
