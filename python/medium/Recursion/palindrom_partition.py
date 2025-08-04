def palindrome_partition(s: str) -> list[list[int]] :
    """
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
    """

    if not s:
        return []

    all_palindromes = []

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def dfs(current_index: int, partition = []) -> None:
        if current_index == len(s):
            all_palindromes.append(partition[:])
            return

        for i in range(current_index, len(s)):
            if is_palindrome(s[current_index : i + 1]):
                partition.append(s[current_index : i + 1])
                dfs(i + 1, partition)
                partition.pop()
            continue

    dfs(0)

    return all_palindromes

if __name__ == '__main__':
    print(palindrome_partition('aab'))
