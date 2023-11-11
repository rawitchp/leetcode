class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dict = defaultdict(set)
        for u,v in edges:
            dict[u].add(v)
            dict[v].add(u)

        leaves = []
        for node in dict:
            if len(dict[node]) == 1:
                leaves.append(node)
        while len(dict) > 2:
            new_leaves = []
            for leaf in leaves:
                nei = dict[leaf].pop()
                del dict[leaf]
                dict[nei].remove(leaf)
                if len(dict[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        
        return leaves