# Ingresar 3 notas, calcular el promedio y luego mostrar sobresaliente(8 a 10), regular (4 a 7) y reprobado (0 a 3)

nota1 = int(input("Ingrese la primera nota"))
nota2 = int(input("Ingrese la segunda nota"))
nota3 = int(input("Ingrese la tercera nota"))

promedio = round((nota1+nota2+nota3)/3, 1)
print("Tu promedio es ", promedio)

if promedio >= 8 and promedio <= 10:
    print("Sobresaliente")
elif promedio >= 4 and promedio < 8:
    print("Regular")
elif promedio >= 0 and promedio < 4:
    print("Reprobado")
else:
    print("No ingreso notas entre 0 y 10")
