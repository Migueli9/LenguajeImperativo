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
