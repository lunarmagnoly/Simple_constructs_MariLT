#Task 0(skeem v3_2.jpeg) 
#Программу написаную на уроке по блок схемам: https://moodle.edu.ee/mod/assign/view.php?id=469362 прикрепите как ответ на задание.

from datetime import datetime

# enter current date
current_date = datetime.now()

# ask user to enter the start date in the format DD-MM-YYYY 
start_date_str = input("Enter the start date (DD.MM.YYYY): ") 
start_date = datetime.strptime(start_date_str, "%d.%m.%Y")

# Calculate the number of years between the start date and the current date
H = (current_date - start_date).days // 365

# Ask user to enter the initial deposit amount and annual interest rate
Y = float(input("Enter the initial deposit amount in dollars: "))
Z = float(input("Enter the annual interest rate (in %): "))

# Calculate the accumulated sum
if H > 0 and Y > 0 and Z > 0:
    accumulated_sum = Y + (Y * H * Z / 100)
    print(f"Vlad on kogunenud {accumulated_sum:.2f} dollarit")
else:
    print("Invalid input. Please ensure all values are greater than 0.")

#Task 1
# Определить и вывести максимальное из N вводимых пользователем чисел.
# Запрашиваем количество чисел
N = int(input("Введите количество чисел: "))

# Проверяем, что количество чисел больше 0
if N > 0:
    # Инициализируем переменную для максимального числа
    max_number = None

    # Ввод чисел и нахождение максимального числа
    for i in range(N):
        number = float(input(f"Введите число {i+1}: "))
        if max_number is None or number > max_number:
            max_number = number

    # Выводим максимальное число
    print(f"Максимальное число: {max_number}")
else:
    print("Количество чисел должно быть больше 0.")

#Task 2
#Написать программу, которая бы запрашивала целые числа и распечатывала любые значение, кроме13. Если заданное число равно13, вместо него печатается число 77.

while True:
    user_input = input("Введите целое число (или введите 'выход' для выхода): ")

    # Проверка на выход из программы
    if user_input.lower() == 'выход':
        break

    # Проверка вводимых данных
    try:
        number = int(user_input)
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
        continue

    # Проверка числа
    if number == 13:
        print(77)
    else:
        print(number)

#Task 3 
#Начав тренировки, спортсмен в первый день пробежал 10 км. 
#Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. 
#Какой суммарный путь пробежит спортсмен за 7 дней?

# Инициализируем переменные
distance = 10  # первый день
total_distance = 0

# Рассчитываем суммарный путь за 7 дней
for day in range(1, 8):
    total_distance += distance
    distance += distance * 0.10  # увеличение дневной нормы на 10%

# Выводим результат
print(f"Суммарный путь, который пробежит спортсмен за 7 дней: {total_distance:.2f} км")

#Task 4 
# Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. 
# Все данные по использованию ткани заносятся в компьютер. Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется и предложить выкупить остаток. 
# Если пользователь согласен, то продается последний кусок и программа заканчивает работу, если нет, то переходим к следующиму покупателю.
# Инициализация переменной для хранения длины ткани
M = float(input("Введите длину ткани в метрах: "))

while True:
    # Запрос длины требуемого куска ткани
    requested_length = input("Введите длину требуемого куска ткани (или введите 'выход' для выхода): ")

    if requested_length.lower() == 'выход':
        print("Программа завершена.")
        break

    try:
        requested_length = float(requested_length)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        continue

    if requested_length > M:
        print("Материала не хватает.")
        buyout = input("Хотите выкупить остаток ткани? (да/нет): ").strip().lower()
        if buyout == 'да':
            print(f"Выкуплен остаток ткани длиной {M:.2f} метров.")
            break
        else:
            print("Переход к следующему покупателю.")
    else:
        M -= requested_length
        print(f"Осталось {M:.2f} метров ткани.")

#Task 5
# Составьте программу для вычисления площади трапеций до тех пор пока пользователь не откажется вычислать.

while True:
    try:
        # Запрашиваем длины оснований и высоту трапеции
        a = float(input("Введите длину первого основания (a): "))
        b = float(input("Введите длину второго основания (b): "))
        h = float(input("Введите высоту (h): "))
        
        # Проверяем введенные значения
        if a <= 0 or b <= 0 or h <= 0:
            print("Длины оснований и высота должны быть больше нуля. Пожалуйста, попробуйте снова.")
            continue

        # Вычисляем площадь трапеции
        S = (a + b) * h / 2
        print(f"Площадь трапеции: {S:.2f} квадратных единиц")

        # Спрашиваем пользователя, хочет ли он продолжить вычисления
        continue_calculation = input("Хотите вычислить площадь еще одной трапеции? (да/нет): ").strip().lower()
        if continue_calculation != 'да':
            print("Программа завершена.")
            break
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")

#Task 6
#Составьте программу, проверяющую, верно ли утверждение, что введенное вами целое число делится без остатка на 3.

while True:
    user_input = input("Введите целое число (или введите 'выход' для выхода): ")

    if user_input.lower() == 'выход':
        print("Программа завершена.")
        break

    try:
        number = int(user_input)
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
        continue

    if number % 3 == 0:
        print(f"Число {number} делится на 3 без остатка.")
    else:
        print(f"Число {number} не делится на 3 без остатка.")



