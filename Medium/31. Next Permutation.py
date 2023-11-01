class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def search(start,end,target):
            print(nums[start:end+1])
            res = 0
            while start <= end:
                mid = (start+end)//2
                if nums[mid] > target:
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return res
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                up = search(i,len(nums)-1,nums[i-1])
                print(up)
                nums[i-1],nums[up] = nums[up],nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
        return