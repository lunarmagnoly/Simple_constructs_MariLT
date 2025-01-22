ikoodid = []
arvud = []

while True:
    id_code = input("Введите личный код (или 'stop' для выхода): ")
    
    if id_code.lower() == "stop":
        break

    if len(id_code) != 11:
        print("Неверное количество цифр")
        arvud.append(id_code)
        continue

    if id_code[0] not in '123456':
        print("Первый символ должен быть 1, 2, 3, 4, 5 или 6")
        arvud.append(id_code)
        continue

    try:
        year = int(id_code[1:3])
        month = int(id_code[3:5])
        day = int(id_code[5:7])
    except ValueError:
        print("Неверный формат даты рождения")
        arvud.append(id_code)
        continue

    if not (1 <= month <= 12 and 1 <= day <= 31):
        print("Неверная дата рождения")
        arvud.append(id_code)
        continue

    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    sum_1 = sum(int(id_code[i]) * weights_1[i] for i in range(10))
    remainder_1 = sum_1 % 11

    if remainder_1 != 10:
        check_number = remainder_1
    else:
        sum_2 = sum(int(id_code[i]) * weights_2[i] for i in range(10))
        remainder_2 = sum_2 % 11
        check_number = 0 if remainder_2 == 10 else remainder_2

    if check_number != int(id_code[10]):
        print("Неверный контрольный номер")
        arvud.append(id_code)
        continue

    if id_code[0] in '12':
        year += 1800
    elif id_code[0] in '34':
        year += 1900
    else:
        year += 2000

    gender = "мужчина" if id_code[0] in '135' else "женщина"
    date_of_birth = f"{id_code[5:7]}.{id_code[3:5]}.{year}"

    hospital_code = int(id_code[7:10])
    place_of_birth = None
    if year < 2013:
        if 1 <= hospital_code <= 10:
            place_of_birth = "Kuressaare Haigla"
        elif 11 <= hospital_code <= 19:
            place_of_birth = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
        elif 21 <= hospital_code <= 220:
            place_of_birth = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
        elif 221 <= hospital_code <= 270:
            place_of_birth = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
        elif 271 <= hospital_code <= 370:
            place_of_birth = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
        elif 371 <= hospital_code <= 420:
            place_of_birth = "Narva Haigla"
        elif 421 <= hospital_code <= 470:
            place_of_birth = "Pärnu Haigla"
        elif 471 <= hospital_code <= 490:
            place_of_birth = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
        elif 491 <= hospital_code <= 520:
            place_of_birth = "Järvamaa Haigla (Paide)"
        elif 521 <= hospital_code <= 570:
            place_of_birth = "Rakvere, Tapa haigla"
        elif 571 <= hospital_code <= 600:
            place_of_birth = "Valga Haigla"
        elif 601 <= hospital_code <= 650:
            place_of_birth = "Viljandi Haigla"
        else:
            place_of_birth = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    
    if place_of_birth:
        print(f"Это {gender}, его/ее день рождения {date_of_birth} и место рождения {place_of_birth}")
    else:
        print(f"Это {gender}, его/ее день рождения {date_of_birth}, место рождения не установлено")

    ikoodid.append(id_code)

arvud.sort()
ikoodid_women = [code for code in ikoodid if code[0] in '246']
ikoodid_men = [code for code in ikoodid if code[0] in '135']
ikoodid = ikoodid_women + ikoodid_men

print("\nСписок верных личных кодов (ikoodid):", ikoodid)
print("\nСписок неверных личных кодов (arvud):", arvud)

