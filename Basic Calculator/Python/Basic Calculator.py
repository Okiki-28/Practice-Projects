import operator

print("Enter Expression to calculate: ")
while True:
    #expr = "(((12))+2)"
    expr = input()
    if len(expr) < 1:
        print("Invalid!")
        continue
    if expr.isalnum():
        print("Invalid! Include an operation!")
        continue
    if not ((expr[0].isdigit() or expr[0] == '(') and \
            (expr[-1].isdigit()) or expr[-1] == ')'):
        print("Invalid!")
        continue
    break


oper = []
i = 0
operI = 0
while i < len(expr):
    oper.append("")
    while expr[i].isdigit():
        oper[operI] += expr[i]
        i += 1
        if i == len(expr):
            break
    else:
        while not expr[i].isdigit():
            oper.append(expr[i])
            operI += 1
            i += 1
            if i == len(expr):
                break
    operI += 1

while oper[0] == "":
    del oper[0]

print(expr)

def recall(oper=oper, ans = oper[0], skip=False):
    print('-->', oper)
    print(0, ans)
    if ans.isdecimal():
        ans = int(ans)
    elif ans == '(':
        end = oper[:-1]
        if ')' in end:
            end = (end[::-1].index(')'))
            end = len(oper) - end -1
        else:
            end = oper.index(')')
        print(end)
        file = oper[1:end]
        print('1', file)
        ans = recall(file, ans=file[0])
        print('2', ans)
        skip = True
    #try:
    for i in range(len(oper)-1):
        print(" ", oper[i])
        forw = None
        
        if skip == True:
            print('3', oper[i])
            if oper[i] == ')':
                print('4')
                skip = False
            continue
        
        if oper[i+1] == '(':
            file = oper[i+2:]
            print('5', file)
            forw = recall(file, ans=file[0])
            skip = True
            
        if oper[i+1] == oper[i] == '+':
            continue
        if oper[i+1] == oper[i] == '-':
            oper[i+1] = '+'
            continue
        if (oper[i+1] == '+' and oper[i] == '-') or \
           (oper[i] == '+' and oper[i+1] == '-'):
            oper[i+1] = '-'
            continue
        match oper[i]:
            case '+':
                if forw == None:
                    forw = int(oper[i+1])
                print('==>', ans, forw)
                ans = operator.add(ans, forw)
            case '-':
                if forw == None:
                    forw = int(oper[i+1])
                ans = operator.sub(ans, forw)
            case '*':
                if forw == None:
                    forw = int(oper[i+1])
                ans = operator.mul(ans, forw)
            case '/':
                if forw == None:
                    forw = int(oper[i+1])
                ans = operator.truediv(ans, forw)
            case _:
                continue
 #   except:
  #      print(oper[i])
   #     print("Error")
    print("<<6", ans)
    return ans

print(recall())




