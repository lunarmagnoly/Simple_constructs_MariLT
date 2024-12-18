print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => "))))
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga ei saa midagi teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu on ")
    print()
    c=b=a
    paaris =0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10     # единицы числа
        a = a // 10     # десятки числа
        b = b * 10
        b += number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    # if c % 2 == 0:
    #     print(f"{c} - Paaris arv. Jagame 2.")
    # else:
    #     print(f"{c} - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
        if c % 2 == 0:
            print('{:>4}'.format(round(c))," - Paaris arv. Jagame 2.")
            c = c / 2
        else:
             print('{:>4}'.format(round(c))," - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
             c = (3*c + 1) / 2
                
    print()
    print('{:>4}'.format(round(c))," - Teoreem on tõestatud")