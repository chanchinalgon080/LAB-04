def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    tokens = tokenize(expression)

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
    return stack[0]


def tokenize(expression):
    tokens = []
    num = ''
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(num)
                num = ''
            if ch in '+-*/()':
                tokens.append(ch)
    if num:
        tokens.append(num)
    return tokens


def evaluate_expression(expression):
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)

expr = "(3 + 4) * 2"
result = evaluate_expression(expr)
print(f"Result: {result}")  

# TestCase
test_expressions = [
    "5 + 2 * 3",           # 5 + 6 = 11
    "(1 + 2) * (3 + 4)",   # 3 * 7 = 21
    "10 + 2 * 6",          # 10 + 12 = 22
    "100 * (2 + 12)",      # 100 * 14 = 1400
    "100 * (2 + 12) / 14"  # 1400 / 14 = 100
]

for test_expr in test_expressions:
    test_result = evaluate_expression(test_expr)
    print(f"test: {test_expr} = {test_result}")
