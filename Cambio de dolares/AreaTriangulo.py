
print("Bienvenido a Calculeidor")

while True:
    base = float(input("Cual es la base del triangulo?\n"))
    altura = float(input("Cual es la altura del triangulo?\n"))

    Respuesta = base * altura / 2

    print(f"El area del triangulo es: {Respuesta}")

    SalirOcontinuar = input("Quieres salir del programa? (Si/No): ")
    if SalirOcontinuar == "si":
        print("Gracias por usar calculeidor")
        print("Hasta la proxima!")
        break



