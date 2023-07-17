print('Im thinking of a number, try and guess what it is.')
while True: 
    x = int(input('Enter a number: '))
    y = 1234
    if x != y:
        print('Try again.')
    if x == y:
        print('Good job! You guessed the number.')
        break
    