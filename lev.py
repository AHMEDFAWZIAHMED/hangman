import random
from words import words

word = random.choice(words)

letters =  list(word)
used = '_'
results = []
user = ''
trys = 0
turns = 10

while True:
    trys += 1
    letter = input("Type a letter: ")
    user += letter
    
    for i in range(len(letters)):
        if letters[i] != letter and trys == 1:
            results += used
        if letters[i] == letter and trys == 1:
            results += letter
    if trys >= 2:
        for i, (val1, val2) in enumerate(zip(letters, results)):
            if letter == val1:
                val2 = letter
                results[i] = letter
    if letter not in letters:
        turns = turns - 1
        if turns == 9:
            print("9 turns left")
            print("  ------------")
        if turns == 8:
            print("8 turns left")
            print("  ------------")
            print("        0       ")
        if turns == 7:
            print("7 turns left")
            print("  ------------")
            print("        0       ")
            print("        |        ")
        if turns == 6:
            print("6 turns left")
            print("  ------------")
            print("        0       ")
            print("        |        ")
            print("       /         ")
        if turns == 5:
            print("5 turns left")
            print("  ------------")
            print("        0       ")
            print("        |        ")
            print("       / \       ")
        if turns == 4:
            print("4 turns left")
            print("  ------------")
            print("     \  0       ")
            print("        |        ")
            print("       / \       ")
        if turns == 3:
            print("3 turns left")
            print("  ------------")
            print("     \  0  /    ")
            print("        |        ")
            print("       / \       ")
        if turns == 2:
            print("2 turns left")
            print("  ------------")
            print("     \  0  / |  ")
            print("        |        ")
            print("       / \       ")
        if turns == 1:
            print("1 turns left")
            print("Last breaths counting...")
            print("  ------------")
            print("     \  0_| /  ")
            print("        |        ")
            print("       / \       ")
        if turns == 0:
            print("You loose")
            print("You let a kind man die")
            print("  ------------")
            print("        0_|    ")
            print("      / | \      ")
            print("       / \       ")
            print("The word was: {}".format(word))
            break
    
    m_letters = (' '.join(results))
    print(m_letters)

    if results == letters:
        print("Congratulations you wn the Hangman game!")
        break
    print('You used these letters: {}'.format(user))
    continue
     
