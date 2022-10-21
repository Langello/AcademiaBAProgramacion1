print("Acumulador de importes - Ingrese 0 para finalizar")
monto = int(input("Ingrese monto:"))
total = 0
total += monto

while monto != 0:
    monto = int(input("Ingrese monto: "))
    total = total+monto
print("El total de importes es:", total)

input("Ingrese enter para finalizar")
