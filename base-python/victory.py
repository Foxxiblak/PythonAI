def victory():
    count_questions = 10
    correct_answer = 0
    incorrect_answer = 0

    q_1 = 'Введите год рождения Альберта Эйнштейна: ' #1879
    q_2 = 'Введите год рождения Джеймса Максвелла: ' #1831
    q_3 = 'Введите год рождения Чарльза Дарвина: ' #1809
    q_4 = 'Введите год рождения Марии Складовской-Кюри: ' #1867
    q_5 = 'Введите год рождения Никола Тесла: ' #1856
    q_6 = 'Введите год рождения Нильса Бора: ' #1885
    q_7 = 'Введите год рождения Дмитрия Менделеева: ' #1834
    q_8 = 'Введите год рождения Галилео Галилея: ' #1564
    q_9 = 'Введите год рождения Луи Пастера: ' #1822
    q_10 = 'Введите год рождения Джеймса Максвелла: ' #1831

    a_1 = '1879'
    a_2 = '1831'
    a_3 = '1809'
    a_4 = '1867'
    a_5 = '1856'
    a_6 = '1885'
    a_7 = '1834'
    a_8 = '1564'
    a_9 = '1822'
    a_10 = '1831'

    yaer_1 = input(q_1)
    yaer_2 = input(q_2)
    yaer_3 = input(q_3)
    yaer_4 = input(q_4)
    yaer_5 = input(q_5)
    yaer_6 = input(q_6)
    yaer_7 = input(q_7)
    yaer_8 = input(q_8)
    yaer_9 = input(q_9)
    yaer_10 = input(q_10)

    if yaer_1 == a_1:
        correct_answer += 1
    if yaer_2 == a_2:
        correct_answer += 1
    if yaer_3 == a_3:
        correct_answer += 1
    if yaer_4 == a_4:
        correct_answer += 1
    if yaer_5 == a_5:
        correct_answer += 1
    if yaer_6 == a_6:
        correct_answer += 1
    if yaer_7 == a_7:
        correct_answer += 1
    if yaer_8 == a_8:
        correct_answer += 1
    if yaer_9 == a_9:
        correct_answer += 1
    if yaer_10 == a_10:
        correct_answer += 1

    incorrect_answer = count_questions - correct_answer
    print('-.'*50)
    print(f'Правильные ответы: {correct_answer}/{count_questions}')
    print(f'Количество ошибок: {incorrect_answer}/{count_questions}')
    print('Процент правильных ответов: ', (correct_answer/count_questions)*100, end='%\n')
    print('Процент неправильных ответов: ', (incorrect_answer/count_questions)*100, end='%\n')

again = True
while again:
    victory()
    print('-.' * 50)
    again = input("Сыграем снова? Да/Нет ")
    again = again.lower()
    if again == 'нет':
        again = False