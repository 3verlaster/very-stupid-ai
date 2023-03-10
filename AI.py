import random

# Список приветственных фраз
greetings = ['привет', 'здравствуй', 'ку', 'добрый день', 'приветствую', 'здорово', 'здравствуйте']

# Список вопросительных фраз
questions = ['как дела?', 'как ты?', 'как поживаешь?', 'чем занимаешься?', 'что нового?', 'что интересного?', 'какие планы на день?']

# Список ответов на вопросы
question_responses = ['неплохо, а у тебя?', 'обычно, спасибо', 'в основном работаю', 'ничего особенного, а у тебя?', 'много всего', 'планирую...', 'собираюсь...']

# Список фраз для ответа на "нормально"
fine_responses = ['это замечательно!', 'рад это слышать!', 'отлично!', 'круто!', 'прекрасно!']

# Список фраз для ответа на "плохо"
not_fine_responses = ['очень жаль!', 'надеюсь, что все наладится', 'сочувствую', 'бывают такие дни']

# Список прощальных фраз
goodbyes = ['до свидания', 'увидимся', 'пока', 'всего доброго']

# Список фраз для ответа на "спасибо"
thank_responses = ['Всегда рад помочь!', 'Не за что!', 'Рад был помочь!', 'Обращайтесь!', 'Вам спасибо!']

# Главный цикл обработки сообщений
while True:
    # Получаем сообщение от пользователя
    message = input('Вы: ').lower()

    # Обработка приветственных фраз
    if message in greetings:
        response = random.choice(greetings).capitalize() + '!'
    # Обработка вопросительных фраз
    elif message in questions:
        response = random.choice(question_responses)
    # Обработка ответа "нормально"
    elif 'нормально' in message:
        response = random.choice(fine_responses)
    # Обработка ответа "плохо"
    elif 'плохо' in message:
        response = random.choice(not_fine_responses)
    # Обработка сообщения "спасибо"
    elif 'спасибо' in message:
        response = random.choice(thank_responses)
    # Обработка прощальных фраз
    elif message in goodbyes:
        response = random.choice(goodbyes).capitalize() + '!'
        print(response)
        break
    # Обработка неизвестных сообщений
    else:
        response = 'Извините, я вас не понимаю.'

    # Выводим ответ ИИ
    print('ИИ:', response)
