from MyModule import *

paroolid = []  # Список для паролей
kasutajad = []  # Список для имен пользователей

while True:
    print("\nVali tegevus:")
    actions = [
        "Registreerimine", "Autoriseerimine", "Unustanud parooli taastamine", "Lõpetamine"
    ]

    for i in range(len(actions)):
        print(f"{i + 1}. {actions[i]}")
    try:
        choice = int(input("\nSisesta tegevuse number: ")) - 1
    except ValueError:
        print("Vale sisestus. Palun sisestage number.")
        continue

    if choice == 0:
        nimi = input("Sisestage nimi: ")
        if nimiKontroll(nimi, kasutajad):
            print("\nNimi on juba kasutusel.\n")
        else:
            print("\nValige parooli loomise viis:")
            print("1. Sisestan ise")
            print("2. Genereeritud parool")

            try:
                parool_choice = int(input("\nSisesta valiku number: ")) - 1
                if parool_choice == 0:
                    while True:
                        parool = input("Sisestage parool: ")
                        if parooliKontroll(parool):
                            registreerimine(nimi, parool, kasutajad, paroolid)
                            print("\nRegistreerimine on õnnestunud.\n")
                            break
                        else:
                            print("\nParool peab sisaldama vähemalt 8 sümbolit, sealhulgas numbrid, suured ja väiksed tähed ja spetsiaalset sümbolit.\n")
                elif parool_choice == 1:
                    parool = salasona(12)
                    registreerimine(nimi, parool, kasutajad, paroolid)
                    print(f"\nTeie automaatselt genereeritud parool: {parool}")
                    print("\nRegistreerimine on õnnestunud.\n")
                else:
                    print("Vale valik. Palun valige uuesti.")
            except ValueError:
                print("Vale sisestus. Palun sisestage number.")

    elif choice == 1:
        nimi = input("Sisestage nimi: ")
        parool = input("Sisestage parool: ")
        if autoriseerimine(nimi, parool, kasutajad, paroolid):
            print("\nEdukalt sisse logitud.\n")
        else:
            print("\nVale kasutajanimi või parool.\n")

    elif choice == 2:
        nimi = input("Sisestage nimi: ")
        if nimiKontroll(nimi, kasutajad):
            uus_parool = input("Sisestage uus parool: ")
            if unustanudParooliTaastamine(nimi, uus_parool, kasutajad, paroolid):
                print("\nParool on edukalt uuendatud.\n")
            else:
                print("\nViga parooli uuendamisel.\n")
        else:
            print("\nKasutajat ei leitud.\n")

    elif choice == 3:
        print("\nProgramm on lõppenud.\n")
        break

    else:
        print("\nVale valik. Palun valige uuesti.\n")
