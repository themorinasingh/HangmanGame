import random
from words import word_list
from hangmanArt import logo
from hangmanArt import stages



def hangman(list_of_words, art):

    print(logo)

    print("Let's see, if you can save the Man, Guess the word:")

    random_word = random.choice(list_of_words)

    word = [letter for letter in random_word]

    dashes = []

    for i in range(len(word)):
        dashes += ["_"]

    player_lives = 6

    while player_lives > 0 :

        print("".join(dashes))

        print(player_lives)

        letter = input("Enter You Guess:").lower()

        if letter in word:
            letter_index = word.index(letter)
            dashes[letter_index], word[letter_index] = letter,  '_'

        else:
            player_lives -= 1

        print(stages[player_lives])

        if "_" not in dashes:
            print("Game Over, You Win🏆")
            break

        elif player_lives == 0:
            print("Game Over, You are responsible for death of hangman😳")
            print("The word was: " + random_word )


    play_again = input("y/n: ").lower()
    
    if play_again == 'y':
        hangman(list_of_words, art)

    else :
        print("Thank You For Playing")
        return 0






hangman(word_list, stages)