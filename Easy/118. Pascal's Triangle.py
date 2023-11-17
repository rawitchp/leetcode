class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            lists = []
            for j in range(i+1):
                if j == 0 or j == i:
                    lists.append(1)
                else:
                    lists.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(lists)
        return ans