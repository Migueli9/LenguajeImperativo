print("Determinaremos si el numero que ingreses es par o impar!")
print("Comencemos!")

while True:
    Considerar = int(input("Ingresa un numero entero: "))
    if Considerar % 2 == 0:
        print(f"El numero {Considerar} es par")
    else:
        print(f"El numero {Considerar} es impar")
    SaliroContinuar = input("Quieres hacer otro intento? (Si/No)")
    if SaliroContinuar == "no":
        print("Hasta la proxima!")
        break 
