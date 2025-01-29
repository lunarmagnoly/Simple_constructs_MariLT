import re
import random
import string

def nimiKontroll(nimi: str, kasutajad: list) -> bool:
    """
    Проверяет, есть ли указанное имя в списке пользователей.

    :param nimi: Строка с именем.
    :param kasutajad: Список с именами пользователей.
    :rtype: bool
    """
    return nimi in kasutajad

def registreerimine(nimi: str, parool: str, kasutajad: list, paroolid: list) -> None:
    """
    Регистрирует нового пользователя, добавляя его имя и пароль в списки.

    :param nimi: Строка с именем.
    :param parool: Строка с паролем.
    :param kasutajad: Список с именами пользователей.
    :param paroolid: Список с паролями пользователей.
    """
    kasutajad.append(nimi)
    paroolid.append(parool)

def autoriseerimine(nimi: str, parool: str, kasutajad: list, paroolid: list) -> bool:
    """
    Авторизует пользователя, проверяя имя и пароль.

    :param nimi: Строка с именем.
    :param parool: Строка с паролем.
    :param kasutajad: Список с именами пользователей.
    :param paroolid: Список с паролями пользователей.
    :rtype: bool
    """
    if nimi in kasutajad:
        index = kasutajad.index(nimi)
        return paroolid[index] == parool
    return False

def unustanudParooliTaastamine(nimi: str, uus_parool: str, kasutajad: list, paroolid: list) -> bool:
    """
    Восстанавливает пароль пользователя.

    :param nimi: Строка с именем.
    :param uus_parool: Строка с новым паролем.
    :param kasutajad: Список с именами пользователей.
    :param paroolid: Список с паролями пользователей.
    :rtype: bool
    """
    if nimi in kasutajad:
        index = kasutajad.index(nimi)
        paroolid[index] = uus_parool
        return True
    return False



def parooliKontroll(parool: str) -> bool:
    """
    Проверяет, содержит ли пароль цифры, буквы в нижнем и верхнем регистре и специальные символы.

    :param parool: Строка с паролем.
    :rtype: bool 
    """
    if (len(parool) >= 8 and
        re.search(r"\d", parool) and
        re.search(r"[a-z]", parool) and
        re.search(r"[A-Z]", parool) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", parool)):
        return True
    return False


def salasona(k: int):
 """
    Генерирует случайный пароль длиной k, содержащий цифры и буквы.

    :param k: Длина пароля.
    :rtype: str
 """
 sala = ""
 for i in range(k):
        t = random.choice(string.ascii_letters)
        num = random.choice('0123456789')
        t_num = [t, str(num)]
        sala += random.choice(t_num)
 return sala
    
