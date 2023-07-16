from random import randint
from gasp.utils import read_yesorno


def game():
    amount = int(input('What number do you want the range to go to? '))
    x = randint(1, (amount))
    print('A number between 1 and ' + str(amount) + ' has been choosen!')
    y = 0
    while True:
        y = y + 1
        Guess = int(input('Enter your guess: '))
        if x < Guess:
            print('That number is too high.')
        if x > Guess:
            print('That number is too low.')
        if Guess == x:
            print('That was the number! Awesome job! You guessed right!')
            break
        else:
            print('Try again!')
    print('You made ' + str(y) + " guesses.")
print(game())
Question = input(read_yesorno('Would you like another game? '))
if Question == True:
    print(game())
else:
    print('Okay! Thanks for playing!')
    exit()

