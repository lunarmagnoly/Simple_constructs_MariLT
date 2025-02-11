import random

# Загрузка вопросов и ответов из файла
def load_questions(filename):
    kus_vas = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Убедимся, что строка содержит символ ':'
                if ':' in line:
                    question, answer = line.strip().split(':', 1)  # Разделяем только по первому ':'
                    kus_vas[question] = answer
                else:
                    print(f"Ignoring invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return kus_vas

# Проведение опроса кандидатов
def interview_candidates(kus_vas):
    vastuvõetud = []  # Список успешных кандидатов
    eisobi = []       # Список неуспешных кандидатов

    while len(vastuvõetud) < 5:  # Пока не набрано 5 успешных кандидатов
        name = input("Sisesta kandidaadi nimi: ")
        correct_answers = 0

        # Выбор 5 случайных вопросов
        questions = random.sample(list(kus_vas.keys()), 5)

        for question in questions:
            answer = kus_vas[question]
            user_answer = input(f"{name}, {question}: ")
            if user_answer.lower() == answer.lower():
                correct_answers += 1

        # Обработка результатов
        if correct_answers >= 3:
            vastuvõetud.append((name, correct_answers))
        else:
            eisobi.append((name, correct_answers))

    return vastuvõetud, eisobi

# Сохранение результатов в файл
def save_results(vastuvõetud, eisobi):
    # Сортировка успешных кандидатов по количеству правильных ответов
    vastuvõetud.sort(key=lambda x: x[1], reverse=True)
    with open('vastuvõetud.txt', 'w', encoding='utf-8') as file:
        for name, score in vastuvõetud:
            file.write(f"{name}: {score}\n")

    # Сортировка неуспешных кандидатов по имени
    eisobi.sort(key=lambda x: x[0])
    with open('eisobi.txt', 'w', encoding='utf-8') as file:
        for name, score in eisobi:
            file.write(f"{name}: {score}\n")

# Вывод результатов в Shell
def print_results():
    print("Vastuvõetud kandidaadid:")
    with open('vastuvõetud.txt', 'r', encoding='utf-8') as file:
        print(file.read())

    print("Eisobi kandidaadid:")
    with open('eisobi.txt', 'r', encoding='utf-8') as file:
        print(file.read())