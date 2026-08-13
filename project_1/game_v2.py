"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import random

import numpy as np


def game_core_v3(number: int = 70) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число по умолчанию 70.

    Returns:
        int: Число попыток
    """
    count = 0
    low_number = 1 
    high_number = 100 
    
    ##  Делаем бесконечный цикл. Увеличиваем счетчик. 
    ##  Угадываемое число равно нижняя граница + верхняя граница делить на 2
    ##  если наше угадываемое число больше загадонного
    ##  верхняя граница будет равна угадываемому числу - 1. то же самое с нижней
    ##  если число меньше
    
    while True: 
        count += 1 
        predict = (low_number + high_number) // 2 
        if predict == number: 
            break
        elif predict > number: 
            high_number = predict - 1 
        else:
            low_number = predict + 1
    return count

## Делаем список. Загадываем 1000 чисел от 0 до 101,
## затем делаем цикл из этого списка и каждый элемент вызываем в функции game_core_v3,
## чтобы узнать с какой попытки угадываем
## добавляем счетчик угадываний в список count_ls
## В переменной score считаем среднее арифм из 1000 счетчиков

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
