class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        idx = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx