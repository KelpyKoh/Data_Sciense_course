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
    
    #create counter of attemots
    count = 0
    
    #first predicted number
    predict_number = np.random.randint(1,101)
    
    #create extreme points of number search range 
    point1 = 1
    point2 = 101
    
    
    while True:
        count += 1
        
        
        if number == predict_number:
            break #exit the loop when number is guessed
        
        #if number is less then predicted - change the upper point of the range
        #and choose new number of the new, smaller range
        elif number < predict_number:
            point2 = predict_number
            predict_number = np.random.randint(point1, predict_number)
            
            #if number is bigger then predicted - change the lower point of the range
            #and choose new number of the new, smaller range
            if predict_number < number:
                point1 = predict_number
                predict_number = np.random.randint(point1, point2)
        
        #if number is bigger then predicted - change the lower point of the range
        #and choose new number of the new, smaller range
        else:
            point1 = predict_number
            predict_number = np.random.randint(predict_number, point2)
            
            #if number is less then predicted - change the upper point of the range
            #and choose new number of the new, smaller range
            if predict_number > number:
                point2 = predict_number
                predict_number = np.random.randint(point1, point2)
            
    #So, we made range of search smaller and smaller till number was guessed
    #Function returns number of attempts
    return(count)


print(f'Количество попыток: {not_random_predict(98)}')


def score_game(not_random_predict) -> int:
    """For how many attempts on average the algorithm guesses the number.
       The average is calcelated from 1000 runs.

    Args:
        random_predict (_type_): number guessing function

    Returns:
        int: average number of attempts
    """
    #creating counter of attempts in each run
    count_ls = []
    #fixing seed for reproducibility
    np.random.seed(1)
    #creating list of 1000 elements from random numbers from 1 to 100 
    random_array = np.random.randint(1, 101, size = (1000))
    
    #run function ot_random_predict 1000 times using numbers from random_array
    #append results (number of attempts for each run) in count_ls
    for number in random_array:
        count_ls.append(not_random_predict(number))
    
    #counting average number of attempts
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм справляется в среднем за {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_game(not_random_predict)