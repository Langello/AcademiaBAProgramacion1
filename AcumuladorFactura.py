acum1 = 0
acum2 = 0

nombre1 = input("Ingrese el nombre del empleado 1: ")
monto1 = float(input("Ingrese su monto  "))
acum1 += monto1

while monto1 != 0:
    monto1 = float(input("Ingrese monto:  "))
    acum1 += monto1

nombre2 = input("Ingrese el nombre del empleado 2: ")
monto2 = float(input("Ingrese su monto  "))
acum2 += monto2

while monto2 != 0:
    monto2 = float(input("Ingrese monto:  "))
    acum2 += monto2

if acum1> acum2:
    print("El mayor total es de",nombre1,"con un importe de ",acum1)
elif acum2>acum1:
    print("El mayor total es de",nombre2,"con un importe de ",acum2)
else:
    print("Son iguales")

input("Presione Enter para finalizar")