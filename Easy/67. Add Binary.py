class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r = 0
        p_a = len(a) - 1
        p_b = len(b) - 1
        r = 0
        ans = ""
        while p_a >= 0 and p_b >= 0:
            if a[p_a] == b[p_b]:
                ans = str(0+r) + ans
                r = 0
                if a[p_a] == "1":
                    r = 1
            else :
                if r == 1:
                    ans = "0" + ans
                    r = 1
                else:
                    ans = "1" + ans
                    r = 0
            p_a -= 1
            p_b -= 1
        print(r)
        if p_a >= 0:
            if r == 1:
                while p_a >= 0:
                    if r == 1 and a[p_a] == "1":
                        r = 1
                        ans = "0" + ans
                    else:
                        ans = str(int(a[p_a])+r) + ans
                        r = 0
                    p_a -= 1
            else:
                ans = a[:p_a+1] + ans

        if p_b >= 0:
            if r == 1:
                while p_b >= 0:
                    
                    if r == 1 and b[p_b] == "1":
                        r = 1
                        ans = "0" + ans
                    else:
                        ans = str(int(b[p_b])+r) + ans
                        r = 0
                    p_b -= 1
            else:
                ans = b[:p_b+1] + ans
        if r == 1:
            return "1" + ans
        return ans

        