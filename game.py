import random

name = input("What is your name? ")

print("Hello", name, "! Time to play Mystery Word")
def run():
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
            print(selected_word)
            guess = input("Please make only one guess per round.")
            if len(guess) >= 2:
                print("Your guess can only be one letter. Try again!")

            output_word = ""
            tries = 0
            guess_collection = []
            while output_word != selected_word:
                output_word = selected_word
                tries += 1
                if guess in selected_word:
                    guess_collection.append(guess)
                print(f"There is a {guess_collection}")
                for letter in selected_word:
                    if letter not in guess_collection:
                        output_word = output_word.replace(letter, "_")
                print(output_word)
                if output_word == selected_word:
                    print("Congrats! WINNER")
                    print("You guessed the word: " + selected_word)
                    try_again = input("Play again? y/n\n")
                    if try_again == ("y"):
                        run()
                    else:
                        break
                if tries == 8:
                    print("Sorry, you lose!")
                    try_again = input("Play again? y/n\n")
                    if try_again == ("y"):
                        run()
                    else:
                        break
                else:
                    guess = input(f"Please guess 1 letter per round, {8-tries} times left to try!")
    

run()