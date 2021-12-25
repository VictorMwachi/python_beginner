import random
import string


def hangman():
    fruits=['Mango','lemon','banana','Apple','pineaple','pawpaw']
    secret_word=random.choice(fruits)
    word_letters=set(secret_word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    print(secret_word)

    while len(word_letters)>0:
        print('You have used this letters',' '.join(used_letters))

        word_list=(letter if letter in used_letters else '-' for letter in secret_word)

        print('Current word',' '.join(word_list))

        user_letter=input('ENTER  LETTER YOU GUESSED: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
        elif user_letter in used_letters:
            print('Print you have already used character')

        else:
            print ('Enter a valid character')



hangman()

