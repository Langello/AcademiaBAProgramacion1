# Cargar notas del alumno en una lista, mostrar todas las notas, promedio y si paso de año.

#creo la funcion ingresenotas() para que en caso de que no ingrese ninguna (ponga 0 desde el inicio)
# pueda retornar a pedir que ingrese las notas(el programa se vuelva a ajecutar).
def ingresenotas():
    notas = []
    acumnota = 0
    nota = int(input("Ingrese nota:  "))
    # si la nota no esta entre 0 y 10 le decimos que ingreso una nota incorrecta
    if nota > 10 or nota < 0:
        print("Esa nota es incorrecta")
    # agregar notas nuevas ingresadas que no sea 0 y esten entre 0 y 10
    elif nota != 0:
        notas.append(nota)
        # acumular notas para luego sacar el promedio y verificar que al menos las notas sean mayor a 0 para poder sacar su promedio
        acumnota += nota
    # pedimos mas notas hasta que ingrese 0 // Ponemos exacatamente lo mismo que cuando pedimos la primera nota
    while nota != 0:
        nota = int(input("Ingrese nota:  "))
        if nota > 10 or nota < 0:
            print("Esa nota es incorrecta")
        elif nota != 0:
            notas.append(nota)
            acumnota += nota


# si hay notas ingresadas mostramos la lista de las notas menos el 0
    if acumnota != 0:
        print("Las notas ingresadas son")
        for i in notas:
            print(i)
    else:
        print("No ingresaste notas")
        return ingresenotas()
    # si hay notas ingresadas sacamos el promedio (acumnota es dintinto a cero) 
    if acumnota != 0:
        promedio = round(acumnota / len(notas), 2)
    # mostramos si esta aprobado o desaprobado
        if promedio > 4:
            print("Proemdio ", promedio, " Aprobado")
        else:
            print("Proemdio", promedio, " Desaprobado")

#llamamos a la funcion
ingresenotas()
input("Presione Enter para finalizar")
