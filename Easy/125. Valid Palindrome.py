class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def letters(input):
            return ''.join([c for c in input if c.isalpha() or c.isdigit()])
        word = letters(s).lower()
        # word = "".join(re.split('\W', s)).lower()
        l = 0
        r = len(word) - 1
        while l < r:
            if(word[l] != word[r]):
                return False
            l+=1
            r-=1
        return True