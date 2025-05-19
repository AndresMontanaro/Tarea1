numeros = [2, 3, 4, 5, 6]

numeros_dobles = [num * 2 for num in numeros]

numeros_al_cuadrado = [num ** 2 for num in numeros]

numeros_al_cubo = [num ** 3 for num in numeros]

for numero, numero_doble, numero_al_cuadrado, numero_al_cubo in zip(numeros, numeros_dobles, numeros_al_cuadrado, numeros_al_cubo):
    
    print(f"Original: {numero}, Doble: {numero_doble}, Cuadrado: {numero_al_cuadrado}, Cubo: {numero_al_cubo}")
