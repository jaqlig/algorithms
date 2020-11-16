# Reverse Polish notation algorithm

def infixToPostfix(input):
    
    input = input.split(' ')

    output = ""
    stack = []
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    for i in input:
        if (i.isdigit()):
            output += i + " "

        elif (not stack or i == "(" or stack[-1] == "(" or stack[-1] == ")"):
            stack.append(i)

        elif(i == ")"):
            while (stack[-1] != "("):
                output += stack.pop() + " "
            stack.pop()

        elif(precedence[i] <= precedence[stack[-1]]):
            while not (precedence[i] > precedence[stack[-1]]):
                output += stack.pop() + " "
                if not stack:
                    break
            stack.append(i)

        else:
            stack.append(i)

    while stack:
        output += stack.pop() + " "
    output = output.strip()

    return output


def postfixToInfix(input):
    
    input = input.split(' ')
    output = ""
    stack = []

    for i in input:
        if (i.isdigit()):
            stack.append(i)
            
        else:
            cache = stack.pop()
            operation = "( " + stack.pop() + " " + i + " " + cache + " )"
            stack.append(operation)

    for i in stack:
        output += i + " "
    
    return output

# Converting to postfix notation example:
input1 = "2 * ( 3 + 5 ) + 17 - 88 ^ 3"
print(infixToPostfix(input1))

# Converting to infix notation example:
input2 = "2 3 5 + * 17 + 88 3 ^ -"
print(postfixToInfix(input2))
