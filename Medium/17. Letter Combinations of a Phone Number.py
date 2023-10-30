class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':[' ']}
        ans = []
        if len(digits) == 0:
            return []
        def recursion(s,w):
            if len(s) == 0:
                ans.append(w)
                return
            for i in dic[s[0]]:
                recursion(s[1:],w + i)
            return
        recursion(digits,"")
        return ans