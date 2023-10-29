class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        a = ""
        for i in s:
            if i.isdigit():
                a += i
            else:
                break
        if a == "":
            return 0
        a = int(a) * sign
        if a > pow(2,31) - 1:
            return pow(2,31) - 1
        elif a < pow(-2,31):
            return pow(-2,31)
        return a 