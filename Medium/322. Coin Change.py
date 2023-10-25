class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        q = [(amount,0)]
        visited = set()
        while q:
            cur, n_coins = q.pop(0)
            for c in coins:
                new_cur = cur - c
                if new_cur == 0:
                    return n_coins + 1
                if new_cur in visited or new_cur < 0:
                    continue
                q.append((new_cur,n_coins + 1))
                visited.add(new_cur)
        return -1