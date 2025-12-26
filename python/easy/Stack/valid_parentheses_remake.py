def valid_parentheses(s: str) -> bool:
    stack = []
    pair = {'(' : ')', '[' : ']', '{' : '}'}

    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if char != pair[stack.pop()]:
                return False

    return len(stack) == 0

if __name__ == '__main__':
    print(valid_parentheses('()'))