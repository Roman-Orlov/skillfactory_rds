def game_core(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    min_d=1
    max_d=100
    predict = int((max_d-min_d)/2)
    if number == min_d or number == max_d:
        return (1)
    while number != predict:
        count+=1
        if number > predict:
            min_d = predict
            predict = min_d+int((max_d-min_d)/2)
        elif number < predict:
            max_d = predict
            predict = max_d-int((max_d-min_d)/2)
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

import numpy as np

# Проверяем
score_game(game_core)
