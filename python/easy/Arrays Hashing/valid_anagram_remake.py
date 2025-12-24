#Sorting, hash, array
from collections import Counter


class Solution:
    def __init__(self, s: str, t: str):
        self.s = s
        self.t = t

    def sorting(self) -> bool:
        s = sorted(self.s)
        t = sorted(self.t)

        return s == t

    def hash(self) -> bool:
        if len(self.s) != len(self.t):
            return False

        count_s = {}
        count_t = {}

        for char in self.s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in self.t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t

    def array(self) -> bool:
        if len(self.s) != len(self.t):
            return False

        count_s = {}
        count_t = {}

        for i in range(len(self.s)):
            count_s[self.s[i]] = count_s.get(self.s[i], 0) + 1
            count_t[self.t[i]] = count_t.get(self.t[i], 0) + 1

        return count_s == count_t


if __name__ == "__main__":
    testcase = Solution("anagram", "nagaram")
    print(testcase.array())
    print(testcase.hash())
    print(testcase.sorting())





