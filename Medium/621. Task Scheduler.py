class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        dict = Counter(tasks)
        heap = []
        for i in dict:
            heapq.heappush(heap,dict[i])
        heapq._heapify_max(heap)
        mx = heapq._heappop_max(heap)
        mx_cnt = 1 
        while heap:
            count = heapq._heappop_max(heap)
            if count == mx:
                mx_cnt += 1
            else:
                break
        return max((mx - 1) * (n + 1) + mx_cnt, len(tasks))
