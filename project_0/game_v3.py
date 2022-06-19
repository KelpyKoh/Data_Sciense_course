"""Guess the number game
I'm thinking of, computer is guessing
"""

#Importing numpy library to generate random numbers
import numpy as np

def not_random_predict(number: int=1) -> int:
    """_summary_

    Args:
        number (int, optional): thinked of number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    #first predicted number
    predict_number = np.random.randint(1,101)
    point1 = 1
    point2 = 101
    
    
    while True:
        count += 1
        
        
        if number == predict_number:
            print(f'Number was {predict_number}')
            break #exit the loop when number is guessed
        
        elif number < predict_number:
            point2 = predict_number
            predict_number = np.random.randint(point1, predict_number)
            
            if predict_number < number:
                point1 = predict_number
                predict_number = np.random.randint(point1, point2)
        
        else:
            point1 = predict_number
            predict_number = np.random.randint(predict_number, point2)
            
            if predict_number > number:
                point2 = predict_number
                predict_number = np.random.randint(point1, point2)
            
    return(count)

print(f'Количество попыток: {not_random_predict(98)}')


def score_game(not_random_predict) -> int:
    """За какое количество попыток в среднем алгоритм угадывает число.\
       Среднее вычисляется из 1000 подходов

    Args:
        random_predict (_type_): функция угадывания чисел

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] #создаем список для подсчета количества попыток в каждом запуске
    np.random.seed(1) #фиксируем сид для воспроизводимости
    #создаем список из 1000 элементов из случайных чисел от 1 до 100 
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(not_random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм справляется в среднем за {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_game(not_random_predict)