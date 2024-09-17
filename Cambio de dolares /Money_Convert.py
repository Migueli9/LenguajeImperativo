Dolar = 19.20
print("Bienvenido a tu convertidor de moneda mas confiable")
print("COMENCEMOSSSSSS!")
option = int(input("¿Qué moneda quieres convertir?\n1 = Dólares a Pesos\n2 = Pesos a Dólares\nIngresa el número de la opción: "))

if option == 1:
        CantidadDeDolar = float(input("Cuantos dolares quieres convertir?"))
        resultadoDolar= Dolar * CantidadDeDolar
        print(f"{CantidadDeDolar} dolares son equivalentes a {resultadoDolar:.2f} pesos." )
elif option == 2:
        CantidadDePesos = float(input("Cuantos pesos quieres cambiar a dolares?"))
        resultadoPesos = CantidadDePesos / Dolar
        print(f"{CantidadDePesos} pesos son equivalentes a {resultadoPesos:.2f} dolares")
else:
        print("Opcion no valida. Por favor, selecciona 1 o 2")
