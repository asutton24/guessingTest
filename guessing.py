import random
playing = 'y'
print('Guess the Number')
while playing == 'y':
    r = int(input('How big do you want the range to be?\n'))
    num = random.randint(1, r)
    print('Guess a number between 1 and {}'.format(r))
    guess = -1
    while num != guess:
        guess = int(input())
        if guess != num:
            print('Wrong')
    playing = input('You win!\nPlay again? (y to continue)\n')
