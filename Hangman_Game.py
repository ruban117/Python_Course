import random
import hangman_art
import hangman_words

life = 6
choose_random = random.choice(hangman_words.word_list)
print(choose_random)
display = []

for _ in range(len(choose_random)):
    display += '_'

end = False

print(hangman_art.logo)

while not end:
    guess = input("Guess the word: ").lower()

    if guess in display:
        print(f"You have already guessed {guess} letter!!")
    for position in range(len(choose_random)):
        letter = choose_random[position]
        if guess == letter:
            display[position] = letter

    if guess not in choose_random:
        print(
            f"Your guessed word {guess} is not present in this word! so you loose your life! remaining life is {life-1}!! So be careful!"
        )
        life -= 1
        if life == 0:
            end = True
            print("You Loose The Game! GAME OVER!!")
    print(' '.join(display))
    if '_' not in display:
        end = True
        print("YES!! You GOT IT !! WINNER!!")
    print(hangman_art.stages[life])
