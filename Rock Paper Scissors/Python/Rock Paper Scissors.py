import random
import time

def screen(text, end="", dy=1): #dy = delay
    for char in text:
        print(char, end="")
        time.sleep(dy/50)
    if not end == None:
        print(end)

def play(score = [0,0]):
    choices = ["Rock", "Paper", "Scissors"]
    
    comp_choice = random.choice(choices)
    screen("Rock(R), Paper(P) or Scissors(S): ", None)
    player_choice = input().upper()
    print()

    while True:
        if player_choice in ['R', 'P', 'S']:
            break
        else:
            print("Invalid")
        player_choice = input("R, P or S: ").upper()
    for choice in choices:
        if choice.startswith(player_choice):
            player_choice = choice
            break
    screen(f"Computer's Choice was >>> {comp_choice} <<<")
    screen(f"Your Choice was >>> {player_choice} <<<")
    print()

    if comp_choice == "Rock" and player_choice == "Scissors":
        winner = "Computer"
        score[1] += 1
    elif comp_choice == "Paper" and player_choice == "Rock":
        winner = "Computer"
        score[1] += 1
    elif comp_choice == "Scissors" and player_choice == "Paper":
        winner = "Computer"
        score[1] += 1
    elif comp_choice == player_choice:
        winner = False
    else:
        winner = "You"
        score[0] += 1

    if winner:
        screen(f"{winner} won this round!!")
    else:
        screen("It was a tie")

    screen(f"PLAYER: {score[0]}")
    screen(f"COMPUTER: {score[1]}")
    screen("\n=======|=======\n")

    return score

def main():
    screen("  ==============\nLets play Rock Paper Scissors!!\n  ==============")
    print()
    screen("Score Aim: ", None)
    aim = int(input())

    score = [0, 0]
    while aim not in score:
        score = play(score)

    if score[0] > score[1]:
        screen("====THE WINNER IS PLAYER====")
    else:
        screen("====THE WINNER IS COMPUTER====")
main()
    
