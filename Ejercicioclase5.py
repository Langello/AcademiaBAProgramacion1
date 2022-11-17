# registre 5 datos temperatura, finalmente muestre las  5 medidas y su promedio.
# Además si el promedio es mayor o igual a 21 indique "Clima cálido,", entre 19 y 21 "Clima templado", y menor de eso "Clima frío"

Temperaturas = []
acumulador = 0


for i in range(5):
    temp = int(input("Ingrese temperatura: "))
    Temperaturas.append(temp)
    acumulador += temp

print("Las temperaturas ingresadas son:")
for i in Temperaturas:
    print(i)

prom = acumulador/len(Temperaturas)
print ("El promedio de las temperaturases: ", round(prom,2))

if prom >= 21:
    print("Clima cálido")
elif prom <21 and prom >=19:
    print("Clima templado")
else:
    print("Clima frío")

input("Presione enter para finalizar")