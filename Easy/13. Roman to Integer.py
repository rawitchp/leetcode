class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev1 = ""
        ans = 0
        for i in s:
            if i == "M":
                if prev1 == "C":
                    ans += 800
                else:
                    ans += 1000
            elif i == "D":
                if prev1 == "C":
                    ans += 300
                else:
                    ans += 500
            elif i == "C":
                if prev1 == "X":
                    ans += 80
                else:
                    ans += 100
            elif i == "L":
                if prev1 == "X":
                    ans += 30
                else:
                    ans += 50
            elif i == "X":
                if prev1 == "I":
                    ans += 8
                else:
                    ans += 10
            elif i == "V":
                if prev1 == "I":
                    ans += 3
                else:
                    ans += 5
            elif i == "I":
                ans += 1
            prev1 = i
        return ans