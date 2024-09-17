print("Welcome to All In One, where everything what do you want is here")
print("Well, Let's Begin!!!!")

while True:
    option = input("What do you wanna do?\n 1 = Currency exchange\n 2 = Triangle's Ares\n 3 = Odd or even\n 4 = Can you be Driver? \n 5 = Don Baraton\n 6 = Exit\n")

    if option == '1':
        Dolar = 19.20
        print("Bienvenido a tu convertidor de moneda mas confiable")
        print("COMENCEMOSSSSSS!")
        while True:
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
            SalirOContinuar = input("Quieres regresar al menu principal? (si/no)\n")
            if SalirOContinuar == 'si':
                break
    if option == '2':
        while True:
            print("Bienvenido a Calculeidor")
            base = float(input("Cual es la base del triangulo?\n"))
            altura = float(input("Cual es la altura del triangulo?\n"))
            Respuesta = base * altura / 2
            print(f"El area del triangulo es: {Respuesta}")
            print("Gracias por usar calculeidor")
            print("Hasta la proxima!")
            SalirOContinuar = input("Quieres regresar al menu principal? (si/no)\n")
            if SalirOContinuar == 'si':
                break
    if option =='3':
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
    if option == '4':
        print("Ahora evaluaremos si estas acto para estar tras el volante")
        while True:
            Edad = int(input("Cual es su edad?: \n"))
            if Edad < 18:
                print("Eres menor de edad, valora tu vida.")
                break
            if Edad >= 65:
                ExamenMedico = input("Se ha realizado un examen medico en menos de 3 meses? \n")
                if ExamenMedico == 'si':
                    FueronBuenos = input("Sus resultados fueron buenos? \n")
                    if FueronBuenos == "si":
                        print("Usted todavia puede conducir, por el momento...")
                    else:
                        print("Lo siento, le recomiendo que instale uber")
                else:
                    print("Hagalos y despues vuelve")
            else:
                Licencia = input("Cuenta con licencia? \n")
                if Licencia == 'si':
                    print("Usted puede seguir manejando sin miedo")
                else:
                    print("La licencia de Dios no cuenta hermano, pero nos podemos arreglar")
            SaliroContinuar = input("Quieres volverlo a intentar? \n")
            if SaliroContinuar == 'no':
                print("Hasta la proxima!")
                break
    if option == '5':
        print("Bienvenido a Don Baraton, Donde los descuentos sobran")
        while True:
            TotalCompra = float(input("Cual fue el monto final de su compra? \n"))
            Vip = input("Es cliente Vip? (Si/No)\n")
            descuento = 0.05
            if Vip == "si":
                if TotalCompra >= 1000:
                    print("Obtuviste un descuento del 15%!!!!")
                    Desc15 = TotalCompra * 0.15
                    CompraDesc15 = TotalCompra - Desc15
                    print(f"Su monto total con descuento seria de: {CompraDesc15}")
                    print("Quien dijo que ser vip no tenia sus ventajas!!!")
                elif 500 <= TotalCompra < 1000:
                    print("Obtuviste un descuento del 10%!!!!")
                    Desc10 = TotalCompra * 0.10
                    CompraDesc10 = TotalCompra - Desc10
                    print(f"Su monto total con descuento seria de: {CompraDesc10}")
                elif TotalCompra < 500: 
                    print("Lo siento, no obtuvo descuento :'( ")
                    print(f"Pero como eres vip puedo hacer una excepsion y regalarte un 5% de tu compra :D")
                    Desc5 = TotalCompra * 0.05
                    CompraDesc5 = TotalCompra - Desc5
                    print(f"Su monto total seria de: {CompraDesc5}")
            elif Vip == "no":
                if TotalCompra >= 1000:
                    print("Obtuviste un descuento del 10%!!!!")
                    Desc10 = TotalCompra * 0.10
                    CompraDesc10 = TotalCompra - Desc10
                    print(f"Su monto final sera de: {CompraDesc10}")
                elif 500 <= TotalCompra < 1000:
                    print("Obtuviste un descuento del 5%!!!!")
                    Desc5 = TotalCompra * 0.05
                    CompraDesc5 = TotalCompra - Desc5
                    print(f"Su monto total seria de: {CompraDesc5}")
                elif TotalCompra < 500:
                    print("Lo siento, no obtuvo descuento :'( ")
            SalirOContinuar = input("Quieres hacer otro intento?(Si/No) \n")
            if SalirOContinuar == "no":
                print("Hasta la proxima!")
                break
    if option == '6':
        print("Hasta la proxima!")
        break

