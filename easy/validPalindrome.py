def isPalindrome(s):
    """"
    O(n)
    O(n)
    """
    s = s.lower()
    s_plain = ''
    for i in range(len(s)):
        if s[i].isalpha() or s[i].isdigit():
            s_plain += s[i]
    for i in range((len(s_plain))//2):
        if s_plain[i] == s_plain[len(s_plain) - i - 1]:
            continue
        return False
    return True

if __name__ == '__main__':
    print(isPalindrome("0P"))