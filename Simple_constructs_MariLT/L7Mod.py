def summa3(arv1:int,arv2:int, arv3: int)->int:
    """
    Tagastab kolme täisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int
    """
    summa = arv1+arv2+arv3

    return summa
def arithmetic(a:float,b:float, o: str )->any:
    """
    Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine

    :param float a: arv1
    :param float b: arv2
    :param str o: arithmetic operation
    :rtype: var any type
    """

    if o in ["+", "-", "*", "/"]:
        if b==0 and 0=="/":
            vastus = "DIV/0"
        else:
            vastus=eval(str(a)+o+str(b))
    else:
        vastus="Tundmatu tehe"
    
    return vastus

def is_year_leap(year:int)->bool:
    """
    Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int year: year  number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if year%4==0:
        v=True

    else:
        v=False
    return v

def square(a: float)->float:

    """
    Написать функцию square, принимающую 1 аргумент — сторону квадрата, и 
    возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.
    """
    P=a*4
    S = a^2
    d = a * 2^(1/2)

    return P, S, d

def season (month: int)->str:
    """ Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и 
    возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis). """
    if month==[12,1,2]:
        season="talv"
    elif month==[3,4,5]:
        season="kevad"
    elif month==[6,7,8]:
        season="suvi"
    elif month==[9,10,11]:
        season="sügis"
    else:
        season="Kuu peab olema integer"
    return season

def bank(a: float, years: int) ->float:
    """ Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых 
    (каждый год размер его вклада увеличивается на 10%. 
    Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
    Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя. 
    """
    intress=10/100
    for _ in range(years):
        a += a * intress
    return a
def is_prime(n:int) ->bool:
    """
    Функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
    """
    if n < 0 or n > 1000:
        raise ValueError("Число должно быть в диапазоне от 0 до 1000.")
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def date(day:int, month, year)->bool:
    """
    Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
    Вернуть True, если такая дата есть в нашем календаре, и False иначе.
    
    """
    if 1 <= day <= 31 and month in [1,3,5,7,8, 10 ,12] and year >0 :
        v=True
    elif 1 <= day <= 30 and month in [4,6,9,11] and year >0:
        v=True
    elif 1 <= day <= 28 and month in 2 and year%4!=0 and year >0:
        v=True
    elif 1 <= day <= 29 and month in 2 and year%4==0 and year >0:
        v=True
    else:
        v=False

    return v


