brackets_string = str(input('Введите структуру из скобок: '))
wrong_bracket_index = 0
check = 0
for i in range(len(brackets_string)):
    if brackets_string[i] == '(':
        check += 1
        if check == 1:
            wrong_bracket_index = i
    else:
        check -= 1
    if check == -1:
        print('Первая лишняя закрытая скобка под индексом ' + str(i))
        break
if check == 0:
    print('Структура из скобок верная')
if check > 0:
    print('Первая лишняя открытая скобка под индексом ' + str(wrong_bracket_index))
