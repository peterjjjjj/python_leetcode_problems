def validParentheses(s):
    existing_char = [] #store existing left bracket
    pairs = {'(' : ')', '{' : '}', '[' : ']'}

    for char in s:
        if char in pairs.keys(): #if left bracket
            existing_char.append(char)
        elif char in pairs.values(): #if right bracket
            if not existing_char: #and no existing left brackets
                return False
            else:
                if char == pairs[existing_char.pop()]:
                    continue
                else:
                    return False

    return True

if __name__ == '__main__':
    print(validParentheses("()]"))