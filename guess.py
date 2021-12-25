import random

# def guess(x):
# secret_number=random.randint(1,x)
# guess=0
# while guess !=secret_number:
# guess=int(input(f'Enter your Guess between 1 and{x}: '))

# if guess > secret_number:
#     print(f'Your guess is too high')
# elif guess< secret_number:
#     print(f'Your guess is too low')
#def guess(x):
# secret_number=random.randint(1,x)
# guess=0
# while guess !=secret_number:
# guess=int(input(f'Enter your Guess between 1 and{x}: '))

# if guess > secret_number:
#     print(f'Your guess is too high')
# elif guess< secret_number:
#     print(f'Your guess is too low')

# else:
#     print('Your Guess is correct')

# x=int(input('Enter the max guess number: '))
# guess(x)
# else:
#     print('Your Guess is correct')

# x=int(input('Enter the max guess number: '))
# guess(x)



def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':

        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low

        feedback=input(f'if {guess} is too high (H), too low (l) or correct (c)').lower()

        if feedback =='h':
            high=guess-1
        elif feedback=='l':
                low=guess+1

    print('Hooray computer guesed your number correctly')


computer_guess(20)


