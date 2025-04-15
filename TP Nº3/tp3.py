ejer = int(input("Ingrese el ejercicio a ejecutar"))

if ejer == 1:
    edad = int(input("Ingrese un número entero: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

elif ejer == 2:
    nota = float(input("Ingrese su nota"))
    if nota >= 6:
        print("Estas aprobado")
    else:
        print("Estas desaprobado")

elif ejer == 3:
    num = int(input("Ingrese un numero par"))
    if num % 2 == 0:
        print("Su numero es par")
    else:
        print("Por favor ingrese un numero par") 

elif ejer == 4:
    edad_1 = int(input("Ingrese su edad"))
    if edad_1 < 12:
        print("Eres un niño")
    elif edad_1 < 18:
        print("Eres un adolescente")
    elif edad_1 < 30:
        print("Eres un adulto joven")
    else:
        print("Eres un adulto")

elif ejer == 5:
    contra = str(input("Ingrese una contraseña (de entre 8 y 14 digitos)"))
    if len(contra) >= 8 < 14:
        print("Ha ingresado la contraseña correctamente")
    else:
        print("Por favor ingrese una contraseña que cumpla con la cantidad de digitos solicitados")  

elif ejer == 6:
    import random
    from statistics import mode, median, mean

    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    if media > mediana > moda:
        sesgo = "positivo"
    elif media < mediana < moda:
        sesgo = "negativo"
    else:
        sesgo = "sin sesgo"

        print(f"Números aleatorios: {numeros_aleatorios}")
        print(f"Moda: {moda}")
        print(f"Mediana: {mediana}")
        print(f"Media: {media}")
        print(f"Sesgo: {sesgo}")

elif ejer == 7:
    frase = str(input("Ingrese una palabra o frase"))
    if frase [-1].lower() in "aeiou":
        frase += '!'
        print(f"Resultado: {frase}")

elif ejer == 8:
    nombre = input("Por favor, ingresa tu nombre: ")

    print("Elige una opción:")
    print("1. Mostrar el nombre en mayúsculas")
    print("2. Mostrar el nombre en minúsculas")
    print("3. Mostrar el nombre con la primera letra en mayúscula")
    opcion = int(input("Ingresa el número de la opción que deseas (1, 2 o 3): "))

    if opcion == 1:
        print("Tu nombre en mayúsculas es:", nombre.upper())
    elif opcion == 2:
        print("Tu nombre en minúsculas es:", nombre.lower())
    elif opcion == 3:
        print("Tu nombre con la primera letra en mayúscula es:", nombre.title())
    else:
        print("Opción no válida. Por favor, ingresa 1, 2 o 3.")
    
elif ejer == 9:
    magnitud = float(input("Ingrese la magnitud del terremoto"))
    
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por las personas pero generalmente no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en pequeñas estructuras)")
    elif magnitud < 7:
        print("Muy fuerte (causa daños significativos)")
    elif magnitud > 7:
        print("Extremo (causa daños graves a gran escala)")

elif ejer == 10:
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
    mes = int(input("Ingresa el número del mes (1 para enero, 12 para diciembre): "))
    día = int(input("Ingresa el día del mes: "))

    if hemisferio == "N":
    if (mes == 12 and día >= 21) or (1 <= mes <= 2) or (mes == 3 and día <= 20):
        estacion = "Invierno"
    elif (mes == 3 and día >= 21) or (mes <= 6 and día <= 20):
        estacion = "Primavera"
    elif (mes == 6 and día >= 21) or (7 <= mes <= 8) or (mes == 9 and día <= 20):
        estacion = "Verano"
    elif (mes == 9 and día >= 21) or (mes <= 12 and día <= 20):
        estacion = "Otoño"
    elif hemisferio == "S":  # Hemisferio sur
        if (mes == 12 and día >= 21) or (1 <= mes <= 2) or (mes == 3 and día <= 20):
        estacion = "Verano"
    elif (mes == 3 and día >= 21) or (mes <= 6 and día <= 20):
        estacion = "Otoño"
    elif (mes == 6 and día >= 21) or (7 <= mes <= 8) or (mes == 9 and día <= 20):
        estacion = "Invierno"
    elif (mes == 9 and día >= 21) or (mes <= 12 and día <= 20):
        estacion = "Primavera"
    else:
    estacion = "Hemisferio no válido"

    print(f"La estación en la que te encuentras es: {estacion}")