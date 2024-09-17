
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
