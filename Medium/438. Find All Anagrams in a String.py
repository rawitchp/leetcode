class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict = defaultdict(int)
        for i in p:
            dict[i] += 1
        pop_list = []
        ans = []
        for idx,i in enumerate(s):
            if dict == {}:
                ans.append(idx-len(p))
                char = pop_list.pop(0)
                dict[char] += 1
            if i not in dict:
                while pop_list:
                    char = pop_list.pop(0)
                    dict[char] += 1
                    if char == i:
                        break
            if i in dict:
                dict[i] -= 1
                pop_list.append(i)
                if dict[i] == 0:
                    del dict[i]
        if dict == {}:
            ans.append(len(s)-len(p))
        return ans