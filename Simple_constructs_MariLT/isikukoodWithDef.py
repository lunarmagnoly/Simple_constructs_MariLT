from defForIsikukood import *
ikoodid = []
arvud = []
while True:
    try:
        isikukood=input("Sisetage isikukood. Lõpetamiseks siseta 'stopp' ")
        if isikukood.lower() == "stopp":
            break
        if korrektneIsikukood(isikukood):
            print(f"See inimene on {getGender(isikukood)}. Tema sünnipäev on {getDate(isikukood)} ja sünnikoht on {getSunnikoht(isikukood)}") 
            korrektneIsikukoodNimikirja(isikukood, ikoodid)
            print("Korrektsed isikukoodid:", ikoodid)
        else:
            valeIsikukoodNimikirja(isikukood, arvud) and isikukoodIsDigit(isikukood)
            print("Arvud, mis ei ole isikukoodid", arvud)
    except ValueError:
        print("Viga sisestamisel: isikukood peab olema 11 numbrit.")

