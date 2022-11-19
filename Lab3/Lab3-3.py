Operators = set(['+', '-', '*', '/', '(', ')', '^'])
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def display(z,x,output):
    print("|   ", z, " " * (7 - len(z)),
          "|   ", x, " " * (6 - len(x)),
          "|   ", output, " " * (6 - len(output)), "|")

def infixToPostfix(infix):
    stack = []
    output = ''
    infixList = []

    for push in infix:
        infixList.append(push)
    print("|    Infix    |   Stack    |   Postfix  |")
    print("-----------------------------------------")
    for char in infix:
        z = ''
        x = ''
        for i in infixList:
            z += i

        for j in stack:
          if len(stack) != 2:
            x += j
            x = x+"  "
          else:
            x += j

        if char == '(':
            display(z,x,output)
            stack.append('(')
            infixList.pop(0)

        elif char == ')':
            display(z,x,output)
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
            infixList.pop(0)

        elif char not in Operators:
            display(z,x,output)
            output += char
            infixList.pop(0)

        else:
            display(z,x,output)
            while stack and stack[-1] != '(' and Priority[char] <= Priority[stack[-1]]:
                output += stack.pop()
            stack.append(char)
            infixList.pop(0)

    z = ''
    for loop in infixList:
        z += loop
    display(z,x,output)
    while stack:
        x = ''
        output += stack.pop()
        for loop2 in stack:
            x += loop2
    display(z,x,output)

infix = "A*(B+C)"
print('Infix : ', infix, "\n")
infixToPostfix(infix)

