adminAcc1 = "Admin1"
adminAcc2 = "Admin2"
admin1Pass = "123"
admin2Pass = "567"
vet1Name = ""
vet1Code = ""
vet1Specialty = ""
vet1PhoneNum = ""
vet1EmailAdd = ""
vet1Schedule = ""
vet2Name = ""
vet2Code = ""
vet2Specialty = ""
vet2PhoneNum = ""
vet2EmailAdd = ""
vet2Schedule = ""
vet3Name = ""
vet3Code = ""
vet3Specialty = ""
vet3PhoneNum = ""
vet3EmailAdd = ""
vet3Schedule = ""
owner1FullName = ""
owner1IDNum = ""
owner1PhoneNum = ""
owner1EmailAdd = ""
owner1Address = ""
owner1Pet1Name = ""
owner1Pet1Race = ""
owner1Pet1BirthDate = ""
owner1Pet1Sex = ""
owner1Pet1Weight = ""
owner1Pet1Characteristics = ""
owner1Pet1Food = ""
owner1Pet1Observations = ""
owner1Pet2Name = ""
owner1Pet2Race = ""
owner1Pet2BirthDate = ""
owner1Pet2Sex = ""
owner1Pet2Weight = ""
owner1Pet2Characteristics = ""
owner1Pet2Food = ""
owner1Pet2Observations = ""
owner2FullName = ""
owner2IDNum = ""
owner2PhoneNum = ""
owner2EmailAdd = ""
owner2Address = ""
owner2Pet1Name = ""
owner2Pet1Race = ""
owner2Pet1BirthDate = ""
owner2Pet1Sex = ""
owner2Pet1Weight = ""
owner2Pet1Characteristics = ""
owner2Pet1Food = ""
owner2Pet1Observations = ""
owner2Pet2Name = ""
owner2Pet2Race = ""
owner2Pet2BirthDate = ""
owner2Pet2Sex = ""
owner2Pet2Weight = ""
owner2Pet2Characteristics = ""
owner2Pet2Food = ""
owner2Pet2Observations = ""

print("¡Bienvenido!\nPor favor llene los espacios mostrados a continuación:")
userName = input("Por favor digite su nombre de usuario: ")
userPass = input("Por favor digite su contraseña: ")
if (userName == adminAcc1 and userPass == admin1Pass) or (userName == adminAcc2 and userPass == admin2Pass):
    print("Bienvenido,", userName)

    while True:
        print("\n---- MENÚ PRINCIPAL ----")
        print("1. Registros")
        print("2. Clínica")
        print("3. Venta de productos")
        print("4. Historial")
        print("5. Salir\n")
        option = input("Selecciona una opción: ")
        if option == "1":

            print("Has seleccionado la opción 1: Registros\n")

            while True:
                print("  1. Registrar Médico")
                print("  2. Registrar Dueño")
                print("  3. Registrar Mascota")
                print("  4. Volver al menú principal")
                option = input("Selecciona una opción (1-4): ")

                if option == "1":
                    print("Usted ha elegido registrar médico.")

                    print("Nota: Solo puede registrar un máximo de 3 médicos.")
                    vet1Name = input("Ingrese el nombre del médico: ")
                    vet1Code = input("Ingrese el código del médico: ")
                    vet1Specialty = input("Ingrese la especialidad del médico: ")
                    vet1PhoneNum = input("Ingrese el número de teléfono del médico: ")
                    vet1EmailAdd = input("Ingrese el correo elecrónico del médico: ")

                    while True:
                        print("\n1. Mañanas L-V.")
                        print("  2. Tardes L-V")
                        print("  3. Fines de semana S-D")
                        print("Solo puede escoger uno de los 3 horarios para este médico.")
                        scheduleOption = input("Digite el número del horario seleccionado para el médico: ")

                        if scheduleOption == "1":
                            vet1Schedule = "Mañanas L-V"
                            break
                        elif scheduleOption == "2":
                            vet1Schedule = "Tardes L-V"
                            break
                        elif scheduleOption == "3":
                            vet1Schedule = "Fines de semana S-D."
                            break
                        else:
                            print("No introdujo un valor válido, vuelva a intentar.")
                    addVet = input("Si desea registrar a otro médico digite 1, si desea salir, digite cualquier otra tecla: ")
                    if addVet == "1":
                        print("Nota: Sólo puede registrar un máximo de 3 médicos.")
                        vet2Name = input("Ingrese el nombre del médico: ")
                        vet2Code = input("Ingrese el código del médico: ")
                        vet2Specialty = input("Ingrese la especialidad del médico: ")
                        vet2PhoneNum = input("Ingrese el número de teléfono del médico: ")
                        vet2EmailAdd = input("Ingrese el correo elecrónico del médico: ")

                        while True:
                            print("\n1. Mañanas L-V.")
                            print("  2. Tardes L-V")
                            print("  3. Fines de semana S-D")
                            print("Sólo puede escoger uno de los 3 horarios para este médico.")
                            scheduleOption = input("Digite el número del horario seleccionado para el médico: ")
                            if scheduleOption == "1":
                                vet2Schedule = "Mañanas L-V"
                                if vet1Schedule != vet2Schedule:
                                    break
                                else:
                                    print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                            elif scheduleOption == "2":
                                vet2Schedule = "Tardes L-V"
                                if vet1Schedule != vet2Schedule:
                                    break
                                else:
                                    print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                            elif scheduleOption == "3":
                                vet2Schedule = "Fines de semana S-D."
                                if vet1Schedule != vet2Schedule:
                                    break
                                else:
                                    print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                            else:
                                print("No introdujo un valor válido, vuelva a intentar.")
                        addVet = input("Si desea registrar a otro médico digite 1, si desea salir, digite cualquier otra tecla: ")
                        if addVet == "1":
                            print("Nota: Sólo puede registrar un máximo de 3 médicos.")
                            vet3Name = input("Ingrese el nombre del médico: ")
                            vet3Code = input("Ingrese el código del médico: ")
                            vet3Specialty = input("Ingrese la especialidad del médico: ")
                            vet3PhoneNum = input("Ingrese el número de teléfono del médico: ")
                            vet3EmailAdd = input("Ingrese el correo elecrónico del médico: ")

                            while True:
                                print("\n1. Mañanas L-V.")
                                print("  2. Tardes L-V")
                                print("  3. Fines de semana S-D")
                                print("Sólo puede escoger uno de los 3 horarios para este médico.")
                                scheduleOption = input("Digite el número del horario seleccionado para el médico: ")
                                if scheduleOption == "1":
                                    vet3Schedule = "Mañanas L-V"
                                    if vet1Schedule != vet2Schedule != vet3Schedule:
                                        break
                                    else:
                                        print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                                elif scheduleOption == "2":
                                    vet3Schedule = "Tardes L-V"
                                    if vet1Schedule != vet2Schedule != vet3Schedule:
                                        break
                                    else:
                                        print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                                elif scheduleOption == "3":
                                    vet3Schedule = "Fines de semana S-D."
                                    if vet1Schedule != vet2Schedule != vet3Schedule:
                                        break
                                    else:
                                        print("Sólo puede asignar un horario por médico, asegúrese de no haber ingresado este horario antes.")
                                else:
                                    print("No introdujo un valor válido, vuelva a intentar.")
                        else:
                            print("Alcanzó el máximo de médicos por registrar.")
                    else:
                        print("Escogió no registrar más médicos")
                    print(vet1Name, vet1Code, vet1Specialty, vet1PhoneNum, vet1EmailAdd, vet1Schedule)
                    print(vet2Name, vet2Code, vet2Specialty, vet2PhoneNum, vet2EmailAdd, vet2Schedule)
                    print(vet3Name, vet3Code, vet3Specialty, vet3PhoneNum, vet3EmailAdd, vet3Schedule)
                elif option == "2":
                    print("Usted ha elegido registrar dueño.\n")
                    print("Nota: Sólo puede registrar un máximo de 2 dueños.\n")
                    owner1FullName = input("Ingrese el nombre completo del dueño: ")
                    owner1IDNum = input("Ingrese la cédula del dueño: ")
                    owner1PhoneNum = input("Ingrese el número de teléfono del dueño: ")
                    owner1EmailAdd = input("Ingrese el correo elecrónico del dueño: ")
                    owner1Address = input("Ingrese la dirección del dueño: ")
                    # Datos del segundo dueño
                    addOwner = input("Si desea registrar a otro dueño digite 1, si desea salir, digite cualquier otra tecla: ")
                    if addOwner == "1":
                        print("Nota: Sólo puede registrar un máximo de 2 dueños.")
                        owner2FullName = input("Ingrese el nombre completo del dueño: ")
                        owner2IDNum = input("Ingrese la cédula del dueño: ")
                        owner2PhoneNum = input("Ingrese el número de teléfono del dueño: ")
                        owner2EmailAdd = input("Ingrese el correo elecrónico del dueño: ")
                        owner2Address = input("Ingrese la dirección del dueño: ")
                    else:
                        print("Escogió no registrar más dueños")
                    print(owner1FullName, owner1IDNum, owner1PhoneNum, owner1EmailAdd, owner1Address)
                    print(owner2FullName, owner2IDNum, owner2PhoneNum, owner2EmailAdd, owner2Address)

                elif option == "3":
                    print("Usted ha elegido registrar mascotas.")
                    print("Nota: Sólo puede registrar un máximo de 2 mascotas por dueño.\n")
                    while True:
                        print("  1. Registrar mascotas para dueño 1")
                        print("  2. Registrar mascotas para dueño 2")
                        print("  3. Regresar al menú principal")
                        optionpets = input("Selecciona una opción (1-3): ")
                        if optionpets == "1":
                            owner1Pet1Name = input("Ingrese el nombre de la mascota: ")
                            owner1Pet1Race = input("Ingrese la raza de la mascota: ")
                            owner1Pet1BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                            owner1Pet1Sex = input("Ingrese el sexo de la mascota: ")
                            owner1Pet1Weight = input("Ingrese el peso de la mascota: ")
                            owner1Pet1Characteristics = input("Ingrese las características de la mascota: ")
                            owner1Pet1Food = input("Ingrese el alimento de la mascota: ")
                            owner1Pet1Observations = input("Ingrese observaciones de la mascota: ")
                            addPet = input("Si desea agregar otra mascota, presione 1, de lo contrario, digite cualquier tecla: ")
                            if addPet == "1":
                                print("Usted ha elegido registrar la mascota 2")
                                owner1Pet2Name = input("Ingrese el nombre de la mascota: ")
                                owner1Pet2Race = input("Ingrese la raza de la mascota: ")
                                owner1Pet2BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                                owner1Pet2Sex = input("Ingrese el sexo de la mascota: ")
                                owner1Pet2Weight = input("Ingrese el peso de la mascota: ")
                                owner1Pet2Characteristics = input("Ingrese las características de la mascota: ")
                                owner1Pet2Food = input("Ingrese el alimento de la mascota: ")
                                owner1Pet2Observations = input("Ingrese observaciones de la mascota: ")
                            else:
                                print("Usted decidió no agregar más mascotas al dueño 1.")
                                print(owner1Pet1Name, owner1Pet1Race, owner1Pet1BirthDate, owner1Pet1Sex,
                                      owner1Pet1Weight, owner1Pet1Characteristics, owner1Pet1Food,
                                      owner1Pet1Observations)
                                print(owner1Pet2Name, owner1Pet2Race, owner1Pet2BirthDate, owner1Pet2Sex,
                                      owner1Pet2Weight, owner1Pet2Characteristics, owner1Pet2Food,
                                      owner1Pet2Observations)
                                addOwnerpet = input("Si desea registrar mascotas al dueño 2, digite 1, de lo contrario, digite cualquier tecla: ")
                                if addOwnerpet == "1":
                                    owner2Pet1Name = input("Ingrese el nombre de la mascota: ")
                                    owner2Pet1Race = input("Ingrese la raza de la mascota: ")
                                    owner2Pet1BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                                    owner2Pet1Sex = input("Ingrese el sexo de la mascota: ")
                                    owner2Pet1Weight = input("Ingrese el peso de la mascota: ")
                                    owner2Pet1Characteristics = input("Ingrese las características de la mascota: ")
                                    owner2Pet1Food = input("Ingrese el alimento de la mascota: ")
                                    owner2Pet1Observations = input("Ingrese observaciones de la mascota: ")
                                    addPet = input("Si desea registrar mascotas al dueño 2, digite 1, de lo contrario, digite cualquier tecla: ")
                                    if addPet == "1":
                                        print("Usted ha elegido registrar la mascota 2")
                                        owner2Pet2Name = input("Ingrese el nombre de la mascota: ")
                                        owner2Pet2Race = input("Ingrese la raza de la mascota: ")
                                        owner2Pet2BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                                        owner2Pet2Sex = input("Ingrese el sexo de la mascota: ")
                                        owner2Pet2Weight = input("Ingrese el peso de la mascota: ")
                                        owner2Pet2Characteristics = input("Ingrese las características de la mascota: ")
                                        owner2Pet2Food = input("Ingrese el alimento de la mascota: ")
                                        owner2Pet2Observations = input("Ingrese observaciones de la mascota: ")
                                    else:
                                        print("Usted decidió no agregar más mascotas al dueño 2.")
                                        print(owner2Pet1Name, owner2Pet1Race, owner2Pet1BirthDate, owner2Pet1Sex,
                                              owner2Pet1Weight, owner2Pet1Characteristics, owner2Pet1Food,
                                              owner2Pet1Observations)
                                        print(owner2Pet2Name, owner2Pet2Race, owner2Pet2BirthDate, owner2Pet2Sex,
                                              owner2Pet2Weight, owner2Pet2Characteristics, owner2Pet2Food,
                                              owner2Pet2Observations)
                                else:
                                    print("Usted decidió no agregar mascotas al dueño 2.")
                                    print(owner2Pet2Name, owner2Pet2Race, owner2Pet2BirthDate, owner2Pet2Sex,
                                          owner2Pet2Weight, owner2Pet2Characteristics, owner2Pet2Food,
                                          owner2Pet2Observations)
                        elif optionpets == "2":
                            owner2Pet1Name = input("Ingrese el nombre de la mascota: ")
                            owner2Pet1Race = input("Ingrese la raza de la mascota: ")
                            owner2Pet1BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                            owner2Pet1Sex = input("Ingrese el sexo de la mascota: ")
                            owner2Pet1Weight = input("Ingrese el peso de la mascota: ")
                            owner2Pet1Characteristics = input("Ingrese las características de la mascota: ")
                            owner2Pet1Food = input("Ingrese el alimento de la mascota: ")
                            owner2Pet1Observations = input("Ingrese observaciones de la mascota: ")
                            addPet = input("Si desea agregar otra mascota al dueño 2, presione 1, de lo contrario, digite cualquier tecla")
                            if addPet == "1":
                                print("Usted ha elegido registrar la mascota 2")
                                owner2Pet2Name = input("Ingrese el nombre de la mascota: ")
                                owner2Pet2Race = input("Ingrese la raza de la mascota: ")
                                owner2Pet2BirthDate = input("Ingrese la fecha de nacimiento de la mascota: ")
                                owner2Pet2Sex = input("Ingrese el sexo de la mascota: ")
                                owner2Pet2Weight = input("Ingrese el peso de la mascota: ")
                                owner2Pet2Characteristics = input("Ingrese las características de la mascota: ")
                                owner2Pet2Food = input("Ingrese el alimento de la mascota: ")
                                owner2Pet2Observations = input("Ingrese observaciones de la mascota: ")
                            else:
                                break
                            print("Usted decidió no agregar más mascotas al dueño 2")
                            print(owner2Pet1Name, owner2Pet1Race, owner2Pet1BirthDate, owner2Pet1Sex, owner2Pet1Weight,
                                  owner2Pet1Characteristics, owner2Pet1Food, owner2Pet1Observations)
                            print(owner2Pet2Name, owner2Pet2Race, owner2Pet2BirthDate, owner2Pet2Sex, owner2Pet2Weight,
                                  owner2Pet2Characteristics, owner2Pet2Food, owner2Pet2Observations)
                        elif optionpets == "3":
                            break
                        else:
                            print("No ha ingresado un valor válido")



                elif option == "4":
                    print("Volviendo al menú principal...")
                    break


        elif option == "2":
            print("Has seleccionado la opción 2: Clínica")
        elif option == "3":
            print("Has seleccionado la opción 3: Venta de productos")
        elif option == "4":
            print("Has seleccionado la opción 4: Historial")
        elif option == "5":
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción inválida. Por favor, selecciona una opción del menú.")
else:
    print("Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")