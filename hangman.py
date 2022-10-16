import random


def hangman():
    word_list = ["younger", "car", "pelosi"]
    random_number = random.randint(0, 2)
    word = word_list[random_number]
    wrong = 0
    stage = ["",
             "__________          ",
             "|         |         ",
             "|         |         ",
             "|         0         ",
             "|        /|\        ",
             "|        / \        ",
             "|       Deadly      "
             ]
    rletters = list(word)
    board =["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stage) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stage[0: e]))
        if "__" not in board:
          print("You Win!")
          print("  ".join(board))
          win = True
          break
    if not win:
        print("\n".join(stage[0: wrong]))
        print("You Fucking LOSER! It was {}.".format(word))

hangman()
