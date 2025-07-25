def longest_common_subsequence(text1: str, text2: str) -> int:
    #Initialize the dp.
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

if __name__ == "__main__":
    print(longest_common_subsequence(text1="abc", text2="abcdef"))
