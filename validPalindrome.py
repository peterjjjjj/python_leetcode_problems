def isPalindrome(s):
    s = s.lower()
    s_plain = ''
    for i in range(len(s) - 1):
        if s[i].isalpha():
            s_plain += s[i]
    for i in range((len(s_plain) - 1)//2):
        if s_plain[i] == s_plain[-i]:
            continue
        return False
    return True

if __name__ == '__main__':
    print(isPalindrome("amA"))