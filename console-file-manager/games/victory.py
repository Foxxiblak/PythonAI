import random

count_questions = 5
correct_answer = 0
incorrect_answer = 0

q_1 = 'Введите дату рождения Альберта Эйнштейна: '  # 14.03.1879
q_2 = 'Введите дату рождения Джеймса Максвелла: '  # 13.06.1831
q_3 = 'Введите дату рождения Чарльза Дарвина: '  # 12.02.1809
q_4 = 'Введите дату рождения Марии Складовской-Кюри: '  # 07.11.1867
q_5 = 'Введите дату рождения Никола Тесла: '  # 07.01.1856
q_6 = 'Введите дату рождения Нильса Бора: '  # 07.10.1885
q_7 = 'Введите дату рождения Дмитрия Менделеева: '  # 08.02.1834
q_8 = 'Введите дату рождения Галилео Галилея: '  # 15.02.1564
q_9 = 'Введите дату рождения Луи Пастера: '  # 27.12.1822
q_10 = 'Введите дату рождения Джеймса Максвелла: '  # 13.06.1831

a_1 = '14.03.1879'
a_2 = '13.06.1831'
a_3 = '12.02.1809'
a_4 = '07.11.1867'
a_5 = '07.01.1856'
a_6 = '07.10.1885'
a_7 = '08.02.1834'
a_8 = '15.02.1822'
a_9 = '27.12.1822'
a_10 = '13.06.1831'

result = []
def gen_question():
    numbers = range(0, 10)
    return random.sample(numbers, count_questions)

questions = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
answers = [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10]

def get_date(date):
    date_str = date.split('.')
    month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    month_num = int(date_str[1])-1
    month_word = month[month_num]
    return (date_str[0] + ' ' + month_word + ' ' + date_str[-1])

def victory():
    result = gen_question()
    for i in result:
        bth = input(questions[i])
        print("Верно!" if bth == answers[i] else "Неверно! Правильный ответ: ", get_date(answers[i]))

    incorrect_answer = count_questions - correct_answer
    print('-.'*50)
    print(f'Правильные ответы: {correct_answer}/{count_questions}')
    print(f'Количество ошибок: {incorrect_answer}/{count_questions}')


def start_game():
    again = True
    while again:
        victory()
        print('-.' * 50)
        again = input("Сыграем снова? Да/Нет ")
        again = again.lower()
        if again == 'нет':
            again = False