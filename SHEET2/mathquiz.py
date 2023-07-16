from random import randint

right = 0
x = int(input('How many questions do you want to solve? '))
for x in range(x):
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    question = "What is " + str(num1) + " times " + str(num2) + "? "
    answer = int(input(question))
    product = num1 * num2
    if answer == product:
        print('Yes! The answer is ' + str(product) + '. ')
        print('You answered correctly!')
        right = right + 1
    else:
        print('Sorry thats wrong!')
        print('The correct answer is actually ' + str(product) + '. ')
x = x + 1
print("I asked you " + str(x) + " questions. You got " + str(right) + " of them right.")
print("Well done!")
          