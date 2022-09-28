import datetime

Reloj = datetime.datetime.now()
ValorMin = 150
opc = 1
ve = 0
DistRec = 0
LatOrLong = 0
LatposOrLatNeg = 0
LongposOrLongNeg = 0

while opc != 2301: #Primer Ciclo
    print("")
    print("Fecha: ",Reloj.strftime("%c"))
    print("Presione 1 para registrarse")
    print("Presione 2 para salir")
    opc = int(input("Ingrese opcion: "))
    if opc == 1 : #Registro
        print("")
        print("Fecha: ",Reloj.strftime("%c"))
        print("Ingrese su nombre y apellido")
        usuario = input()
        opc = 2
        while opc !=2001: #Segundo Ciclo
            print("")
            print("Fecha: ",Reloj.strftime("%c"))
            print("Usuario "+ usuario)
            print("Presione 1 para comenzar una carrera")
            print("Presione 2 para salir")
            opc = int(input('Ingrese opcion: '))
            if opc == 1: #Inicio Carrera
                print("")
                print("Fecha: ",Reloj.strftime("%c"))
                opc = 2
                Latitud = int(input("Ingrese ubicacion (LATITUD): ")) #Ingreso Ubicacion
                Longitud = int(input("Ingrese ubicacion (LONGITUD): ")) #Termino De Ingreso Ubicacion
                LongitudInc = Longitud
                LatitudInc = Latitud
                while opc !=145: #Tercer Ciclo
                    print("")
                    print("Fecha: ",Reloj.strftime("%c"))
                    print("Usuario: "+usuario)
                    print("Ubicacion Longitud:",Longitud ," | Latitud:",Latitud)
                    print("Presione 1 para encender el vehiculo")
                    print("Presione 2 para terminar el viaje")
                    print("Presione 0 para cancelar el viaje")
                    v = 0
                    opc = int(input("Ingrese opcion: "))
                    if opc == 1:
                        while v != 4: #Cuarto Ciclo
                            velocidad = ve
                            print(DistRec)
                            print("")
                            print("Fecha: ",Reloj.strftime("%c"))
                            print("Usuario: "+usuario)
                            print("Ubicacion Longitud:",Longitud ," | Latitud:",Latitud)
                            print("Vehiculo encendido")
                            print("Velocidad ",velocidad," Km/h")
                            print('Presione 1 para Acelerar')
                            print('Presione 2 para Frenar')
                            print('Presione 3 para girar')
                            print('Presione 4 para apagar vehiculo')
                            a = int(input("Ingrese opcion: "))
                            if a >= 5:
                                print("INGRESE OPCION VALIDA PORFAVOR")
                                input("Enter para continuar")

                            if a == 1: #OPCION 1 CUARTO CICLO
                                ve = ve + 1
                                DistRec = DistRec + 1
                                if LatOrLong % 2 == 1:
                                    print("Latitud")
                                    if LatposOrLatNeg % 2 == 1:
                                        Latitud = Latitud - 1
                                    if LatposOrLatNeg % 2 == 0:
                                        Latitud = Latitud + 1
                                    
                                if LatOrLong % 2 == 0:
                                    print("Longitud")
                                    if LongposOrLongNeg % 2 == 0:
                                        Longitud = Longitud + 1
                                    if LongposOrLongNeg % 2 == 1:
                                        Longitud = Longitud - 1
                                    
                            if a == 2: #OPCION 2 CUARTO CICLO
                                ve = ve * 0
                            if a == 3: #OPCION 3 CUARTO CICLO
                                print("1 = derecha")
                                print("2 = izquierda")
                                b=int(input('Ingrese opcion: '))
                                if b == 1: # GIRAR A LA DERECHA
                                    if LatOrLong % 2 == 1:
                                        LatOrLong = LatOrLong + 1
                                        if LatposOrLatNeg % 2 == 0:
                                            if LongposOrLongNeg % 2 == 1:
                                                LongposOrLongNeg = LongposOrLongNeg + 1
                                        if LatposOrLatNeg % 2 == 1:
                                            if LongposOrLongNeg % 2 == 0:
                                                LongposOrLongNeg = LongposOrLongNeg + 1
                                        
                                    elif LatOrLong % 2 == 0:
                                        LatOrLong = LatOrLong + 1
                                        if LongposOrLongNeg % 2 == 0:
                                            if LatposOrLatNeg % 2 == 0:
                                                LatposOrLatNeg = LatposOrLatNeg + 1
                                        if LongposOrLongNeg % 2 == 1:
                                            if LatposOrLatNeg %2 == 1:
                                                LatposOrLatNeg = LatposOrLatNeg + 1
                                elif b == 2: # GIRAR A LA IZQUIERDA
                                    if LatOrLong % 2 == 1:
                                        LatOrLong = LatOrLong + 1
                                        if LatposOrLatNeg % 2 == 0:
                                            if LongposOrLongNeg % 2 == 0:
                                                LongposOrLongNeg = LongposOrLongNeg + 1
                                        if LatposOrLatNeg % 2 == 1:
                                            if LongposOrLongNeg % 2 == 1:
                                                LongposOrLongNeg = LongposOrLongNeg + 1
                                        
                                    elif LatOrLong % 2 == 0:
                                        LatOrLong = LatOrLong + 1
                                        if LongposOrLongNeg % 2 == 0:
                                            if LatposOrLatNeg % 2 == 1:
                                                LatposOrLatNeg = LatposOrLatNeg + 1
                                        if LongposOrLongNeg % 2 == 1:
                                            if LatposOrLatNeg %2 == 0:
                                                LatposOrLatNeg = LatposOrLatNeg + 1
                            if a == 4: #OPCION 4 CUARTO CICLO
                                break
                            
                    if opc == 2: #OPCION 2 TERCER CICLO
                        print("")
                        print("Su recorrido fue desde:")
                        print("Latitud inicio: ",LatitudInc," ","Longitud inicio: ",LongitudInc,)
                        print("hasta")
                        print("Latitud final: ",Latitud," ","Longitud final: ",Longitud)
                        print("El total a pagar es de: $", ValorMin*((Latitud - LatitudInc)+(Longitud - LongitudInc)))
                        f = (input("Terminar viaje si/no: "))
                        if f == "si":
                            opc = 145
                    if opc == 0: #OPCION 3 TERCER CICLO
                        break
                        

            if opc == 2: #OPCION 2 SEGUNDO CICLO
                opc = 2
                break
    
    if opc == 2: #OPCION 2 PRIMER CICLO
        break