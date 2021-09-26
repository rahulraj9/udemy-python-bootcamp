import platform
print(platform.system())
import random
from wordlist import word_list
from stage import stages
from hangmanlogo import logo
from clear import screen_clear

screen_clear()
print(logo)

random_word = random.choice(word_list)
length_of_random_word = len(random_word)



display_random_word_value = []
for letter in random_word:
    display_random_word_value.append("_")



total_lives = 6
end_of_game = False

while not end_of_game:
    user_input = input(f"Guess the word of {length_of_random_word} letters ").lower()
    screen_clear()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_input:
            display_random_word_value[position] = letter
    if user_input not in random_word:
        total_lives -= 1
        print(stages[total_lives])
            

    print(display_random_word_value)
    if "_" not in display_random_word_value:
        end_of_game = True
        print("you win")
    if total_lives == 0:
        end_of_game =True
        print("You Lose")
        