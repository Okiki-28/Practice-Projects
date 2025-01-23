import random
import time

with open("Madlibs_text.txt", "r") as file:
    lines = file.readlines()
file.close

def screen(text, end="", dy=1): #dy = delay
    for char in text:
        print(char, end="")
        time.sleep(dy/50)
    if not end == None:
        print(end)

def play():
    screen("LET'S PLAY MADLIBS")
    mlIndex = random.randint(0, (len(lines)//3)-1)
    
    nouns = lines[mlIndex*3].strip("\n").strip(" ").split(" ")
    del nouns[0]
    
    ans = []
    ind = 0
    for noun in nouns:
        ind += 1
        if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            msg = "Enter an"
        else:
            msg = "Enter a"
        phrase = input(f"{ind}. {msg} {noun}: ")
        ans.append(phrase)
        
    text = lines[(mlIndex*3)+2].split(" ")

    ind = 0
    for i in range(len(text)):
        word = text[i]
        if word.startswith("___"):
            word = word.replace("___", ans[ind])
            text[i] = word
            ind += 1
    text = " ".join(text)

    head = lines[(mlIndex*3)+1]
    print("\n\n------------------------------\n")
    screen(head)
    screen(text, end=" ")
    print("------------------------------\n")
    
play()
