#Bron: https://stackoverflow.com/questions/8114355/loop-until-a-specific-user-input

import random
def randomness():
    randomNumber = random.randint(1, 3)
    while True:
        inputNumber = int(input('Guess a number between 1 and 9: '))
        if inputNumber == randomNumber:
            print('You guessed', inputNumber,', which is the right number!')
            break

randomness()
