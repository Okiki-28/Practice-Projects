import random
import time
with open('dogs.txt', 'r') as dog_names:
    lines = dog_names.readlines()
dog_names.close()

card_group = []
cards = []
temp_list = []
computer_cards = []
player_cards = []
category = ["Exercise: ", "Intelligence: ", "Friendliness: ", "Droll: "]

def read_str(*string, tm=0.02):
    for word in string:
        for letter in str(word):
            print(letter, end='', flush=True)
            time.sleep(tm)
    print('')

def game():
    read_str("WELCOME TO CELEBRITY DOGS GAME!!!", tm=0.07)
    p_top = 0
    c_top = 0
    read_str("Enter number of cards: ")
    total_cards = int(input())
    while (not total_cards % 2 == 0) or (not 3<total_cards<31):
        read_str("Unacceptable")
        total_cards = int(input("Enter number of cards: "))
    read_str(f"Choosing {total_cards} Cards...", tm=(total_cards/(2**2))*0.1)
    time.sleep((total_cards/(2**2))*0.5)
    while len(cards)<total_cards:
        randy = (random.randint(0, 29))
        new = lines[randy].rstrip("\n")
        if not new in cards:
            cards.append(new)
    for a in cards:
        temp_list = []
        temp_list.append(a)
        temp_list.append(random.randint(1, 5)) #Exercise
        temp_list.append(random.randint(1, 100)) #Intelligence
        temp_list.append(random.randint(1, 10)) #Friendliness
        temp_list.append(random.randint(1, 10)) #Droll
        card_group.append(temp_list)
    for z in range(len(card_group)//2):
        player_cards.append(card_group[z])
        computer_cards.append(card_group[-(z+1)])
    """for a in range(len(player_cards)): #Checking for stored code
        read_str(player_cards[a])
        read_str(computer_cards[a])
        read_str("____")"""
    
    # Player's turn
    def player_turn(curr):
        nonlocal p_top
        nonlocal c_top
        read_str("**PLAYER'S TURN**")
        play = player_cards[curr]
        read_str("\n--PLAYER CARD--")
        read_str(play[0])
        read_str(f"1. Exercise: {play[1]}")
        read_str(f"2. Intelligence: {play[2]}")
        read_str(f"3. Friendliness: {play[3]}")
        read_str(f"4. Droll: {play[4]}")
        read_str("---------------\n")

        cate = int(input("Enter a category [1-4]: "))
        while not 0<cate<5:
            read_str("Invalid!!")
            cate = int(input("Enter a category(1-4): "))
        read_str(f"Category Chosen: {category[cate-1][:-2]}")

        read_str("\n--COMPUTER CARD--")
        read_str(computer_cards[c_top][0], tm=0.0125)
        read_str(f"1. Exercise: {computer_cards[c_top][1]}", tm=0.0125)
        read_str(f"2. Intelligence: {computer_cards[c_top][2]}", tm=0.0125)
        read_str(f"3. Friendliness: {computer_cards[c_top][3]}", tm=0.0125)
        read_str(f"4. Droll: {computer_cards[c_top][4]}", tm=0.0125)
        read_str("---------------\n")
        
        
        read_str("---------------")
        read_str("Player: ",category[cate-1], play[cate])
        read_str("Computer: ",category[cate-1], computer_cards[c_top][cate])
        read_str("---------------")
        if cate == 1 or cate == 2 or cate == 3:
            if play[cate] >= computer_cards[c_top][cate]:
                read_str("\n---Player Has Won This Round!---\n")
                player_cards.append(computer_cards[c_top])
                del computer_cards[c_top]
                p_top += 1
            else:
                read_str("\n---Computer Has Won This Round!---\n")
                computer_cards.append(player_cards[curr])
                del player_cards[curr]
                c_top += 1
        else:
            if play[cate] <= computer_cards[c_top][cate]:
                read_str("\n---Player Has Won This Round!---\n")
                player_cards.append(computer_cards[c_top])
                del computer_cards[c_top]
                p_top += 1
            else:
                read_str("\n---Computer Has Won This Round!---\n")
                computer_cards.append(player_cards[curr])
                del player_cards[curr]
                c_top += 1
        read_str("---------------")
        read_str(f"player: {len(player_cards)} cards")
        read_str(f"computer: {len(computer_cards)} cards")
        read_str("---------------\n")

    def computer_turn(curr):
        nonlocal p_top
        nonlocal c_top
        read_str("**COMPUTER'S TURN**")
        play = computer_cards[curr]
        read_str("\n--COMPUTER CARD--")
        read_str(play[0])
        read_str(f"1. Exercise: {play[1]}")
        read_str(f"2. Intelligence: {play[2]}")
        read_str(f"3. Friendliness: {play[3]}")
        read_str(f"4. Droll: {play[4]}")
        read_str("---------------\n")

        cate = random.randint(1, 4)
        read_str(f"Category Chosen: {category[cate-1][:-2]}")

        read_str("\n--PLAYER CARD--")
        read_str(player_cards[p_top][0], tm=0.0125)
        read_str(f"1. Exercise: {player_cards[p_top][1]}", tm=0.0125)
        read_str(f"2. Intelligence: {player_cards[p_top][2]}", tm=0.0125)
        read_str(f"3. Friendliness: {player_cards[p_top][3]}", tm=0.0125)
        read_str(f"4. Droll: {player_cards[p_top][4]}", tm=0.0125)
        read_str("---------------\n")
        
        read_str("---------------")
        read_str("Computer: ",category[cate-1], play[cate])
        read_str("Player: ",category[cate-1], player_cards[p_top][cate])
        read_str("---------------")
        
        if cate == 1 or cate == 2 or cate == 3:
            if play[cate] > player_cards[p_top][cate]:
                read_str("\n---Computer Has Won This Round!---\n")
                computer_cards.append(player_cards[p_top])
                del player_cards[p_top]
                c_top += 1
            else:
                read_str("\n---Player Has Won This Round!---\n")
                player_cards.append(computer_cards[curr])
                del computer_cards[curr]
                p_top += 1
        else:
            if play[cate] < player_cards[p_top][cate]:
                read_str("\n---Computer Has Won This Round!---\n")
                computer_cards.append(player_cards[p_top])
                del player_cards[p_top]
                c_top += 1
            else:
                read_str("\n---Player Has Won This Round!---\n")
                player_cards.append(computer_cards[curr])
                del computer_cards[curr]
                p_top += 1
        read_str("---------------")
        read_str(f"player: {len(player_cards)} cards")
        read_str(f"computer: {len(computer_cards)} cards")
        read_str("---------------\n")

    count = 0
    while len(player_cards)>0 and len(computer_cards)>0:
        read_str(f"\nRound {count+1}", tm=0.05)
        if count % 2 == 0:
            player_turn(p_top)
            count+=1
        else:
            computer_turn(c_top)
            count+=1
        if p_top == len(player_cards):
            p_top = 0
        elif c_top == len(computer_cards):
            c_top = 0

    if len(player_cards) == 0:
        read_str("|--THE WINNER IS COMPUTER--|")
    elif len(computer_cards) == 0:
        read_str("|--THE WINNER IS PLAYER--|")
        
game()
