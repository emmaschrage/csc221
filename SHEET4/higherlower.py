from random import randint
from gasp.utils import read_yesorno
from gasp.utils import read_number


def game():
    amount = int(input('What number do you want the range to go to? '))
    x = randint(1, (amount))
    print('A whole number between 1 and ' + str(amount) + ' has been choosen!')
    y = 0
    while True:
        y = y + 1
        Guess = read_number()
        if x < Guess:
            print('That number is too high.')
        if x > Guess:
            print('That number is too low.')
        if Guess == x:
            print('That was the number!')
            break
        else:
            print('Try again!')
    if y == 1:
        print('You only took one guess! Amazing Job!')
    if  2 < y < 5 or y == 5:
        print('You made ' + str(y) + ' guesses. Great Job!')
    if y > 5:
        print('You made ' + str(y) + ' guesses. Better luck next time!')
        
    if read_yesorno('Would you like to play again? '):
        print(game())
    else:
        print('Okay! Thanks for playing!')
        
print(game())


