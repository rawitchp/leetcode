class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[0] = True
        for i in range(1,len(s)+1):
            for j in wordDict:
                len_j = len(j)
                if i-len_j >= 0 and check[i-len_j] and s[:i].endswith(j):
                    check[i] = True
        return check[-1]