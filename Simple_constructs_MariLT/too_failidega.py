# Импорт функций из модуля interview_module
import interview_module

# Основная программа
if __name__ == "__main__":
    # Загрузка вопросов и ответов
    kus_vas = interview_module.load_questions('kusimused_vastused.txt')

    # Проведение опроса
    vastuvõetud, eisobi = interview_module.interview_candidates(kus_vas)

    # Сохранение результатов
    interview_module.save_results(vastuvõetud, eisobi)

    # Вывод результатов
    interview_module.print_results()