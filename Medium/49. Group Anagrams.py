class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            name = sorted(i)
            name = "".join(name)
            if name in dict:
                dict[name].append(i)
            else:
                dict[name] = [i]
        ans = []
        for i in dict.values():
            ans.append(i)
        return ans