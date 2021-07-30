from random import randint as r_number

new_game = 'да'
print('Добро пожаловать в числовую угадайку')


def is_valid():
    if (n.isdigit()) and ((int(n) >= 1) and (int(n) <= border)):
        return True
    else:
        return False


while new_game == 'да':
    print('Введите границу случайного числа')
    border = int(input())  # Граница вводимая пользователем
    online = True
    number = r_number(1, border)
    counter = 0
    while online:
        print('\nМожете ввести свое число')
        n = input()
        if is_valid():
            n = int(n)
            counter += 1
            if n < number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                if n == number:
                    print('\nВы угадали, поздравляем!\nВаше общее количество попыток: ', counter,
                          '\n\nСпасибо, что играли в числовую угадайку.\n\nХотите сыграть еще?\t(Чтобы начать заново, введите  \'да\')')
                    new_game = input()
                    if new_game == 'да':
                        counter = 0
                        break
        else:
            print('А может быть все-таки введем целое число от 1 до,', border, '?')