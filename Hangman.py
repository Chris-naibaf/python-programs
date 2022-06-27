import random

print("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
""")

# List of words
words = ["accountant", "actor", "architect", "astronomer", "author", "baker", "butcher",
         "carpenter", "chef", "cleaner", "dentist", "designer", "doctor", "electrician", "engineer",
         "farmer", "fisherman", "florist", "gardener", "journalist", "judge", "lawyer", "lifeguard",
         "mechanic", "model", "nurse", "painter", "photographer", "pilot", "plumber", "politician",
         "scientist", "secretary", "soldier", "teacher", "translator", "waiter", "veterinarian"]

# Ascii art
lives_6 = """
     _______
    |/      |
    |      
    |      
    |       
    |      
    |
 ___|___
 """

lives_5 = """
     _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
 ___|___
 """

lives_4 = """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
 ___|___
 """

lives_3 = """
     _______
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
 ___|___
 """

lives_2 = """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
 ___|___
 """

lives_1 = """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
 ___|___
 """

lives_0 = """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
 ___|___
 """

man = [lives_0, lives_1, lives_2, lives_3, lives_4, lives_5, lives_6]

# Random selected word converted to list
game_word = list(random.choice(words))  # When using list on a string it makes each char an element

# Blank spaces for game display
blanks = []

for char in game_word:
    blanks.append("__")


def print_blanks():
    for blank in blanks:
        print(f" {blank} ", end="")

    print("\n")


def game_conditions(game_word):
    if game_word == blanks:
        game_word = "".join(game_word)
        print(f"You win!, the word was {game_word}")
        return True

    if lives == 1:
        game_word = "".join(game_word)
        print(f"You lose!, the word was {game_word}")
        return True


game_over = False
lives = 7
while not game_over:
    user_choice = input("Enter a letter or guess: ")

    if user_choice in game_word:
        print(man[lives - 1])
        for i in range(len(game_word)):
            if game_word[i] == user_choice:
                blanks[i] = user_choice

        print_blanks()

    elif len(user_choice) > 1:
        game_word = "".join(game_word)
        if user_choice == game_word:
            print(f"\nYou win!, the word was {game_word}")
            game_over = True
        else:
            lives -= 1
            print(man[lives - 1])
            print_blanks()
    else:
        lives -= 1
        print(man[lives - 1])
        print_blanks()

    game_over = game_conditions(game_word)
