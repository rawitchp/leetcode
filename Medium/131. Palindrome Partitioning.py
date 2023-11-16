class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dict = defaultdict(bool)
        def isPalindrome(w):
            l = 0
            r = len(w)-1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = []
        def recursion(curr_str,cur_ans,s):
            if len(s) == 0:
                if curr_str == "":
                    ans.append(cur_ans)
                return
            if curr_str+s[0] in dict or isPalindrome(curr_str+s[0]):
                dict[curr_str+s[0]] = True
                recursion("",cur_ans + [curr_str+s[0]],s[1:])
            recursion(curr_str+s[0],cur_ans,s[1:])
        recursion("",[],s)
        return ans