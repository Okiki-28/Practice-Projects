import time

def screen(text, end="", dy=1): #dy = delay
    for char in text:
        print(char, end="")
        time.sleep(dy/50)
    if not end == None:
        print(end)

def dd(n):
    n = str(n)
    if len(n) < 2:
        n = '0'+n
    return n

def counter():
    screen("Enter number to count to: ", end=None)
    n = int(input())

    curr_time = time.time()
    for a in range(1, n+1):
        curr_time += 1
        print('-->', dd(a))
        time.sleep(max(0, curr_time-time.time()))

def countdown():
    screen("Enter countdown number: ", end=None)
    n = int(input())

    curr_time = time.time()
    for a in range(n+1):
        curr_time += 1
        print('-->', dd(n-a))
        time.sleep(max(0, curr_time-time.time()))

def timer():
    screen("*Input x at the end of a time unit to disregard leeser ones")
    while True:
        h = input("Enter Hours: ")
        if h.endswith('x') and h[:-1].isdecimal():
            h = h[:-1]
            m = 0
            s = 0
            break
        if not h.isdecimal():
            print("Invalid")
            continue
            
        m = input("Enter Minutes: ")
        if m.endswith('x') and m[:-1].isdecimal():
            m = m[:-1]
            s = 0
            break
        if not m.isdecimal():
            print("Invalid")
            continue
        
        s = input("Enter Seconds: ")
        if not s.isdecimal():
            print("Invalid")
            continue
        break
    h = int(h)
    m = int(m)
    s = int(s)
        
    total = h*60*60 + m*60 + s
    curr_time = time.time()
    for a in range(total+1):
        curr_time += 1
        print(f"{dd(h)}:{dd(m)}:{dd(s)}")

        s -= 1
        if s < 0:
            m -= 1
            s = 59
        if m < 0:
            h -= 1
            m = 59
        if h < 0:
            h = 0
            m = 0
            s = 0
        time.sleep(max(0, curr_time-time.time()))

def option():
    screen("\nMain Menu")
    screen("===========")
    screen("-> Counter [C]")
    screen("-> Countdown [D]")
    screen("-> Timer [T]")

    choice = input("\nOption: ").upper()
    while choice not in ['C', 'D', 'T']:
        print("Invalid")
        choice = input("Option: ").upper()
    return choice

def main():
    screen("MY COUNTER PROGRAM")
    choice = option()
    match choice:
        case 'C':
            counter()
        case 'D':
            countdown()
        case 'T':
            timer()
    
main()









