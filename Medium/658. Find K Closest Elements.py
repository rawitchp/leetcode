class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        last = k-1
        for i in range(k,len(arr)):
            if abs(arr[i]-x) < abs(arr[i-k]-x):
                last = i
        return arr[last-k+1:last+1]