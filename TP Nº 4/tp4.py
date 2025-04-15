ejer = int(input("Ingrese el ejercicio a ejecutar "))

if ejer == 1:

    for i in range (0, 101):
        print (i)

elif ejer == 2:

    num = input("Ingrese un numero entero ")

    cantidad_digitos = len(num)

    print(f"Su numero contiene {cantidad_digitos} digitos")

elif ejer == 3:

    valor1 = int(input("Ingrese el primer número: "))
    valor2 = int(input("Ingrese el segundo número: "))

    if valor1 < valor2:
        rango = range(valor1 + 1, valor2)
    else:
        rango = range(valor2 + 1, valor1)

    suma = sum(rango)

    print(f"La suma de los números comprendidos entre {valor1} y {valor2}, excluyéndolos, es: {suma}")

elif ejer == 4:

    suma_total = 0

    print("Ingrese números enteros para sumarlos. Ingrese 0 para detener el programa.")

    while True:

        numero = int(input("Ingrese un número: "))
    
        if numero == 0:
            break
    
    suma_total += numero

    print(f"El total acumulado es: {suma_total}")

elif ejer == 5:
    import random
    numero_secreto = random.randint(0, 9)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza! Intenta adivinar el número entre 0 y 9.")

    while True:

        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break
        else:
            print("Incorrecto, intenta de nuevo.")

elif ejer == 6:

    for numero in range(100, -1, -2):
        print(numero)

elif ejer == 7:
    numero = int(input("Ingrese un número entero positivo: "))

    if numero < 0:
        print("Por favor, ingrese un número positivo.")
    else:

        suma_total = sum(range(numero + 1))
    
    print(f"La suma de todos los números comprendidos entre 0 y {numero} es: {suma_total}")

elif ejer == 8:
    contador_pares = 0
    contador_impares = 0
    contador_positivos = 0
    contador_negativos = 0

    print("Por favor, ingrese 100 números enteros:")

    for i in range(1, 101):
        numero = int(input(f"Ingrese el número {i}: "))

        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1

        if numero > 0:
            contador_positivos += 1
        elif numero < 0:
            contador_negativos += 1

    print("\nResultados:")
    print(f"Números pares: {contador_pares}")
    print(f"Números impares: {contador_impares}")
    print(f"Números positivos: {contador_positivos}")
    print(f"Números negativos: {contador_negativos}")

elif ejer == 9:

    contador_num = 0
    
    print ("Ingrese 100 numeros enteros")

    for i in range(1, 11):
        numero1 = int(input(f"Ingrese el numero {i}: "))

    if numero1 > 0:
        contador_num += 1
    
    media = sum(numero1) / contador_num

    print(f"La media de la suma de los numeros ingresados es {media}")

elif ejer == 10:
    numero = input("Ingrese un número: ")

    numero_invertido = numero[::-1]

    print(f"El número invertido es: {numero_invertido}")

    

