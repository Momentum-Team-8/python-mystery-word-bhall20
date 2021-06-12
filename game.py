import random

name = input("What is your name? ")

print("Hello", name, "! Time to play Mystery Word")

with open("words.txt") as f:
    word_list = f.read().splitlines()
    game_difficulty = None
    while True:
        try:
            game_difficulty = int(input("What difficulty would you like to play? Choose 1 for easy, 2 for normal, 3 for hard.  "))
            break
        except: 
            print("You have to type a value of 1, 2, or 3.  ")
            game_difficulty = int(input("What difficulty would you like to play? Choose 1 for easy, 2 for normal, 3 for hard.  "))
            break
    if game_difficulty == 1:
        l1_list = [word for word in word_list if len(word) >= 4 and len(word) <= 6]
        selected_word = random.choice(l1_list)
        print("Your word is", len(selected_word), "letters long.")

        guess = input("Please make only one guess per round.")
        if len(guess) >= 2:
            print("Your guess can only be one letter. Try again!")

