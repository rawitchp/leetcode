class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_s = []
        new_t = []
        len_s = len(s)-1
        len_t = len(t)-1
        i = 0
        while len_s >= i or len_t >= i:
            if len_s >= i:
                if s[i] == "#":
                    if len(new_s) == 0:
                        new_s = []
                    else:
                        new_s.pop()
                else:
                    new_s.append(s[i])
            if len_t >= i:
                if t[i] == "#":
                    if len(new_t) == 0:
                        new_t = []
                    else:
                        new_t.pop()
                else:
                    new_t.append(t[i])
            i += 1
        return new_s == new_t