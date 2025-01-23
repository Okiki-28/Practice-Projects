import random
import time

with open("words.txt", 'r') as file:
    words = file.readlines()
file.close()
words = words[0][1:-1].split('","')

def screen(text, end="", dy=1): #dy = delay
    for char in text:
        print(char, end="")
        time.sleep(dy/50)
    if not end == None:
        print(end)

def play():
    word = random.choice(words).upper()
    progress = ["_" for i in range(len(word))]
    trials_i = 7
    won = False
    used_letters = []

    screen(f"You have {trials_i} lives")
    while trials_i>0:
        screen(f"\nCurrent Word: {' '.join(progress)}")
        screen("\nGuess a Letter: ", end=None)
        while True:
            char = input().upper()
            if len(char) > 1:
                screen("Invalid input, one letter only: ", end=None)
                continue
            elif len(char) < 1:
                screen("Enter at least one letter: ", end=None)
                continue
            elif char in used_letters:
                screen("You've used this letter already")
                screen("Pick again: ", end=None)
                continue
            break
        print()
        used_letters.append(char)        

        if char in word:
            screen(f"Your guess '{char}' is in the word")
            for i,letter in enumerate(word):
                if char == letter:
                    progress[i] = char            
        else:
            screen(f"Your guess '{char}' is not in the word")
            trials_i -= 1

        if '_' not in progress: 
            return True, word
        
        screen(f"Guessed Characters : '{' '.join(used_letters)}'\n")
        screen(f"You've used {7-trials_i}/7 lives")

    return False, word

def main():
    screen("  ==============\nLets play Hangman!!\n  ==============")
    while True:
        won = play()

        if won[0] == True:
            screen("\n =====\nCongratulations\n =====")
            screen(f"You found the word: {won[1]}!!")
        else:
            screen(f"\n  You Lost, the word was: {won[1]}\n")

        screen("\n Will you like to go again? [Y/N]: ", end=None)
        repeat = input().upper()

        if not repeat == 'Y':
            print("\n======|======\n")
            break
main()
