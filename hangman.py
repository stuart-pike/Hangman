import random


from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
already_guessed_letters = []

for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6
print(logo)

#print(f"Psst, the solution is {chosen_word}")
while not end_of_game:
    guess = input("Chose a character ").lower()

    if guess in already_guessed_letters:
        print(f"You have already guessed {guess}")
    else:
        already_guessed_letters.append(guess)

        for position in range(word_length):
            if guess == chosen_word[position]:
                display[position] = guess

        if guess not in display:
            print(f"You guessed {guess}, your life is getting shorter")
            lives -= 1

        print(*display)
        print(stages[lives])

        if "_" not in display:
            end_of_game = True
            print("YOU WIN!")

        if lives == 0:
            end_of_game = True
            print("YOU LOSE!")
