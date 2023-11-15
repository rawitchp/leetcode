class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        w = self.countAndSay(n-1)
        ans = ''
        count = 0
        prev = ''
        for i in str(w):
            if prev == '' or prev == i:
                count += 1
                prev = i
            else:
                ans += str(count) + prev
                prev = i
                count = 1
        ans += str(count) + prev
        return ans