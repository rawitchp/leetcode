class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # pushed = set()
        def recursion(i,sub):
            # if f'{sub}' not in pushed:
            #     ans.append(sub)
            #     pushed.add(f'{sub}')
            if sub not in ans:
                ans.append(sub)  
            if i > len(nums)-1:
                return
            recursion(i+1,sub)
            recursion(i+1,sub+[nums[i]])
        recursion(0,[])
        return ans