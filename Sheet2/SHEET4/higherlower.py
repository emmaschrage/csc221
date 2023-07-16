from random import randint
x = randint(1, 1000)
print('A number between 1 and 1000 has been choosen!')
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

