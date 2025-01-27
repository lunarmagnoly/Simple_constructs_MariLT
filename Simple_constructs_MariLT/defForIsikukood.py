def isikukoodPikkusTrue(isikukood: str)->bool:
    """
    Проверяет длинну isikukood, должно быть 11 чисел в строке и то что знаки в строке числа
    :param isikukood: Личный код (должен быть строкой из 11 цифр).
    :rtype: bool 
    """
    return len(isikukood) == 11 and isikukood.isdigit()

def isikukoodiEsimeneNumber(isikukood: str)->bool:
    """
    Проверяет длинну первую цифру isikukood
    Если 1-8, то True
    :param isikukood: Личный код (должен быть строкой из 11 цифр).
    :rtype: bool 
    """
    return isikukood[0] in '12345678'

def onKuupaev(isikukood: str) -> bool:
    """
    Проверяет подлинность даты в isikukood
    
    :param isikukood: Личный код (должен быть строкой из 11 цифр).
    :rtype: bool 
    """
    year = int(isikukood[1:3])
    month = int(isikukood[3:5])
    day = int(isikukood[5:7])

    # Проверка корректности месяца и дня
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False

    # Проверка дней в месяцах
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        return True
    elif month in [4, 6, 9, 11] and 1 <= day <= 30:
        return True
    elif month == 2:
        # Проверка високосного года
        if year % 4 == 0 and 1 <= day <= 29:
            return True
        elif year % 4 != 0 and 1 <= day <= 28:
            return True
    
    return False

def isikukoodKontrollNumber(isikukood: str) -> bool:
    """
    Проверяет подлинность isikukood на основе контрольного числа.

    :param isikukood: Личный код (должен быть строкой из 11 цифр).
    :rtype: bool(True, если контрольное число верное, иначе False.)
    """
    # Проверка длины личного кода
    if len(isikukood) != 11 or not isikukood.isdigit():
        return False

    # Весовые коэффициенты
    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    # Вычисление первой суммы
    summa_1 = sum(int(isikukood[i]) * weights_1[i] for i in range(10))
    jaak_1 = summa_1 % 11

    # Если остаток меньше 10, это контрольное число
    if jaak_1 != 10:
        kontroll_number = jaak_1
    else:
        # Вычисление второй суммы
        summa_2 = sum(int(isikukood[i]) * weights_2[i] for i in range(10))
        jaak_2 = summa_2 % 11
        kontroll_number = 0 if jaak_2 == 10 else jaak_2

    # Сравнение расчетного контрольного числа с последней цифрой кода
    return kontroll_number == int(isikukood[10])

def valeIsikukoodNimikirja(isikukood: str, arvud: list) -> list:
    """
    Добавляет неверный личный код в список arvud, если он не проходит проверки.

    :param isikukood: Личный код (строка из 11 цифр).
    :param arvud: Список для записи неверных кодов.
    :rtype: list. Обновленный список arvud.
    """
    # Проверяем, проходит ли код все проверки
    if (not isikukoodKontrollNumber(isikukood) or
        not onKuupaev(isikukood) or
        not isikukoodiEsimeneNumber(isikukood) or
        not isikukoodPikkusTrue(isikukood)):
        arvud.append(isikukood)  # Добавляем неверный код в список

    return arvud

def getYear(isikukood: str) -> int:
    """
    Определяет год рождения на основе первой цифры личного кода.

    :param isikukood: Личный код (строка из 11 цифр).
    :rtype: year int
    """
    # Извлекаем последние две цифры года из личного кода
    year_part = int(isikukood[1:3])

    # Определяем столетие по первой цифре личного кода
    if isikukood[0] in '12':
        year = 1800 + year_part
    elif isikukood[0] in '34':
        year = 1900 + year_part
    elif isikukood[0] in '56':
        year = 2000 + year_part
    elif isikukood[0] in '78':
        year = 2100 + year_part
    else:
        raise ValueError("Неверная первая цифра личного кода")

    return year


def getDate(isikukood: str) -> str:
    """
    Определяет день рождения.

    :param isikukood: Личный код (строка из 11 цифр).
    :rtype: День рождения
    """
    if onKuupaev(isikukood): 
        month = isikukood[3:5]
        day = isikukood[5:7]
        return f"{day}.{month}.{getYear(isikukood)}"

def getGender(isikukood: str) -> str:
    """
    Определяет пол на основе первой цифры личного кода.

    :param isikukood: Личный код (строка из 11 цифр).
    :return: "мужчина", если первая цифра 1, 3, 5 или 7, иначе "женщина".
    """
    return "мужчина" if isikukood[0] in '1357' else "женщина"
    
def getSunnikoht(isikukood: str) -> str:
    """
    Определяет место рождения на основе личного кода.

    :param isikukood: Личный код (строка из 11 цифр).
    :return: Место рождения (строка).
    """
    # Извлечение кода больницы из личного кода
    hospital_code = int(isikukood[7:10])
    
    # Получаем год рождения
    year = getYear(isikukood)
    
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
    else:
        place_of_birth = "не установлено"
    return place_of_birth

def korrektneIsikukoodNimikirja(isikukood: str, ikoodid: list) -> list:
    """
    Добавляет верный личный код в список ikoodid, если он проходит все проверки.

    :param isikukood: Личный код (строка из 11 цифр).
    :param ikoodid: Список для записи верных кодов.
    :return: Обновленный список ikoodid.
    """
    # Проверяем, проходит ли код все проверки
    if (isikukoodKontrollNumber(isikukood) and
        onKuupaev(isikukood) and
        isikukoodiEsimeneNumber(isikukood) and
        isikukoodPikkusTrue(isikukood)):
        ikoodid.append(isikukood)  # Добавляем верный код в список

    return ikoodid
