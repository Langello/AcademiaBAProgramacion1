notas = [] #Lista vacía

print("Sistema de notas")
n1 =int(input("Ingrese nota 1: "))
notas.append(n1)

n2 =int(input("Ingrese nota 2: "))
notas.append(n2)

n3 =int(input("Ingrese nota 3: "))
notas.append(n3)

print ("Las notas son:")
for num in notas:   #Recorremos la lista
    print("nota ", num)

input("Presione Enter para finalizar")