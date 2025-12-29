#Simple 2 pointer, re to remove spaces and chars
import re

def solution(s: str) -> bool:
    s = re.sub(r'[\W_]', '', s).lower()

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == "__main__":
    print(solution("ab ,.!ba"))