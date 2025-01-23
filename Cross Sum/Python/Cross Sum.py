def cross(num, k=1, wgh=False, alt=False, right=False):
    ans = 0
    count = 1
    sign = 1
    if right == True:
        num = num[::-1]
    for i in range(0, len(num), k):
        char = num[i:i+k]
        if right == True:
            char = char[::-1]
        char = int(char)
        char *= count*sign
        ans += char

        if wgh == True:
            count += 1
        if alt == True:
            sign *= -1

    return ans

def option():
    print()
    print("SELECT CROSS SUM METHOD")
    print("========")
    print("--> 1. Single Digit Sum [N]")
    print("--> 2. Weighted Digit Sum [W]")
    print("--> 3. Alternate Sum [A]")
    print("--> 4. K-Cross Sum [K]")
    print()

    while True:
        choice0 = input("OPTION: ").upper()
        k = 1
        if choice0 in ['N', 'W', 'A', 'K']:
            if choice0 == 'K':
                k = int(input("Enter k: "))
            break
        else:
            print("Invalid")

    choice1 = 'L'
    if not choice0 == 'N':
        choice1 = input("CHOOSE DIRECTION L(def) or R: ").upper()
    return [choice0, choice1, k]

def solve():
    while True:
        num = input("Enter number: ")
        if num.isdecimal():
            break
        else:
            print("Invalid")
    rightOpt = False
    choice = option()
    if choice[1] == 'R':
        rightOpt = True
    match choice[0]:
        case 'N':
            ans = cross(num=num, right=rightOpt)
        case 'W':
            ans = cross(num=num, wgh=True, right=rightOpt)
        case 'A':
            ans = cross(num=num, alt=True, right=rightOpt)
        case 'K':
            ans = cross(num=num, k=choice[2], right=rightOpt)
    print(ans)


solve()
