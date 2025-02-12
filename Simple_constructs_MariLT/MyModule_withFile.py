from email.message import EmailMessage
import re
import random
import string
import smtplib, ssl

def nimiKontroll(nimi: str, kasutajad: str) -> bool:
    """
    Проверяет, есть ли указанное имя в файле пользователей.
    :param nimi: Строка с именем.
    :param kasutajad: Имя файла с именами пользователей.
    :return: True, если имя уже существует, иначе False.
    """
    try:
        with open(kasutajad, 'r', encoding='utf-8') as file:
            kasutajad_list = file.read().splitlines()
        return nimi in kasutajad_list
    except FileNotFoundError:
        print(f"Файл {kasutajad} не найден.")
        return False

def registreerimine(nimi: str, parool: str, kasutajad: str, paroolid: str) -> None:
    """
    Регистрирует нового пользователя, добавляя его имя и пароль в файлы.
    :param nimi: Строка с именем.
    :param parool: Строка с паролем.
    :param kasutajad: Имя файла с именами пользователей.
    :param paroolid: Имя файла с паролями пользователей.
    """
    try:
        with open(kasutajad, 'a', encoding='utf-8') as kasutajad_file:
            kasutajad_file.write(nimi + '\n')
        with open(paroolid, 'a', encoding='utf-8') as paroolid_file:
            paroolid_file.write(parool + '\n')
        saada_kiri(nimi, parool)
    except FileNotFoundError:
        print(f"Один из файлов {kasutajad} или {paroolid} не найден.")

def autoriseerimine(nimi: str, parool: str, kasutajad: str, paroolid: str) -> bool:
    """
    Авторизует пользователя, проверяя имя и пароль.
    :param nimi: Строка с именем.
    :param parool: Строка с паролем.
    :param kasutajad: Файл с именами пользователей.
    :param paroolид: Файл с паролями пользователей.
    :return: True, если авторизация успешна, иначе False.
    """
    try:
        with open(kasutajad, 'r', encoding='utf-8') as kasutajad_file, \
             open(paroolid, 'r', encoding='utf-8') as paroolid_file:
            for kasutaja, parool_line in zip(kasutajad_file, paroolid_file):
                if kasutaja.strip() == nimi and parool_line.strip() == parool:
                    return True
        return False
    except FileNotFoundError:
        print(f"Один из файлов {kasutajad} или {paroolid} не найден.")
        return False

def unustanudParooliTaastamine(nimi: str, uus_parool: str, kasutajad: str, paroolid: str) -> bool:
    """
    Восстанавливает пароль пользователя.
    :param nimi: Строка с именем.
    :param uus_parool: Строка с новым паролем.
    :param kasutajad: Файл с именами пользователей.
    :param paroolид: Файл с паролями пользователей.
    :return: True, если пароль успешно обновлён, иначе False.
    """
    if not nimiKontroll(nimi, kasutajad):
        print(f"Пользователь {nimi} не найден.")
        return False
    try:
        with open(kasutajad, 'r', encoding='utf-8') as kasutajad_file:
            kasutajad_list = kasutajad_file.read().splitlines()
        with open(paroolid, 'r', encoding='utf-8') as paroolid_file:
            paroolid_list = paroolid_file.read().splitlines()

        kasutajad_dict = dict(zip(kasutajad_list, paroolid_list))

        if nimi in kasutajad_dict:
            kasutajad_dict[nimi] = uus_parool
            with open(paroolid, 'w', encoding='utf-8') as paroolid_file:
                for user, pwd in kasutajad_dict.items():
                    paroolid_file.write(pwd + '\n')
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"Один из файлов {kasutajad} или {paroolid} не найден.")
        return False

def parooliKontroll(parool: str) -> bool:
    """
    Проверяет, соответствует ли пароль требованиям.
    :param parool: Строка с паролем.
    :return: True, если пароль соответствует требованиям, иначе False.
    """
    if (len(parool) >= 8 and
        re.search(r"\d", parool) and
        re.search(r"[a-z]", parool) and
        re.search(r"[A-Z]", parool) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", parool)):
        return True
    return False

def salasona(pikkus: int) -> str:
    """
    Генерирует случайный пароль заданной длины.
    :param pikkus: Длина пароля.
    :return: Строка с паролем.
    """
    tähed = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(tähed) for _ in range(pikkus))

def saada_kiri(nimi: str, parool: str):
    """
    Отправляет электронное письмо с информацией о регистрации.
    :param nimi: Имя пользователя.
    :param parool: Пароль пользователя.
    """
    kellele = input("Kellele: ")
    kiri = f"Sa oled registreeritud. Sinu kasutajanimi on {nimi}, sinu salasona on {parool}"
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mary.luna.tey@gmail.com"
    password = input("Enter app password: ")
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "E-kiri saatmine"
    msg['From'] = "Mari"
    msg['To'] = kellele
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        print("Informatsioon: Kiri oli saadetud")
    except Exception as e:
        print("Tekkis viga!", e)
    finally:
        server.quit()