import random
import os

def clrscr():
    if os.name == "nt":
        clrscr()
    else:
        os.system("clear")

def get_player_input(player_name, word):
    print(f"{player_name}, your turn!", end="\n\n")
    answer = input("What is on your mind >> ")
    if answer.lower() == word:
        return 1
    if answer.lower() == "#show":
        clrscr()
        print(f"The mystry word is {word.capitalize()}!!", end="\n\n")
        return -1
    else:
        clrscr()
        print("Sorry wrong guess!!", end="\n\n")
        return 0
    
def choose():
    words = ['apple', 'banana', 'orange', 'mango', 'pineapple', 'strawberry', 'kiwi', 'grape', 'blueberry', 'raspberry', 'watermelon', 'peach', 'plum', 'cherry', 'lemon', 'lime', 'apricot', 'blackberry', 'avocado', 'papaya', 'pomegranate', 'cranberry', 'cantaloupe', 'grapefruit', 'coconut', 'fig', 'guava', 'passionfruit', 'tangerine', 'nectarine', 'persimmon', 'date', 'kiwifruit', 'currant', 'elderberry', 'lychee', 'dragonfruit', 'boysenberry', 'starfruit', 'gooseberry', 'huckleberry', 'plantain', 'raspberry', 'melon', 'cherry', 'grape', 'plum', 'peach', 'mango', 'apricot', 'tangerine', 'lemon', 'lime', 'kiwi', 'coconut', 'grapefruit', 'blueberry', 'strawberry', 'pineapple', 'blackberry', 'watermelon', 'orange', 'papaya', 'passionfruit', 'pomegranate', 'cantaloupe', 'cranberry', 'fig', 'guava', 'date', 'kiwifruit', 'lychee', 'persimmon', 'nectarine', 'currant', 'elderberry', 'boysenberry', 'starfruit', 'plantain', 'huckleberry', 'raspberry', 'melon', 'cherry', 'grape', 'plum', 'peach', 'mango', 'apricot', 'tangerine', 'lemon', 'lime', 'kiwi', 'coconut', 'grapefruit', 'blueberry', 'strawberry', 'pineapple', 'blackberry', 'watermelon', 'orange']
    return random.choice(words)     
    
def jumple(word):
    list_word = list(word)
    random.shuffle(list_word)
    return "".join(list_word)

def thank(p1name, p2name, p1points, p2points):
    print("Thank you for playing the Jumpled Game!!", end="\n\n")
    if p1points > p2points:
        print(f"Congratulations {p1name} you are the winner!!", end="\n\n")
    elif p1points == p2points == 0:
        print(f"{p1name} and {p2name}, what are you two even doing??", end="\n\n")
    elif p1points == p2points:
        print(f"It's a draw!!\nWell done {p1name} and {p2name}!!", end="\n\n")
    else:
        print(f"Congratulations {p2name} you are the winner!!", end="\n\n")
    print(f"{p1name} scored: {p1points}", end="\n\n")
    print(f"{p2name} scored: {p2points}", end="\n\n")


def continue_game(prompt, word=""):
    c = input(prompt)[0]
    if c in ('Y', 'y'):
        return True
    else:
        if word != "":
            print(f"The mystry word is {word}!!", end="\n\n")
        return False
        
def process_name(p1name, p2name):
    run = True
    while (run):
        clrscr()
        p1name = input("Enter your name player 1: ")
        p2name = input("Enter your name player 2: ")
        p1name = p1name.capitalize()
        p2name = p2name.capitalize()

        if p1name == p2name:
            print("\nHmm, so you both have the same name!!")
            print("Trust me it is gonna get hella confusing!!", end="\n\n")            
            ch = input("Would like to change your name? (Y/N) >> ")
            if ch == 'N' or ch == 'n':
                print("\nWell, I warned you!! (GOOD LUCK)", end="\n\n")
                input("Press Enter to exit...")
            else:
                continue
        run = False
    clrscr()
    return p1name, p2name
    
    
def play():
    p1name = ""
    p2name = ""
    p1name, p2name = process_name(p1name, p2name)
    p1points = 0
    p2points = 0
    turn = 1
    game_run = True
    round_run = True
    while (game_run):
        no_turns = 0
        round_run = True
        word = choose()
        jumpled_word = jumple(word)
        while (round_run):
            no_turns += 1
            print("Find the word: ", jumpled_word, end="\n\n")
            if turn == 1:
                player_input = get_player_input(p1name, word)
                if player_input == 1:
                    p1points += 1
                    print(f"{p1name} you got it right!!", end="\n\n")
                    round_run = False
                elif player_input == -1:
                    round_run = False
                turn = turn % 2 + 1
            else:
                player_input = get_player_input(p2name, word)
                if player_input == 1:
                    p2points += 1
                    print(f"{p2name} you got it right!!", end="\n\n")
                    round_run = False
                elif player_input == -1:
                    round_run = False
                else:
                    if no_turns > 3:
                        round_run = continue_game("Would you like to continue? (Y/N) >> ", word)
                        clrscr()
                        no_turns = 0
                turn = turn % 2 + 1
            if round_run:
                continue
            else:
                round_run = False
                game_run = continue_game("Would you like to start another game? (Y/N) >> ")
                clrscr()
        if not game_run:
            thank(p1name, p2name, p1points, p2points)
            input("Press Enter to exit...")


play()
