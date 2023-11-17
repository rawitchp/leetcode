class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        count = [0] * len(primes)
        ans = [0] * n
        ans[0] = 1
        for i in range(1,n):
            min_sum = float('inf')
            min_digit = -1
            for j in range(len(count)):
                if ans[i-1] >= primes[j]*ans[count[j]]:
                    count[j] += 1
                if primes[j]*ans[count[j]] < min_sum:
                    min_sum = primes[j]*ans[count[j]]
                    min_digit = j
            ans[i] = min_sum
            count[min_digit] += 1
        return ans[-1]