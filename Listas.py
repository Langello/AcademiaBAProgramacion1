frutas = ["Pera", "Banana", "Palta", "Frutilla"]
#           0       1         2         3
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

frutas.append("Sandía")  # Agrega items al la lista

print(frutas[4])

for elemento in frutas:  # Se recorre toda la lista
    print(elemento)
"""
Pera
Banana
Palta
Frutilla
Sandía 
"""

cantFrutas = len(frutas)  # Guarda la cantidad de elementos la lista

print("Cantidad de frutas", cantFrutas)

numeros = [1, 2, 3, 4, 5, 15, 8, 65, 7]
numeros.sort()  # Modifica la lista y la ordena de menor a mayor
print(numeros)  # [1, 2, 3, 4, 5, 7, 8, 15, 65]

input('Enter para finalizar')
