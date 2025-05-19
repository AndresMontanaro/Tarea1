import random

def generar_numero():
    return random.randint(1, 20)

def main():

    intentos = 5
    intento_actual = 0
    numero_adivinado = False
    numero_ingresado = ""
    numero_elegido = 0

    numero_obtenido = generar_numero()

    while not numero_adivinado:
        
        if intento_actual == intentos:
            break    
        
        if (intentos-intento_actual) > 1:
            numero_ingresado = input(f"Adivine el número al azar entre 1 y 20. Tienes {(intentos-intento_actual)} intentos: ")
        else:
            numero_ingresado = input("Adivine el número al azar entre 1 y 20. Solo te queda 1 intento: ")

        if numero_ingresado.isdigit():
            
            numero_elegido = int(numero_ingresado)

            if numero_elegido > 0 and numero_elegido <= 20: 

                if numero_elegido != numero_obtenido:

                    intento_actual += 1

                    if intento_actual != intentos:
                        print("\nINCORRECTO. Inténtalo otra vez.\n")

                else:
                    
                    print("\nADIVINASTE!!!\n")

                    numero_adivinado = True

            else:

                print("\nIngreso inválido. Debe ser un valor numérico entre 1 y 20.\n")
        
        else:

            print("\nIngreso inválido. Debe ser un valor numérico entero.\n")

    print("JUEGO TERMINADO")

    if not numero_adivinado:

        print(f"El número correcto era {numero_obtenido}.\n")

    else:

        print(f"El número fue {numero_elegido}.\n") 

main()
