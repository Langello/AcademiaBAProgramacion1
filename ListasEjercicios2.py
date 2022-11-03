# Cargar facturas hasta ingresar cero, al finalizar se debe mostrar los importes mayores a 300000

facturas = []  # Creamos lista para guardar importes

importe = float(input("Ingrese importe: "))  # Pedimos el primer importe
facturas.append(importe)

while importe != 0:   # Seguimos pidiendo importes hasta que se ingrese 0
    importe = float(input("Ingrese importe: "))
    if importe != 0:
        # Cada importe que se ingresa se agrega en la lista factura
        facturas.append(importe)

for i in facturas:
    if i >= 300000:
        print(i)

input("Presione enter para terminar")
