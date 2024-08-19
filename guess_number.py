import random
print('WELCOME TO GUESSING GAME')
print('Can you guess the number?')
print("Let's Start..'")
number=random.randint(1,100)
i=0
while i<100:
    guessing_number = int(input('Guess Your Number: '))
    if guessing_number==number:
        print('You are correct & the number is: ',guessing_number)
    elif guessing_number>number:
        print('Number is too high!',)
    elif guessing_number < number:
        print('Number is too low!', )
    i = i + 1



