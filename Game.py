from random import *
print('Игра: угадай число\n')
print('Правила игры: \n'
      '1. В самом начале вы выбираете уровень сложности, от которого будет зависеть количество попыток.\n'
      ' Легкий - 15\n'
      ' Средний - 10\n'
      ' Тяжелый - 5\n'
      '2. Далее вы вводите  число до тех пор, пока у вас не закончатся попытки или не будет назван правильный ответ.\n'
      'В случае неверного ответа у вас будут даны подсказки указывающие на то в какую сторону двигаться.\n'
      'Желаем удачи!')
while True:
    print('Выберите уровеь сложности:\n'
          ' 1. Легкий - 15 попыток \n'
          ' 2. Средний - 10 попыток \n'
          ' 3. Тяжелый - 5 попыток \n')
    while True:
        try:
            ans = int(input('Введите уровень сложности (1, 2, 3): '))
            if 1 <= ans <= 3:
                break
            else:
                print('Вы ввели неправильное число')
        except ValueError:
            print('Вы ввели не целое число.')
    if ans == 1:
        attempts = 15
    elif ans == 2:
        attempts = 10
    elif ans == 3:
        attempts = 5
    play_attempts = attempts
    number = randint(1,100)
    while play_attempts:
        while True:
            try:
                player_number = int(input('Введите ваше число: '))
                if player_number <= 100 and player_number > 0:
                    break
                else:
                    print('Ваше число не попадает в диапозон (1, 100).')
            except ValueError:
                print('Вы ввели не целое число.')
        if player_number < number:
            print('Загаданное число больше вашего.')
            play_attempts -= 1
            print(f'У вас осталось {play_attempts} попыток.')
        elif player_number > number:
            print('Загаданное число меньше вашего.')
            play_attempts -= 1
            print(f'У вас осталось {play_attempts} попыток.')
        elif player_number == number:
            print(f'Вау вы угадали число за {attempts- play_attempts} попыток')
            break
    check = int(input('Желаете сыграть еще? (1 - Да, 0 - Нет).'))
    if check == 0:
        print('До свидания!')
        break