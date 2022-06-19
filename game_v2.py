"""Guess the number game
I'm thinking of, computer is guessing
"""

#Importing numpy library to generate random numbers
import numpy as np

def random_predict(number: int=1) -> int:
    """_summary_

    Args:
        number (int, optional): thinked of number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        #predicted number
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break #exit the loop when number is guessed
    return(count)

print(f'Количество попыток: {random_predict(10)}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем алгоритм угадывает число.\
       Среднее вычисляется из 1000 подходов

    Args:
        random_predict (_type_): функция угадывания чисел

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    #создаем список из 1000 элементов из случайных чисел от 1 до 100 
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм справляется в среднем за {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_game(random_predict)